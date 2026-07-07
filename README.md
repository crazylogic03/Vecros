# 🚁 Drone Inspection Backend

A serverless backend application built using **AWS Lambda**, **Amazon API Gateway**, **Amazon DynamoDB**, **Amazon S3**, and **AWS SAM** for managing drone inspections and inspection image uploads.

This project was developed as part of a backend assignment to demonstrate AWS fundamentals, serverless architecture, and DynamoDB association modeling.

---

# 📌 Features

- Create a new drone inspection
- List inspections by warehouse
- List inspections by drone
- Generate secure Amazon S3 pre-signed upload URLs
- List inspection image metadata
- Serverless architecture using AWS Lambda
- RESTful APIs with API Gateway
- DynamoDB single-table design
- Reusable helper modules
- Proper HTTP status codes and error handling

---

# 🛠 Tech Stack

- Python 3.11
- AWS Lambda
- Amazon API Gateway
- Amazon DynamoDB
- Amazon S3
- AWS SAM (Serverless Application Model)
- Boto3

---

# 🏗 Architecture

```
                Client
                   │
                   ▼
            Amazon API Gateway
                   │
        ┌──────────┴──────────┐
        ▼                     ▼
      AWS Lambda Functions
        │
        ├──────────────┐
        ▼              ▼
 Amazon DynamoDB    Amazon S3
```

---

# 📂 Project Structure

```text
drone-inspection-backend/
│
├── src/
│   ├── common/
│   │   ├── dynamodb.py
│   │   ├── response.py
│   │   ├── s3.py
│   │   └── utils.py
│   │
│   ├── createInspection/
│   │   └── app.py
│   │
│   ├── listWarehouseInspections/
│   │   └── app.py
│   │
│   ├── listDroneInspections/
│   │   └── app.py
│   │
│   ├── generateUploadUrl/
│   │   └── app.py
│   │
│   └── listInspectionImages/
│       └── app.py
│
├── events/
├── template.yaml
├── requirements.txt
├── samconfig.toml
└── README.md
```

---

# 🗄 DynamoDB Data Model

The application uses a **single-table design**.

## Warehouse

```
PK = WAREHOUSE#WH001
SK = METADATA
```

---

## Inspection (Warehouse View)

```
PK = WAREHOUSE#WH001
SK = INSPECTION#INS001
```

---

## Inspection (Drone View)

```
PK = DRONE#DR001
SK = INSPECTION#INS001
```

---

## Inspection Images

```
PK = INSPECTION#INS001
SK = IMAGE#image1.jpg
```

---

# 📌 DynamoDB Access Patterns

| Access Pattern | Partition Key |
|---------------|---------------|
| Create Inspection | WAREHOUSE#ID & DRONE#ID |
| List Warehouse Inspections | WAREHOUSE#ID |
| List Drone Inspections | DRONE#ID |
| List Inspection Images | INSPECTION#ID |

The inspection record is intentionally duplicated under both Warehouse and Drone partition keys to support efficient querying without table scans.

---

# 🚀 API Endpoints

## 1. Create Inspection

### Request

```
POST /inspections
```

Body

```json
{
  "warehouseId": "WH001",
  "droneId": "DR001",
  "status": "Pending"
}
```

Response

```json
{
  "inspectionId": "INS_4027bb8a",
  "message": "Inspection created successfully."
}
```

---

## 2. List Warehouse Inspections

```
GET /warehouses/{warehouseId}/inspections
```

Example

```
GET /warehouses/WH001/inspections
```

---

## 3. List Drone Inspections

```
GET /drones/{droneId}/inspections
```

Example

```
GET /drones/DR001/inspections
```

---

## 4. Generate Upload URL

```
POST /upload-url
```

Body

```json
{
    "objectKey":"inspections/INS001/image1.jpg"
}
```

Response

```json
{
    "uploadUrl":"https://..."
}
```

---

## 5. List Inspection Images

```
GET /inspections/{inspectionId}/images
```

Example

```
GET /inspections/INS001/images
```

---

# ⚙ Environment Variables

| Variable | Description |
|-----------|-------------|
| TABLE_NAME | DynamoDB table |
| BUCKET_NAME | S3 Bucket |

---

# ▶ Running Locally

Build

```bash
sam build
```

Deploy

```bash
sam deploy --guided
```

Deploy again

```bash
sam deploy
```

View logs

```bash
sam logs -n CreateInspectionFunction --tail
```

---

# 🧪 Testing

### Create Inspection

```
POST
```

```
/inspections
```

---

### List Warehouse Inspections

```
GET
```

```
/warehouses/{warehouseId}/inspections
```

---

### List Drone Inspections

```
GET
```

```
/drones/{droneId}/inspections
```

---

### Generate Upload URL

```
POST
```

```
/upload-url
```

---

### List Inspection Images

```
GET
```

```
/inspections/{inspectionId}/images
```

---

# 🔒 Security

- IAM Roles used instead of AWS credentials
- S3 uploads handled using pre-signed URLs
- Lambda never directly receives image files
- Least-privilege IAM policies through AWS SAM

---

# 💡 Design Decisions

- Serverless architecture for scalability.
- Single-table DynamoDB design to optimize read performance.
- Inspection records stored under both Warehouse and Drone partition keys to support multiple query patterns efficiently.
- Shared utility modules to avoid code duplication.
- Reusable response helpers for consistent API responses.

---

# 🔮 Future Improvements

- Store uploaded image metadata in DynamoDB.
- Validate Warehouse and Drone existence before creating inspections.
- Authentication and authorization.
- Pagination for listing APIs.
- Unit and integration tests.
- CloudWatch monitoring and structured logging.

---

# 👨‍💻 Author

**Sai Thrishul**

Backend Assignment – Drone Inspection (AWS + Python)