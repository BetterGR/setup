# Staff Microservice Documentation

## Overview
The Staff domain manages all data for faculty members, including their roles (e.g., Lecturer, TA, etc.). It enables and provides the flexibility to update or delete staff information when necessary.
The staff microservice is responsible for managing staff records, including their personal information and roles within the organization. It provides a set of APIs to create, read, update, and delete staff records.

## Data Schema


```json
{
  "staff": {
    "id": "string",
    "firstName": "string",
    "lastName": "string",
    "email": "string",
    "phoneNumber": "string",
    "title": "string",
    "office": "string"
  }
}
```


## API Gateway Endpoints

1. `GET /staff/{id}` – Retrieves details about a specific staff member.
2. `POST /staff `– Creates a new staff member record.
3. `PUT /staff/{id}` – Updates information for a specific staff member.
4. `DELETE /staff/{id}` – Deletes a specific staff member.

## Dependencies

The Staff Microservice is independent on other microservices. It provides a standalone gRPC service for managing student records. However, it may interact with other microservices in the BetterGR system for authentication and authorization purposes.

## Setup & Configuration

For setup, configuration and testing details go to the relevant [README file](https://github.com/BetterGR/staff-microservice/blob/main/README.md).

