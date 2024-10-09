
# Image Management Application

This project is a cloud-based image management application using AWS and Python.

## Features
- Upload, list, and download images.
- Optional encryption for image security.
- User authentication with login and signup functionality.
- Hosted on AWS EC2 with images stored in AWS S3.

## Setup Instructions
1. Clone this repository.
2. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```
3. Set up AWS credentials and `.env` file with the necessary environment variables:
   ```
   S3_BUCKET_NAME=your-s3-bucket-name
   ENCRYPTION_KEY=your-encryption-key
   SECRET_KEY=your-flask-secret-key
   ```
4. Run the application:
   ```
   python app.py
   ```
