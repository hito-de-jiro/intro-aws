import boto3
import json

client = boto3.client('glue', region_name='us-west-2')
response = client.start_job_run(
    JobName='IrisJob',
)

print(json.dumps(response, indent=2, sort_keys=True, default=str))
