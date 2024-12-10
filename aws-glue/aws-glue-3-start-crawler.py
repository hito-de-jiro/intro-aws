import boto3
import json

client = boto3.client('glue', region_name="us-west-2")
response = client.list_crawlers()
response2 = client.start_crawler(
    Name=response['CrawlerNames'][0]
)

print(json.dumps(response2, indent=4, sort_keys=True, default=str))
