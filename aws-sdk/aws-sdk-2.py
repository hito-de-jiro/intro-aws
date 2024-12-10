import boto3

S3_RESOURCE = boto3.resource('s3')
bucket = 'my-first-aws-htdjr-bucket'

for obj in S3_RESOURCE.Bucket(bucket).objects.all():
    print(obj.key)
