import boto3
import json

s3 = boto3.client('s3')
sns = boto3.client('sns')

def lambda_handler(event, context):
    sns_topic = 'your-sns-topic-arn'
    
    # List all S3 buckets
    response = s3.list_buckets()
    
    for bucket in response['Buckets']:
        bucket_name = bucket['Name']
        acl = s3.get_bucket_acl(Bucket=bucket_name)
        
        # Check for public permissions
        for grant in acl['Grants']:
            if 'URI' in grant['Grantee'] and 'AllUsers' in grant['Grantee']['URI']:
                sns.publish(TopicArn=sns_topic, Message=f"Bucket {bucket_name} has public access.")
                print(f"Bucket {bucket_name} is public!")
    
    return {'statusCode': 200, 'body': json.dumps('Audit complete.')}
