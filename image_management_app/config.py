import os

class Config:
    # AWS Configuration
    AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')
    AWS_SECRET_KEY = os.getenv('AWS_SECRET_KEY')
    AWS_REGION = os.getenv('AWS_REGION', 'us-east-1')
    S3_BUCKET_NAME = os.getenv('S3_BUCKET_NAME')
    
    # Flask Application Configuration
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_flask_secret_key')  # Used for Flask sessions

    # Encryption Configuration
    ENCRYPTION_KEY = os.getenv('ENCRYPTION_KEY', 'your_default_encryption_key')

    # EC2 Configuration (if you need it)
    EC2_INSTANCE_ID = os.getenv('EC2_INSTANCE_ID')
    EC2_PUBLIC_IP = os.getenv('EC2_PUBLIC_IP')
