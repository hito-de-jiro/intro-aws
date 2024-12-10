Create S3 bucket 
```bash
aws s3 mb s3://my-test-bucket-for-aws-glue-1
```
Downloading only .jpg files
```bash
aws s3 cp Images/ s3://[bucketname] --recursive --include "*.jpg"
```
Show buckets list
```bash
aws s3 ls
```
Show buckets list as json
```bash
aws s3api list-buckets
```
Remove empty bucket
```bash
aws s3 rb s3://my-test-bucket-for-aws-glue-1
```
Remove not empty bucket
```bash
aws s3 rb s3://my-test-bucket-for-aws-glue-2 --force
```
Downloading file to S3
```bash
aws s3 cp ./test.jpg s3://my-test-bucket-for-aws-glue-1/test.jpg
```