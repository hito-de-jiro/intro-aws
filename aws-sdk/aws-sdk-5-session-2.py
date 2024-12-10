import boto3

session = boto3.Session()

s3_client = session.client('s3')
s3_resource = session.resource('s3')

for bucket in s3_client.list_buckets()['Buckets']:
    print(bucket['Name'])

# Create a new bucket
s3_client.create_bucket(Bucket='my-new-bucket')

# Uploading a file
s3_client.upload_file(
    'test.txt',
    'my-new-bucket',
    'test.txt'
)
# Downloading a file
s3_client.download_file(
  'my-bucket',
  'my_file.txt',
  'local_file.txt'
)
# Deleting a file
s3_client.delete_object(
  Bucket='my-bucket',
  Key='my_file.txt'
)