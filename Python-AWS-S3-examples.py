# pip install boto3 python-dotenv
# Env var "S3_BUCKET_NAME" must exist
# Local file './images-input/cat.jpg' must exist
# Local dir './images-output' must exist

# Load env
from dotenv import load_dotenv
from pathlib import Path
load_dotenv(dotenv_path=(Path('.') / '.env'))

# Libs
import boto3
import os
from pprint import pprint as pp

# --- Examples

# Create S3 client
s3 = boto3.client('s3')

# S3 Upload new file
s3_bucket_name = os.environ['S3_BUCKET_NAME']
local_input_dir_name = './images-input'
local_input_file_name = 'cat.jpg'
with open((local_input_dir_name + "/" + local_input_file_name), "rb") as f:
    s3_object_name = "my-files/" + local_input_file_name
    s3.upload_fileobj(f, s3_bucket_name, s3_object_name)

# S3 Download file
s3_bucket_name = os.environ['S3_BUCKET_NAME']
local_output_dir_name = './images-output'
local_output_file_name = 'dog.jpg'
remote_object_name = "my-files/cat.jpg"
with open((local_output_dir_name + "/" + local_output_file_name), 'wb') as f:
    s3.download_fileobj(s3_bucket_name, s3_object_name, f)

# S3 Delete file
s3_bucket_name = os.environ['S3_BUCKET_NAME']
remote_object_name = "my-files/cat.jpg"
s3.delete_object(
    Bucket = s3_bucket_name,
    Key = remote_object_name
)
