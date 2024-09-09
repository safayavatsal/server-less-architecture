import boto3
from datetime import datetime, timedelta

s3 = boto3.client('s3')

def lambda_handler(event, context):
    bucket_name = 'your-bucket-name'
    six_months_ago = datetime.now() - timedelta(days=180)
    
    # List objects in the S3 bucket
    response = s3.list_objects_v2(Bucket=bucket_name)
    
    if 'Contents' in response:
        for obj in response['Contents']:
            # Check if the object is older than 6 months
            if obj['LastModified'] < six_months_ago:
                # Change storage class to Glacier
                s3.copy_object(Bucket=bucket_name,
                               CopySource={'Bucket': bucket_name, 'Key': obj['Key']},
                               Key=obj['Key'],
                               StorageClass='GLACIER')
                print(f"Archived: {obj['Key']}")
    return {
        'statusCode': 200,
        'body': json.dumps('Archival Complete')
    }
