import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    
    # Process the S3 event
    for record in event['Records']:
        bucket_name = record['s3']['bucket']['name']
        object_key = record['s3']['object']['key']
        
        print(f"Object {object_key} changed in bucket {bucket_name}")
    
    return {'statusCode': 200, 'body': 'S3 event processed.'}
