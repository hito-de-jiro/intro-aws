import boto3

s3 = boto3.resource('s3')

for bucket in s3.buckets.all():
    print(bucket.name)

bucket = 'my-first-aws-htdjr-bucket'

with open('test.jpg', 'rb') as data:
    s3.Bucket(bucket).put_object(Key='test.jpg', Body=data)