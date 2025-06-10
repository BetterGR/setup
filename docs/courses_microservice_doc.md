# Courses Microservice Documentation
## Overview
The Courses domain is responsible for managing all academic courses and their semester-specific instances. It tracks information about the courses, their staff, enrolled students, and course-related announcements.

The Courses microservice is designed to handle the following functionalities:
- Manage academic courses and their instances per semester
- Track staff, students, and course-related announcements
- Manage course materials and homework assignments

## Data Schema

- ### Course Schema
```json
{
  "course": {
    "id": "string",
    "name": "string",
    "semester": "string",
    "description": "string"
  }
}
```

- ### Announcement Schema
```json
{
  "announcement": {
    "id": "string",
    "title": "string",
    "content": "string"
  }
}
```



## API Gateway Endpoints

1. `GET/courses/{id} `– Retrieves details about a specific course.
2. `POST/courses `– Creates a new course.
3. `PUT/courses` – Updates details of a specific course.
4. `DELETE/courses/{id}` – Deletes a specific course.
5. `POST/courses/{id}/students/{id}` – adds a given student to a specific course.
6. `DELETE/courses/{id}/students/{id}`–  Removes a specific student from a specific course.
7. `POST/courses/{id}/staff/{id}` – adds a given staff member to a specific course.
8. `DELETE/courses/{id}/staff/{id}` – Removes a specific staff member from a specific course.
9. `GET/courses/{id}/students `– Fetches a list of all students enrolled in a specific course.
10. `GET/courses/{id}/staff `– Fetches a list of staff (lecturers or TAs) assigned to a  specific course.
11. `GET/courses/students/{id}` – Fetches a list of courses a specific student is enrolled in.
12. `GET/courses/staff/{id}` – Fetches a list of courses a specific staff member is assigned to.
13. `POST/courses/{id}/announcements` – Adds a given announcement to a specific course.
14. `GET/courses/{id}` – Retrieves all announcements in a specific course.
15. `DELETE/courses/{id}/announcements/{id} `– Removes an announcement from a specific course.

## Dependencies

The Courses Microservice depends on the following microservices:
- **Students Microservice**: to retrieve student-related information.
- **Staff Microservice**: to retrieve staff-related information.
- **Grades Microservice**: to retrieve grades-related information.
- **Homework Microservice**: to retrieve homework-related information.

## Setup & Configuration

For setup, configuration and testing details go to the relevant [README file](https://github.com/BetterGR/courses-microservice/blob/main/README.md).




