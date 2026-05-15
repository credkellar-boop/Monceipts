import boto3
import os

def upload_receipt_to_cloud(file_path, tx_hash):
    """Uploads the generated PNG to S3-compatible storage."""
    s3 = boto3.client(
        's3',
        aws_access_key_id=os.getenv("AWS_KEY"),
        aws_secret_access_key=os.getenv("AWS_SECRET"),
        endpoint_url=os.getenv("S3_ENDPOINT")
    )
    
    bucket_name = "monceipts-assets"
    object_name = f"receipts/{tx_hash}.png"
    
    try:
        s3.upload_file(file_path, bucket_name, object_name, ExtraArgs={'ACL': 'public-read'})
        return f"{os.getenv('S3_ENDPOINT')}/{bucket_name}/{object_name}"
    except Exception as e:
        print(f"Upload failed: {e}")
        return None
