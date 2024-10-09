from flask import Flask, render_template, request, redirect, url_for, session
from utils.aws_helper import upload_image_to_s3, list_images_from_s3, delete_image_from_s3
from utils.auth_helper import register_user, login_user, authenticate
import os
from config import Config
import boto3
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'your_secret_key')

# Initialize the S3 client
s3_client = boto3.client(
    's3',
    aws_access_key_id=Config.AWS_ACCESS_KEY,
    aws_secret_access_key=Config.AWS_SECRET_KEY,
    region_name='us-east-1'  # Ensure this is a valid region
)

# Function to upload a file to S3
def upload_file_to_s3(file_name, bucket_name, object_name=None):
    try:
        s3_client.upload_file(file_name, bucket_name, object_name or file_name)
        print(f'Uploaded {file_name} to {bucket_name} as {object_name or file_name}')
    except Exception as e:
        print(f'Error uploading to S3: {e}')

# Image Upload
@app.route('/upload', methods=['GET', 'POST'])
@authenticate
def upload():
    if request.method == 'POST':
        file = request.files['file']  # Get the file from the form
        file_name = file.filename
        bucket_name = 'my-flask-image'  # Replace with your bucket name
        object_name = f'uploads/{file_name}'  # Define the object name for S3

        # Save the uploaded file temporarily before uploading
        file.save(file_name)  # Save it to a temporary location

        # Upload to S3
        upload_file_to_s3(file_name, bucket_name, object_name)

        # Optionally, remove the temporary file after upload
        os.remove(file_name)  # Clean up the temporary file
        return redirect(url_for('list_images'))  # Redirect to the list page
    
    return render_template('upload.html')

# List Images
@app.route('/list', methods=['GET'])
@authenticate
def list_images():
    images = list_images_from_s3('my-flask-image')  # Replace with your bucket name
    return render_template('list_images.html', images=images)

# Delete an Image
@app.route('/delete/<filename>', methods=['POST'])
@authenticate
def delete(filename):
    bucket_name = 'my-flask-image'  # Replace with your bucket name
    delete_image_from_s3(bucket_name, f'uploads/{filename}')  # Delete from S3
    return redirect(url_for('list_images'))  # Redirect to the list page

# User Registration (Signup)
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if register_user(username, password):
            return redirect(url_for('login'))
        else:
            return "Signup failed. Try again."
    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True)
