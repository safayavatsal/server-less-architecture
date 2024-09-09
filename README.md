# server-less-architecture

# AWS Lambda Automation Assignments

## Overview
This repository contains solutions for various AWS Lambda automation assignments. Each assignment demonstrates how to use AWS Lambda and Boto3 to automate different AWS tasks, including EC2 instance management, S3 bucket cleanup, and more.

## Assignments

### Assignment 1: Automated Instance Management Using AWS Lambda and Boto3
**Objective:** Automate the stopping and starting of EC2 instances based on tags.

**Steps:**
1. **EC2 Setup:** Create two EC2 instances and tag them appropriately.
2. **Lambda IAM Role:** Create a role with `AmazonEC2FullAccess`.
3. **Lambda Function:** Write a Boto3 script to stop and start instances based on tags.
4. **Testing:** Manually invoke the Lambda function and verify instance states.

### Assignment 2: Automated S3 Bucket Cleanup Using AWS Lambda and Boto3
**Objective:** Automate the deletion of files older than 30 days in an S3 bucket.

**Steps:**
1. **S3 Setup:** Create an S3 bucket and upload files with varying ages.
2. **Lambda IAM Role:** Create a role with `AmazonS3FullAccess`.
3. **Lambda Function:** Write a Boto3 script to delete old files.
4. **Testing:** Manually trigger the Lambda function and verify file deletion.

### Assignment 3: Monitor Unencrypted S3 Buckets Using AWS Lambda and Boto3
**Objective:** Detect S3 buckets without server-side encryption.

**Steps:**
1. **S3 Setup:** Create buckets with and without encryption.
2. **Lambda IAM Role:** Create a role with `AmazonS3ReadOnlyAccess`.
3. **Lambda Function:** Write a Boto3 script to find unencrypted buckets.
4. **Testing:** Manually trigger the Lambda function and review logs.

### Assignment 4: Automatic EBS Snapshot and Cleanup Using AWS Lambda and Boto3
**Objective:** Automate EBS snapshots creation and cleanup of old snapshots.

**Steps:**
1. **EBS Setup:** Identify or create an EBS volume.
2. **Lambda IAM Role:** Create a role with `AmazonEC2FullAccess`.
3. **Lambda Function:** Write a Boto3 script to create and delete EBS snapshots.
4. **Event Source (Bonus):** Attach CloudWatch Events for periodic triggering.
5. **Testing:** Verify snapshot creation and deletion.

### Assignment 5: Auto-Tagging EC2 Instances on Launch Using AWS Lambda and Boto3
**Objective:** Automatically tag newly launched EC2 instances.

**Steps:**
1. **EC2 Setup:** Ensure EC2 instances can be launched.
2. **Lambda IAM Role:** Create a role with `AmazonEC2FullAccess`.
3. **Lambda Function:** Write a Boto3 script to tag new instances.
4. **CloudWatch Events:** Set up a rule to trigger the Lambda function.
5. **Testing:** Launch a new instance and check tags.

### Assignment 6: Monitor and Alert High AWS Billing Using AWS Lambda, Boto3, and SNS
**Objective:** Alert when AWS billing exceeds a specified threshold.

**Steps:**
1. **SNS Setup:** Create an SNS topic and subscribe your email.
2. **Lambda IAM Role:** Create a role with permissions to read billing metrics and send SNS notifications.
3. **Lambda Function:** Write a Boto3 script to monitor billing and send alerts.
4. **Event Source (Bonus):** Set up CloudWatch Events for daily checks.
5. **Testing:** Trigger the function and verify SNS notifications.

### Assignment 7: DynamoDB Item Change Alert Using AWS Lambda, Boto3, and SNS
**Objective:** Alert on DynamoDB item updates.

**Steps:**
1. **DynamoDB Setup:** Create a DynamoDB table and add items.
2. **SNS Setup:** Create an SNS topic and subscribe your email.
3. **Lambda IAM Role:** Create a role with permissions to read DynamoDB Streams and send SNS notifications.
4. **Lambda Function:** Write a Boto3 script to handle item changes and send alerts.
5. **DynamoDB Stream:** Enable streams and attach the Lambda function.
6. **Testing:** Update items and check SNS notifications.

### Assignment 8: Analyze Sentiment of User Reviews Using AWS Lambda, Boto3, and Amazon Comprehend
**Objective:** Analyze and categorize the sentiment of user reviews.

**Steps:**
1. **Lambda IAM Role:** Create a role with permissions to use Amazon Comprehend.
2. **Lambda Function:** Write a Boto3 script to analyze sentiment and log results.
3. **Testing:** Trigger the function with sample reviews and check logs.

### Assignment 9: Archive Old Files from S3 to Glacier Using AWS Lambda and Boto3
**Objective:** Move files older than 6 months from S3 to Glacier.

**Steps:**
1. **S3 Setup:** Create a bucket and upload files.
2. **Lambda IAM Role:** Create a role with `AmazonS3FullAccess`.
3. **Lambda Function:** Write a Boto3 script to change storage class to Glacier.
4. **Testing:** Trigger the function and verify file archiving.

### Assignment 10: Notify When ELB 5xx Errors Spike Using AWS Lambda, Boto3, and SNS
**Objective:** Alert on high 5xx errors in ELB.

