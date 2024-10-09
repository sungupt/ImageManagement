# ImageManagement

This project is a cloud-based image management application using AWS and Python.

## Features
-It Upload, list, and download images.
-Has Optional encryption for image security.
- User authentication with login and signup functionality.


## Setup Instructions
1. Clone this repository.
2. Install the required Python packages:
   pip install -r requirements.txt
3. Set up AWS credentials and `.env` file with the necessary environment variables:
   ```
   S3_BUCKET_NAME=your-s3-bucket-name
   ENCRYPTION_KEY=your-encryption-key
   SECRET_KEY=your-flask-secret-key
   ```
4. Run the application:

   python app.py

