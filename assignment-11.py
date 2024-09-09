import boto3
from datetime import datetime, timedelta
import os
import zipfile

s3 = boto3.client('s3')
ec2 = boto3.resource('ec2')

def lambda_handler(event, context):
    bucket_name = 'your-backup-bucket'
    instance_id = 'your-ec2-instance-id'
    backup_path = '/path/to/backup'
    
    # Step 1: Connect to EC2 and create a backup
    instance = ec2.Instance(instance_id)
    instance.console_output()  # Dummy action to simulate connection
    zip_filename = f"{instance_id}_backup_{datetime.now().strftime('%Y%m%d')}.zip"
    
    # Create zip file of the backup folder
    with zipfile.ZipFile('/tmp/' + zip_filename, 'w') as backup_zip:
        for foldername, subfolders, filenames in os.walk(backup_path):
            for filename in filenames:
                backup_zip.write(os.path.join(foldername, filename))
    
    # Step 2: Upload zip file to S3
    s3.upload_file('/tmp/' + zip_filename, bucket_name, zip_filename)
    print(f"Backup uploaded: {zip_filename}")
    
    # Step 3: Delete backups older than 30 days
    thirty_days_ago = datetime.now() - timedelta(days=30)
    response = s3.list_objects_v2(Bucket=bucket_name)
    if 'Contents' in response:
        for obj in response['Contents']:
            if obj['LastModified'] < thirty_days_ago:
                s3.delete_object(Bucket=bucket_name, Key=obj['Key'])
                print(f"Deleted old backup: {obj['Key']}")
    
    return {
        'statusCode': 200,
        'body': 'Backup and cleanup complete.'
    }
