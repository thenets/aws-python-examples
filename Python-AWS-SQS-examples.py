# pip install boto3 python-dotenv
# Env var "SQS_QUEUE_URL" must exist

# Load env
from dotenv import load_dotenv
from pathlib import Path
load_dotenv(dotenv_path=(Path('.') / '.env'))

# Libs
import boto3
import os
from pprint import pprint as pp

# --- Examples

def getMessage(queue_url):
    # Receive message from SQS queue
    response = sqs.receive_message(
        QueueUrl=queue_url,
        AttributeNames=[
            'SentTimestamp'
        ],
        MaxNumberOfMessages=1,
        MessageAttributeNames=[
            'All'
        ],
        VisibilityTimeout=0,
        WaitTimeSeconds=0
    )

    try:
        return response['Messages'][0]
    except:
        return None

# Create SQS client
sqs = boto3.client('sqs')
queue_url = os.environ['SQS_QUEUE_URL']

# SQS Create
print("# SQS Create")
sqs.send_message(
    QueueUrl=queue_url,
    MessageBody='{"pokemon": "Vulpix"}'
)

# SQS Receive
print("# SQS Receive")
out = getMessage(queue_url)
pp(out)

# SQS Delete
print("# SQS Delete")
sqs.delete_message(
    QueueUrl=queue_url,
    ReceiptHandle=out['ReceiptHandle']
)
