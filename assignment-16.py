import boto3

ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    instance_id = 'your-ec2-instance-id'
    
    # Describe EC2 instance status
    response = ec2.describe_instance_status(InstanceIds=[instance_id])
    
    for instance in response['InstanceStatuses']:
        state = instance['InstanceState']['Name']
        if state == 'running' and instance['InstanceStatus']['Status'] != 'ok':
            ec2.reboot_instances(InstanceIds=[instance_id])
            print(f"Rebooted EC2 instance {instance_id}")
    
    return {'statusCode': 200, 'body': 'EC2 instance checked.'}
