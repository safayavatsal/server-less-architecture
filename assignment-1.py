import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    
    # Describe instances with tag 'Action' and value 'Auto-Stop'
    stop_response = ec2.describe_instances(
        Filters=[{'Name': 'tag:Action', 'Values': ['Auto-Stop']}]
    )
    
    stop_instance_ids = [
        instance['InstanceId']
        for reservation in stop_response['Reservations']
        for instance in reservation['Instances']
        if instance['State']['Name'] != 'stopped'
    ]
    
    if stop_instance_ids:
        ec2.stop_instances(InstanceIds=stop_instance_ids)
        print(f'Stopped instances: {stop_instance_ids}')
    
    # Describe instances with tag 'Action' and value 'Auto-Start'
    start_response = ec2.describe_instances(
        Filters=[{'Name': 'tag:Action', 'Values': ['Auto-Start']}]
    )
    
    start_instance_ids = [
        instance['InstanceId']
        for reservation in start_response['Reservations']
        for instance in reservation['Instances']
        if instance['State']['Name'] != 'running'
    ]
    
    if start_instance_ids:
        ec2.start_instances(InstanceIds=start_instance_ids)
        print(f'Started instances: {start_instance_ids}')
