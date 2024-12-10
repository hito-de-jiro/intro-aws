import boto3
import json



client = boto3.client('glue', region_name="us-west-2")
response = client.create_crawler(
    Name='S3Crawler',
    Role='GlueFullAccess',
    DatabaseName='S3CrawlerHOC',
    Targets={
        'S3Targets': [
            {
                'Path': 's3://glue-source-hoc/read',
                'Exclusions': [
                    'string',
                ],
                'SampleSize': 2
            },
            {
                'Path': 's3://glue-source-hoc/write',
                'Exclusions': [
                    'string',
                ],
                'SampleSize': 2
            },
        ]
    },
    Schedule='cron(15 12 * * ? *)',
    SchemaChangePolicy={
        'UpdateBehavior': 'UPDATE_IN_DATABASE',
        'DeleteBehavior': 'DEPRECATE_IN_DATABASE'
    },
    RecrawlPolicy={
        'RecrawlBehavior': 'CRAWL_EVERYTHING'
    },
    LineageConfiguration={
        'CrawlerLineageSettings': 'DISABLE'
    }
)
print(json.dumps(response, indent=4, sort_keys=True, default=str))
