# Expire large S3 buckets (~16 Milion items or more)
boto3 to expire all items in bucket

When you have 16M items in a S3 bucket you can expire them by using this boto3 script<br>
Delete 16M items in bucket will take over 2 weeks, that why expiring method is prefered as AWS does it for you
