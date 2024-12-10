import boto3

EC2_CLIENT = boto3.client('ec2')

response = EC2_CLIENT.describe_instances()
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        print(instance['InstanceId'])
        