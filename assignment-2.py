import boto3
from datetime import datetime, timedelta

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket_name = 'your-bucket-name'
    threshold_date = datetime.now() - timedelta(days=30)
    
    objects = s3.list_objects_v2(Bucket=bucket_name)
    if 'Contents' in objects:
        for obj in objects['Contents']:
            obj_date = obj['LastModified']
            if obj_date < threshold_date:
                s3.delete_object(Bucket=bucket_name, Key=obj['Key'])
                print(f'Deleted {obj["Key"]}')
