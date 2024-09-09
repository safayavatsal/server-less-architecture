import boto3
from datetime import datetime, timedelta

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    
    # Get instances running for more than 7 days
    instances = ec2.describe_instances(
        Filters=[{'Name': 'instance-state-name', 'Values': ['running']}]
    )
    
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            launch_time = instance['LaunchTime']
            if launch_time < (datetime.now() - timedelta(days=7)).replace(tzinfo=None):
                ec2.terminate_instances(InstanceIds=[instance['InstanceId']])
                print(f"Terminated idle instance: {instance['InstanceId']}")
