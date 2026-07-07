# 🚁 Drone Inspection Backend

A serverless backend application built using **AWS Lambda**, **Amazon API Gateway**, **Amazon DynamoDB**, **Amazon S3**, and **AWS SAM** for managing drone inspections and inspection images.

---

## 📌 Overview

This project provides REST APIs to:

- Create drone inspections
- Retrieve inspections by warehouse
- Retrieve inspections by drone
- Generate secure S3 pre-signed upload URLs
- Retrieve inspection image metadata

The application follows a **serverless architecture**, allowing automatic scaling with minimal infrastructure management.

---

## 🛠 Tech Stack

- Python 3.11
- AWS Lambda
- Amazon API Gateway
- Amazon DynamoDB
- Amazon S3
- AWS SAM (Serverless Application Model)
- Boto3