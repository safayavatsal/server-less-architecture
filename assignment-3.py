import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    buckets = s3.list_buckets()

    for bucket in buckets['Buckets']:
        bucket_name = bucket['Name']
        encryption = None
        try:
            encryption = s3.get_bucket_encryption(Bucket=bucket_name)
        except Exception as e:
            print(f'Bucket {bucket_name} does not have encryption enabled.')
            continue
        if not encryption:
            print(f'Bucket {bucket_name} is unencrypted.')
