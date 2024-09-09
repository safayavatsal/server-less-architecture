import boto3
from datetime import datetime, timedelta

cloudwatch = boto3.client('cloudwatch')

def lambda_handler(event, context):
    instance_id = 'your-ec2-instance-id'
    
    # Fetch EC2 CPU utilization metrics from CloudWatch
    response = cloudwatch.get_metric_statistics(
        Namespace='AWS/EC2',
        MetricName='CPUUtilization',
        Dimensions=[{'Name': 'InstanceId', 'Value': instance_id}],
        StartTime=datetime.utcnow() - timedelta(minutes=5),
        EndTime=datetime.utcnow(),
        Period=300,
        Statistics=['Average']
    )
    
    # Log metrics
    if response['Datapoints']:
        cpu_util = response['Datapoints'][0]['Average']
        print(f"EC2 instance {instance_id} CPU utilization: {cpu_util}%")
    
    return {'statusCode': 200, 'body': 'EC2 metrics logged.'}
