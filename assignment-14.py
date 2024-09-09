import boto3
import json

sns = boto3.client('sns')

def lambda_handler(event, context):
    sns_topic = 'your-sns-topic-arn'
    
    # Extract EC2 state change details from the event
    instance_id = event['detail']['instance-id']
    state = event['detail']['state']
    
    # Send an SNS notification
    sns.publish(
        TopicArn=sns_topic,
        Message=f"EC2 Instance {instance_id} changed state to {state}.",
        Subject='EC2 State Change'
    )
    
    return {'statusCode': 200, 'body': json.dumps('Notification sent.')}
