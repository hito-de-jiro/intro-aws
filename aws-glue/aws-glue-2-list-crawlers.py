import boto3
import json

client = boto3.client('glue', region_name='us-west-2')
response = client.list_crawlers()
print(json.dumps(response, indent=4, sort_keys=True, default=str))

