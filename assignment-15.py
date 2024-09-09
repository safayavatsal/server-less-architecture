import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
    bucket_name = 'your-bucket-name'
    
    lifecycle_policy = {
        'Rules': [
            {
                'ID': 'MoveToGlacier',
                'Prefix': '',
                'Status': 'Enabled',
                'Transitions': [
                    {
                        'Days': 30,
                        'StorageClass': 'GLACIER'
                    }
                ],
                'Expiration': {
                    'Days': 365
                }
            }
        ]
    }
    
    # Apply the lifecycle policy
    s3.put_bucket_lifecycle_configuration(
        Bucket=bucket_name,
        LifecycleConfiguration=lifecycle_policy
    )
    
    return {
        'statusCode': 200,
        'body': 'Lifecycle policy applied.'
    }