**Steps:**
1. **SNS Setup:** Create an SNS topic and subscribe to it.
2. **Lambda IAM Role:** Create a role with permissions to read ELB metrics and send SNS notifications.
3. **Lambda Function:** Write a Boto3 script to check 5xx errors and send alerts.
4. **CloudWatch Events:** Schedule Lambda function to run every 5 minutes.
5. **Testing:** Simulate or wait for errors and check notifications.

### Assignment 11: EC2 Backup and File Cleanup Using Lambda, Boto3, and S3
**Objective:** Back up EC2 data to S3 and delete backups older than 30 days.

**Steps:**
1. **Lambda IAM Role:** Create a role with permissions for EC2 and S3.
2. **Lambda Function:** Write a Boto3 script to back up files and clean old backups.
3. **CloudWatch Events:** Schedule Lambda function to run daily.
4. **Testing:** Verify backup creation and cleanup.

### Assignment 12: Auto-Scale EC2 Instances Based on Load Using AWS Lambda, Boto3, and SNS
**Objective:** Scale EC2 instances based on ELB network load.

**Steps:**
1. **SNS Setup:** Create an SNS topic and subscribe to it.
2. **Lambda IAM Role:** Create a role with permissions to read ELB metrics, manage EC2 instances, and send SNS notifications.
3. **Lambda Function:** Write a Boto3 script to scale instances and send notifications.
4. **CloudWatch Events:** Schedule Lambda function to run every 5 minutes.
5. **Testing:** Simulate load changes and verify scaling actions.

### Assignment 13: Audit S3 Bucket Permissions and Notify for Public Buckets
**Objective:** Audit S3 bucket permissions and notify if any buckets are public.

**Steps:**
1. **SNS Setup:** Create an SNS topic and subscribe to it.
2. **Lambda IAM Role:** Create a role with permissions to list S3 bucket permissions and send SNS notifications.
3. **Lambda Function:** Write a Boto3 script to check bucket permissions and send alerts.
4. **CloudWatch Events:** Schedule Lambda function to run daily.
5. **Testing:** Make buckets public and verify notifications.

### Assignment 14: Monitor EC2 Instance State Changes Using AWS Lambda, Boto3, and SNS
**Objective:** Monitor and notify EC2 instance state changes.

**Steps:**
1. **SNS Setup:** Create an SNS topic and subscribe to it.
2. **Lambda IAM Role:** Create a role with permissions to read EC2 instance states and send SNS notifications.
3. **Lambda Function:** Write a Boto3 script to handle state changes and send notifications.
4. **EC2 Event Bridge:** Set up a rule to trigger Lambda on state changes.
5. **Testing:** Start or stop instances and check notifications.

### Assignment 15: Implement a Log Cleaner for S3
**Objective:** Automatically delete logs older than 90 days from an S3 bucket.

**Steps:**
1. **Lambda Function:** Create a function to list and delete logs older than 90 days.
2. **Schedule:** Use EventBridge to run the function weekly.
3. **Testing:** Verify log deletion after running the function.

### Assignment 16: Automated SNS Alerts for EC2 Disk Space Utilization
**Objective:** Alert on high disk space utilization in EC2 instances.

**Steps:**
1. **Lambda Function:** Create a function to check disk space and send SNS alerts if usage exceeds 85%.
2. **Schedule:** Use CloudWatch Events to trigger the function daily.
3. **Testing:** Verify SNS notifications when utilization is high.

### Assignment 17: Restore EC2 Instance from Snapshot
**Objective:** Create a new EC2 instance from the latest snapshot.

**Steps:**
1. **Lambda Function:** Write a function to fetch the latest snapshot and create a new instance.
2. **Trigger:** Manually or schedule the function based on recovery needs.
3. **Testing:** Verify instance creation from the snapshot.

### Assignment 18: Autosave EC2 Instance State Before Shutdown
**Objective:** Save EC2 instance state to S3 before shutdown.

**Steps:**
1. **Lambda Function:** Write a function to save instance state to S3 before termination.
2. **Trigger:** Use CloudWatch Events to detect termination and invoke the function.
3. **Testing:** Verify state saving to S3 before

### Assignment 19: Automated Lambda Cleanup for Stale DynamoDB Entries

**Objective:** Automate the cleanup of stale or expired items in a DynamoDB table using AWS Lambda and Boto3.

**Steps:**
1. **Configure DynamoDB and Lambda:**
  - **DynamoDB Setup:** Create a DynamoDB table with a TTL (Time to Live) attribute to manage expiration.
  - **Lambda IAM Role:** Set up an IAM role with AmazonDynamoDBFullAccess and CloudWatchLogsFullAccess permissions.
2. **Implement the Lambda Function:**
  - **Function Code:** Write a Python Lambda function using Boto3 to scan the table and delete expired items based on the TTL attribute.
  - **Testing:** Manually invoke the Lambda function to ensure it correctly deletes stale items and checks CloudWatch Logs for execution details.
3. **Automate and Monitor:**
  - **Schedule Lambda:** Create a CloudWatch Events rule to automatically trigger the Lambda function daily.
  - **Monitor:** Verify the automated cleanup process by checking the DynamoDB table and CloudWatch Logs.
