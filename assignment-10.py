import boto3
import json

cloudwatch = boto3.client('cloudwatch')
sns = boto3.client('sns')

def lambda_handler(event, context):
    elb_name = 'your-elb-name'
    sns_topic = 'your-sns-topic-arn'
    
    # Get the 5xx error count from CloudWatch
    response = cloudwatch.get_metric_statistics(
        Namespace='AWS/ELB',
        MetricName='HTTPCode_ELB_5XX_Count',
        Dimensions=[{'Name': 'LoadBalancerName', 'Value': elb_name}],
        StartTime=datetime.utcnow() - timedelta(minutes=5),
        EndTime=datetime.utcnow(),
        Period=300,
        Statistics=['Sum']
    )
    
    if response['Datapoints'] and response['Datapoints'][0]['Sum'] > 10:
        sns.publish(
            TopicArn=sns_topic,
            Message=f"5xx errors exceed threshold: {response['Datapoints'][0]['Sum']}",
            Subject='ELB 5xx Errors Alert'
        )
        print("Notification sent!")
    
    return {'statusCode': 200, 'body': json.dumps('Check Complete')}
