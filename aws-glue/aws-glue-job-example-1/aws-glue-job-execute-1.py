import boto3
import json
import os

session = boto3.Session(
    aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
    aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'],
)

client = session.client('glue', region_name="us-west-2")
response = client.create_job(
    Name='IrisJob',
    Role='AWSGlueServiceRole',
    Command={
        'Name': 'glueetl',
        'ScriptLocation': 's3://my-test-bucket-for-glue-source-hoc/iris_onboarder.py',
        'PythonVersion': '3'
    },
    DefaultArguments={
      '--TempDir': 's3://my-test-bucket-for-glue-source-hoc/temp_dir',
      '--job-bookmark-option': 'job-bookmark-disable'
    },
    MaxRetries=1,
    GlueVersion='3.0',
    NumberOfWorkers=2,
    WorkerType='Standard'
)

print(json.dumps(response, indent=4, sort_keys=True, default=str))