import os
import boto3

BUCKET_NAME = os.environ["BUCKET_NAME"]

s3_client = boto3.client("s3")

#pre signed URL Generate
def generate_presigned_upload_url(object_key: str,expires_in: int = 3600) -> str:
    return s3_client.generate_presigned_url(
        ClientMethod="put_object",
        Params={
            "Bucket": BUCKET_NAME,
            "Key": object_key,
        },
        ExpiresIn=expires_in,
    )