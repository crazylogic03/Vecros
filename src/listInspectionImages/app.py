from common.response import success, error
from common.dynamodb import query_by_partition_key


def lambda_handler(event, context):
    try:
        inspection_id = event["pathParameters"]["inspectionId"]

        images = query_by_partition_key(
            f"INSPECTION#{inspection_id}"
        )

        return success(
            200,
            {
                "inspectionId": inspection_id,
                "images": images
            }
        )

    except Exception as e:
        return error(500, str(e))