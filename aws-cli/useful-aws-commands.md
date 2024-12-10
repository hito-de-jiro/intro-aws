Find AWS account ID
```bash
aws sts get-caller-identity --query Account --output text
```
Find the canonical ID
```bash
aws s3api list-buckets --query Owner.ID --output text
```
