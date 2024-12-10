import boto3

EC2_RESOURCE = boto3.resource('ec2')

for instance in EC2_RESOURCE.instances.all():
    print(instance.id)
    