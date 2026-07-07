import json

from common.response import success, error
from common.s3 import generate_presigned_upload_url


def lambda_handler(event, context):
    try:
        body = json.loads(event.get("body", "{}"))

        object_key = body.get("objectKey")

        if not object_key:
            return error(400, "objectKey is required.")

        upload_url = generate_presigned_upload_url(object_key)

        return success(
            200,
            {
                "uploadUrl": upload_url,
                "objectKey": object_key
            }
        )

    except Exception as e:
        return error(500, str(e))