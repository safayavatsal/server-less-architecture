import boto3
import json

def lambda_handler(event, context):
    logs = boto3.client('logs')
    sns = boto3.client('sns')
    
    # Iterate over log events from CloudWatch Logs
    for record in event['Records']:
        log_data = json.loads(record['body'])
        message = log_data.get('message', '')
        
        # Check for error keywords in log messages
        if 'ERROR' in message or 'FATAL' in message:
            sns.publish(
                TopicArn='arn:aws:sns:region:account-id:LogAlerts',
                Message=f'Error detected in logs: {message}'
            )
            print(f"Error Alert: {message}")
