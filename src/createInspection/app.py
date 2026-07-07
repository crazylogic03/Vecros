import json

from common.response import success, error
from common.utils import generate_id, current_timestamp
from common.dynamodb import put_item


def lambda_handler(event, context):
    try:
        body = json.loads(event.get("body", "{}"))

        warehouse_id = body.get("warehouseId")
        drone_id = body.get("droneId")
        status = body.get("status", "Pending")

        if not warehouse_id or not drone_id:
            return error(
                400,
                "warehouseId and droneId are required."
            )

        inspection_id = generate_id("INS")
        created_at = current_timestamp()

        warehouse_record = {
            "PK": f"WAREHOUSE#{warehouse_id}",
            "SK": f"INSPECTION#{inspection_id}",
            "inspectionId": inspection_id,
            "warehouseId": warehouse_id,
            "droneId": drone_id,
            "status": status,
            "createdAt": created_at,
            "entityType": "Inspection"
        }

        drone_record = {
            "PK": f"DRONE#{drone_id}",
            "SK": f"INSPECTION#{inspection_id}",
            "inspectionId": inspection_id,
            "warehouseId": warehouse_id,
            "droneId": drone_id,
            "status": status,
            "createdAt": created_at,
            "entityType": "Inspection"
        }

        put_item(warehouse_record)
        put_item(drone_record)

        return success(
            201,
            {
                "message": "Inspection created successfully.",
                "inspectionId": inspection_id
            }
        )

    except Exception as e:
        return error(500, str(e))