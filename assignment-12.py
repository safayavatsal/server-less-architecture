import boto3
import json

cloudwatch = boto3.client('cloudwatch')
ec2 = boto3.client('ec2')
sns = boto3.client('sns')

def lambda_handler(event, context):
    elb_name = 'your-elb-name'
    sns_topic = 'your-sns-topic-arn'
    high_threshold = 80
    low_threshold = 20
    
    # Fetch network load metric from CloudWatch
    response = cloudwatch.get_metric_statistics(
        Namespace='AWS/ELB',
        MetricName='NetworkIn',
        Dimensions=[{'Name': 'LoadBalancerName', 'Value': elb_name}],
        StartTime=datetime.utcnow() - timedelta(minutes=5),
        EndTime=datetime.utcnow(),
        Period=300,
        Statistics=['Average']
    )
    
    load = response['Datapoints'][0]['Average'] if response['Datapoints'] else 0
    
    # Check load to scale instances
    if load > high_threshold:
        ec2.run_instances(
            ImageId='your-ami-id',
            InstanceType='t2.micro',
            MinCount=1,
            MaxCount=1
        )
        sns.publish(TopicArn=sns_topic, Message="Scaled up EC2 instance due to high load.")
    elif load < low_threshold:
        instances = ec2.describe_instances(
            Filters=[{'Name': 'instance-state-name', 'Values': ['running']}]
        )
        if instances['Reservations']:
            instance_id = instances['Reservations'][0]['Instances'][0]['InstanceId']
            ec2.terminate_instances(InstanceIds=[instance_id])
            sns.publish(TopicArn=sns_topic, Message="Scaled down EC2 instance due to low load.")
    
    return {'statusCode': 200, 'body': json.dumps('Scaling complete.')}
