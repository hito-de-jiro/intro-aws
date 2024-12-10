import boto3

EC2_RESOURCE = boto3.resource('ec2')
EC2_CLIENT = EC2_RESOURCE.meta.client

paginator = EC2_CLIENT.get_paginator('describe_instances')
ec2_instances = []
for page in paginator.paginate():
    for reservation in page['Reservations']:
        for instance in reservation['Instances']:
            ec2_instances.append(instance['InstanceId'])
print('\n'.join(ec2_instances))
