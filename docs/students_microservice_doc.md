# Students Microservice Documentation
## Overview
The Students domain manages all information related to students, including their identity, and personal details. It ensures accurate and efficient handling of student records and supports core operations like  modifications to student data.
The Students microservice is responsible for managing student-related operations within the BetterGR system. It provides a gRPC service that allows for the creation, retrieval, updating, and deletion of student records. The service is implemented in Go and uses Protobuf to define message types and service methods.

## Data Schema

### Schema for a single student
```json
{
  "student": {
    "id": "string",
    "firstName": "string",
    "lastName": "string",
    "email": "string",
    "phoneNumber": "string"
  }
}
```


## API Gateway Endpoints


1. `GET /students/{id}` – Retrieves information about a specific student.
2. `POST /students` – Creates a new student record.
3. `PUT /students/{id}` – Updates information for a specific student.
4. `DELETE /students/{id}` – Deletes a specific student.


## Dependencies

The Students Microservice is independent on other services. It provides a standalone gRPC service for managing student records. However, it may interact with other microservices in the BetterGR system for authentication and authorization purposes.

## Setup & Configuration

For setup, configuration and testing details go to the relevant [README file](https://github.com/BetterGR/students-microservice/blob/main/README.md).
