import boto3
import json

def lambda_handler(event, context):
    sns = boto3.client('sns')
    cloudwatch = boto3.client('cloudwatch')
    
    # Get current billing metrics
    response = cloudwatch.get_metric_statistics(
        Namespace='AWS/Billing',
        MetricName='EstimatedCharges',
        Dimensions=[{'Name': 'Currency', 'Value': 'USD'}],
        StartTime=(datetime.now() - timedelta(days=1)).isoformat(),
        EndTime=datetime.now().isoformat(),
        Period=86400,
        Statistics=['Maximum']
    )
    
    if response['Datapoints']:
        current_billing = response['Datapoints'][0]['Maximum']
        
        # Send an SNS alert if billing exceeds $100 (adjust threshold as needed)
        if current_billing > 100:
            sns.publish(
                TopicArn='arn:aws:sns:region:account-id:BillingAlerts',
                Message=f'Alert! Your AWS bill has exceeded $100. Current bill: {current_billing:.2f} USD.'
            )
            return {
                'statusCode': 200,
                'body': json.dumps(f'Alert sent: Billing is ${current_billing:.2f}')
            }
