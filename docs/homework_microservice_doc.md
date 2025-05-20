# Grades Microservice Documentation
## Overview


The Homework domain manages all information related to assignments for each course, including workflows for completing homework, submission tracking, and grading. Staff can post workflows to guide students through the homework process, enhancing the user experience (UX) for both students and staff.

## Data Schema

Will add soon...

## API Gateway Endpoints


NOTE: might change...
1. `GET/homework/{id} `– Retrieves information of a specific homework.
2. `POST/homework`– Creates a new homework assignment.
3. `PUT/courses/{id}/homework/{id}`– Updates a homework assignment.
4. `DELETE/homework/{id}` – Deletes a homework.

Dependencies

The Homework Microservice depends on the following microservices(may change):
- **Courses Microservice**: to retrieve course-related information.


## Setup & Configuration

For setup, configuration and testing details go to the relevant [README file](https://github.com/BetterGR/homework-microservice/blob/main/README.md).
