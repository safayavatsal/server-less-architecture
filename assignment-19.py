import boto3

ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    instance_ids = ['your-ec2-instance-id']
    
    # Stop the EC2 instances
    ec2.stop_instances(InstanceIds=instance_ids)
    print(f"Stopped EC2 instances: {instance_ids}")
    
    return {'statusCode': 200, 'body': 'EC2 instances stopped.'}
