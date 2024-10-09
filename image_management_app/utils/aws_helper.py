import boto3
import os
# Initialize the S3 client
s3_client = boto3.client(
    's3',
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY'),
    aws_secret_access_key=os.getenv('AWS_SECRET_KEY'),
    region_name=os.getenv('AWS_REGION')
)

def upload_image_to_s3(file_name, bucket_name, object_name=None):
    try:
        s3_client.upload_file(file_name, bucket_name, object_name or file_name)
        print(f'Uploaded {file_name} to {bucket_name} as {object_name or file_name}')
    except Exception as e:
        print(f'Error uploading to S3: {e}')

def list_images_from_s3(bucket_name):
    try:
        response = s3_client.list_objects_v2(Bucket=bucket_name)
        images = [content['Key'] for content in response.get('Contents', [])]
        return images
    except Exception as e:
        print(f'Error listing images from S3: {e}')
        return []

def delete_image_from_s3(bucket_name, object_name):
    try:
        s3_client.delete_object(Bucket=bucket_name, Key=object_name)
        print(f'Deleted {object_name} from {bucket_name}')
    except Exception as e:
        print(f'Error deleting from S3: {e}')