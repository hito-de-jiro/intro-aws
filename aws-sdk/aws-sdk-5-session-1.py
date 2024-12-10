import boto3
import os

session = boto3.session.Session(
    aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
    aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'],
    region_name='us-west-2',
)

S3_CLIENT = session.client('s3')
