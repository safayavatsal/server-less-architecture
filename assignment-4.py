import boto3
import json

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    
    # Extract parameters from API Gateway event
    action = event['queryStringParameters']['action']
    instance_id = event['queryStringParameters']['instance_id']
    
    if action == 'start':
        ec2.start_instances(InstanceIds=[instance_id])
        return {
            'statusCode': 200,
            'body': json.dumps(f'Started instance {instance_id}')
        }
    elif action == 'stop':
        ec2.stop_instances(InstanceIds=[instance_id])
        return {
            'statusCode': 200,
            'body': json.dumps(f'Stopped instance {instance_id}')
        }
