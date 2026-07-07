from common.response import success, error
from common.dynamodb import query_by_partition_key


def lambda_handler(event, context):
    try:
        warehouse_id = event["pathParameters"]["warehouseId"]

        inspections = query_by_partition_key(
            f"WAREHOUSE#{warehouse_id}"
        )

        return success(
            200,
            {
                "warehouseId": warehouse_id,
                "inspections": inspections
            }
        )

    except Exception as e:
        return error(500, str(e))