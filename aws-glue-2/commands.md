Create dir for read
```bash
aws s3api put-object --bucket my-test-bucket-for-glue-source-hoc --key read/
```
Create dir for write
```bash
aws s3api put-object --bucket my-test-bucket-for-glue-source-hoc --key write/
```
Copy file to
```bash
aws s3 cp ./iris.csv s3://my-test-bucket-for-glue-source-hoc/read
```
Copy python file 
```bash
aws s3 cp ./iris_onboarder.py s3://my-test-bucket-for-glue-source-hoc
```