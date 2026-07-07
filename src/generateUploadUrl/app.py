import json

from common.response import success, error
from common.s3 import generate_presigned_upload_url
from common.dynamodb import put_item
from common.utils import current_timestamp


def lambda_handler(event, context):
    try:
        body = json.loads(event.get("body", "{}"))

        object_key = body.get("objectKey")

        if not object_key:
            return error(400, "objectKey is required.")

        upload_url = generate_presigned_upload_url(object_key)

        inspection_id = object_key.split("/")[1]

        put_item({
            "PK": f"INSPECTION#{inspection_id}",
            "SK": f"IMAGE#{object_key.split('/')[-1]}",
            "inspectionId": inspection_id,
            "imageKey": object_key,
            "uploadedAt": current_timestamp(),
            "entityType": "Image"
        })

        return success(
            200,
            {
                "uploadUrl": upload_url,
                "objectKey": object_key
            }
        )

    except Exception as e:
        return error(500, str(e))