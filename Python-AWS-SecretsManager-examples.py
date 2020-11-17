# pip install boto3 python-dotenv
# Env var "S3_BUCKET_NAME" must exist
# Local file './images-input/cat.jpg' must exist
# Local dir './images-output' must exist

# %%

# Load env
from dotenv import load_dotenv
from pathlib import Path
load_dotenv(dotenv_path=(Path('.') / '.env'))

# Libs
import boto3
import os
import json
from pprint import pprint as pp

# --- Examples

# Create S3 client
secretsmanager = boto3.client('secretsmanager')

response = secretsmanager.get_secret_value(
    SecretId='dev/cafe'
)

# Convert secret string to dict
secret = json.loads(response['SecretString'])
pp(secret)
