import boto3
import json

client = boto3.client('glue', region_name="us-west-2")
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