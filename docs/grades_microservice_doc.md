# Grades Microservice Documentation


## Overview


The grades domain manages all students' grades in each course. Course staff can edit the students' grades, and each student can view their own grades.

## Data Schema

- #### Schema for a single exam grade
```
{
    "examGrade": {
        "course": "string",
        "exam_type": "string",
        "grade": "string"
    }
}
```

- #### Schema for a single homework grade
```
{
    "homeworkGrade": {
        "course": "string",
        "homework_number": "string",
        "grade": "string"
    }
}
```
- #### Schema for grades for a student in a single course
```
{
    "studentCourseGrades": {
        "student_id": "string",
        "course_id": "string",
        "exams": "examGrade",
        "homework": "homeworkGrade"
    }
}
```
- #### Schema for all grades of a student
```
{
    "studentGrades": {
        "student_id": "string",
        "courses": "studentCourseGrades"
    }
}
```
## API Gateway Endpoints

1. `GET/courses/{course_id}/grades` – Lists all grades of all the students of a specific course.
2. `GET/students/{student_id}/courses/{course_id}/grades` – Lists the grades for a specific student of a specific course.
3. `POST/students/{student_id}/courses/{course_id}/homework/{hw_number}/grades/{grade}` – Adds a new homework grade for a specific student in a specific course.
4. `PUT/grades/{grade}/students/{student_id}/courses/{course_id}/homework/{homework_number}` –Updates a grade for a specific student in a specific course.
5. `POST/students/{student_id}/courses/{course_id}/{exam_type}/grades/{grade}` – Adds an exam grade for a specific student in a specific course.
6. `PUT/grades/{grade}/students/{student_id}/courses/{course_id}/{exam_type}` – Updates an exam grade for a specific student in a specific course.
7. `DELETE/grades/students/{student_id}/courses/{course_id}/homework/{homework_number}` – Deletes a homework grade for a specific student in a specific course.
8. `DELETE/grades/students/{student_id}/courses/{course_id}/{exam_type}` – Deletes an exam grade for this student in this course.

## Dependencies

The Grades Microservice depends on the following microservices:

- **Courses Microservice**: to retrieve course-related information.
- **Homework Microservice**: to manage homework-related data and grades.
- **Staff Microservice**: to verify course staff permissions for grade modifications.
- **Students Microservice**: to fetch student-related information and validate student identities.

## Setup & Configuration

For setup, configuration and testing details go to the relevant [README file](https://github.com/BetterGR/grades-microservice/blob/main/README.md).

