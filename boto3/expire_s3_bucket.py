import logging
import boto3
import datetime, os, json, boto3
from botocore.exceptions import ClientError

session = boto3.session.Session(profile_name='default')
s3 = session.client('s3')


#s3 = boto3.client('s3')
response = s3.list_buckets()

# Output the bucket names
print('Existing buckets:')
for bucket in response['Buckets']:
    # print(f'  {bucket["Name"]}')
    #if 'log' in bucket['Name']:
        BUCKET = bucket["Name"]
        print(BUCKET)
        try:
            policy_status = s3.put_bucket_lifecycle_configuration(
                Bucket=BUCKET,
                LifecycleConfiguration={
                  'Rules': [{
                             'ID': 'ITrule',
                             'Expiration': {
                             'Days': 1
                             },
                            'Filter': {'Prefix': ''},
                            'Status': 'Enabled'
                         }
                      ]
                }
            )                 
            print(response)
        except ClientError as e:
            print("Unable to apply bucket policy. \nReason:{0}".format(e))
