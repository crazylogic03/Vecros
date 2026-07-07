from common.response import success, error
from common.dynamodb import query_by_partition_key


def lambda_handler(event, context):
    try:
        drone_id = event["pathParameters"]["droneId"]

        inspections = query_by_partition_key(
            f"DRONE#{drone_id}"
        )

        return success(
            200,
            {
                "droneId": drone_id,
                "inspections": inspections
            }
        )

    except Exception as e:
        return error(500, str(e))