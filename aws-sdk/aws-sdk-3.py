import boto3

S3_CLIENT = boto3.client('s3')

bucket = 'my-first-aws-htdjr-bucket'

with open('test.jpg', 'rb') as data:
    S3_CLIENT.Bucket(bucket).put_object(Key='test.jpg', Body=data)
