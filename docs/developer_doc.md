# Developer Documentation


This documentation is designed to assist developers in understanding the project's structure, how to set up their development environment and how to contribute effectively. 

It is intended for developers who want to contribute to or extend BetterGR and covers setup, architecture, coding standards and contribution guidelines.


---
## Introduction

BetterGR is a scalable and modular application built using microservice architecture. It leverages Go, TypeScript and GraphQL to provide a robust platform for managing educational workflows. 

The project integrates third-party tools like Keycloak for authentication and gRPC for inter-service communication.

Key technologies used:

- **Go**: Backend microservices and API Gateway.
- **Nuxt with Vue**: Frontend development.
- **GraphQL**: API design for flexible data querying.
- **Keycloak**: Authentication and authorization.




## Getting Started
### Cloning Repositories
To begin working on a specific repository, clone it using the following command:
```bash
git clone https://github.com/BetterGR/<repository-name>.git
```
Replace <repository-name> with the name of the repository you want to work on.

### Setting Up the Development Environment

1. Install Go (version 1.24 or higher).
2. Install Nuxt with Vue for frontend development.
3. Install and set up Docker for containerized services.

### Running the Application Locally
Refer to the specific repository's README file for instructions on running the application locally.


## Architecture

### Project Structure
BetterGR follows a modular structure, with each repository representing a specific domain or functionality. 

The key components include:
- **API Gateway**: Acts as the central entry point for client requests, handling routing, authentication, and communication between the frontend and backend microservices.
- **Microservices**: Each microservice is responsible for a specific domain, such as Students, Courses, Grades, Homework, and Staff.
- **Frontend**: Built using Nuxt.js and Vue.js, the frontend provides a responsive and user-friendly interface for interacting with the platform.
- **Database**: Each microservice has its own dedicated database to ensure data isolation and scalability.

### Key Modules and Components
**1.** **API Gateway**:
   - Handles authentication and authorization using Keycloak
   - Routes requests to the appropriate microservices via gRPC
   - Translates gRPC responses into GraphQL responses for the frontend

**2.** **Microservices**:
   - **Students Microservice**: Manages student-related operations.
   - **Staff Microservice**: Handles staff-related functionalities.
   - **Courses Microservice**: Manages course-related workflows.
   - **Homework Microservice**: Handles assignments ,submissions and announcements.
   - **Grades Microservice**: Manages grading operations.

**3.** **Frontend**:
   - Developed using Nuxt.js, Vue.js and TypeScript
   - Communicates with the API Gateway via GraphQL queries and mutations

**4.** **Databases**:
   - SQL databases are used for storing domain-specific data
   - Each microservice has its own database schema optimized for its functionality

### Configuration
BetterGR uses environment variables to configure the application. These variables are defined in `.env` files and include:
- **Database connection strings**: For connecting to microservice-specific databases.
- **Keycloak settings**: For authentication and authorization.
- **gRPC settings**: For inter-service communication.
- **API Gateway settings**: For routing and GraphQL configuration.

### Environment Variables:
Environment variables are used to manage sensitive information and application settings. 
Examples include:
- API_GATEWAY_PORT: Port for the API Gateway configuration.
- CLIENT_SECRET: Secret key used for authentication purposes.
- KEYCLOAK_URL: URL for the Keycloak authentication server.
- REDIRECT_URI: URI for handling authentication callbacks.
- GRADES_PORT, STUDENTS_PORT, HOMEWORK_PORT, COURSES_PORT, STAFF_PORT: Ports for microservice communication.

## Database Setup
Each microservice in BetterGR uses a dedicated PostgreSQL database to ensure data isolation and scalability. 

The setup process includes:

### **Database Initialization**:
   - Use the provided SQL scripts to create the necessary tables and schemas for each microservice.
   - Example command to execute a script:
     ```bash
     psql -U <username> -d <database_name> -f <script_name>.sql
     ```
     
For further information on setting the database, go to [Database Readme](dbDesign.md).



## Third-Party Integrations
BetterGR integrates with several third-party tools to enhance functionality:
- **Keycloak**: Provides authentication and authorization services, including role-based access control.
- **gRPC**: Enables efficient and reliable communication between microservices.
- **Docker**: Used for containerizing services to ensure consistent deployment across environments.


## API Documentation

For detailed API documentation, including endpoints, request/response formats and authentication mechanisms, go to [API Gateway Documentation](api_docs.md).


## Microservices

### Overview of Microservices Architecture
BetterGR employs a microservices architecture to ensure modularity, scalability, and maintainability. Each microservice is designed to handle a specific domain, allowing independent development, deployment and scaling. Communication between microservices is facilitated using gRPC, ensuring efficient and reliable inter-service communication. The architecture also integrates with the API-Gateway, which acts as the central entry point for client requests and handles routing, authentication, and GraphQL query processing.

Key features of the microservices architecture:
- **Domain-specific services**: Each microservice is responsible for a specific domain, such as Students, Courses, Grades, Homework, and Staff.
- **Independent databases**: Each microservice has its own PostgreSQL database to ensure data isolation and scalability.
- **Inter-service communication**: gRPC is used for efficient communication between microservices.
- **API Gateway**: Provides a unified interface for frontend communication and handles authentication via Keycloak.



### Description of Each Microservice

1. **Students Microservice**:
   - Manages student-related operations, including registration, profile management, and enrollment in courses
   - Provides APIs for retrieving student information and managing student-course relationships

2. **Staff Microservice**:
   - Handles staff related functionalities, such as managing instructors and teaching assistants
   - Provides APIs for assigning staff to courses and retrieving staff details

3. **Courses Microservice**:
   - Manages academic courses and their semester-specific instances
   - Tracks enrolled students, assigned staff, course materials, and announcements
   - Provides APIs for creating, updating, and deleting courses, as well as managing course-related data

4. **Homework Microservice**:
   - Handles assignments and submissions for courses
   - Provides APIs for creating, updating, and retrieving homework assignments and submissions

5. **Grades Microservice**:
   - Manages grading workflows, including assignment grading and final grade calculations
   - Provides APIs for retrieving and updating grades for students

Each microservice is designed to operate independently while collaborating with other services to provide a seamless user experience. For detailed documentation for each microservice, refer to the respective documentations 
in [Microservices Documentations](microservices_docs).

## Contribution Guidelines

### Coding Standards
BetterGR follows open-source coding standards to ensure consistency and maintainability across the project. Contributors are encouraged to adhere to best practices for Go, TypeScript, and Vue.js development. Use linters and formatters to maintain code quality and readability.


### Branching and Pull Request Process
BetterGR uses a forking-based workflow for contributions. Follow these steps to contribute:

1. **Fork the Repository**:
   - Navigate to the original repository in the BetterGR organization and fork it to your GitHub account.

2. **Create a Feature Branch**:
   - Clone your forked repository locally:
     ```bash
     git clone https://github.com/<your-username>/<repository-name>.git
     ```
   - Create a new branch for your feature or bug fix:
     ```bash
     git checkout -b feature/<feature-name>
     ```

3. **Develop and Commit Changes**:
   - Make your changes in the feature branch.
   - Commit your changes with clear and descriptive messages:
     ```bash
     git commit -m "Add feature: <description>"
     ```

4. **Push Changes to Your Fork**:
   - Push your feature branch to your forked repository:
     ```bash
     git push origin feature/<feature-name>
     ```

5. **Submit a Pull Request**:
   - Navigate to the original repository in the BetterGR organization.
   - Open a pull request from your feature branch to the `main` branch of the original repository.
   - Provide a detailed description of your changes in the pull request.

6. **Review and Approval**:
   - Pull requests must be reviewed and approved by maintainers before merging.
   - Address any requested changes and update your pull request as needed.

7. **Merge**:
   - Once approved, the pull request will be merged into the `main` branch by a maintainer.


### Issue Tracking
All work and processes in BetterGR must be documented in the **Backlog Repository** using GitHub Issues. For every assignment or task, a corresponding issue must be created. The issue should include:

- **Title**: A clear and concise description of the task.
- **Description**: Detailed information about the task, including objectives and requirements.
- **Labels**: Tags to categorize the issue (e.g., `bug`, `backend`, `epic`).
- **Assignees**: The contributors responsible for completing the task.
- **Milestones**: The target deadline or sprint for the task.

Contributors should update the issue with progress, discussions, and any relevant links to pull requests or commits. This ensures transparency and traceability throughout the development process.

## **Deployment**

### Deployment Process

**1. Containerization**:

   - All microservices are containerized using Docker.
   - Each microservice has its own `Dockerfile` specifying the build instructions. 
    
        Example `Dockerfile` for a microservice:
       ```dockerfile
       FROM golang:1.24-alpine
       WORKDIR /app
       COPY . .
       RUN go build -o main .
       CMD ["./main"]
       ```
**2. Environment Configuration**
   - Each microservice requires specific environment variables for configuration.
   - Environment variables are defined in `.env` files for each microservice.


**3. Deployment Tools**

   - **Docker Compose**: Used for local development and testing.


**4. Production Deployment**

   - **Push Docker Images**:  
      Push the Docker images to a container registry (e.g., Docker Hub).


### CI Pipelines

BetterGR uses GitHub Actions for CI to automate testing, building and deployment.

### Example GitHub Actions Workflow

```yaml
name: CI

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: Check out code
        uses: actions/checkout@v4

      - name: Set up Go
        uses: actions/setup-go@v5
        with:
          go-version: '1.23.3'
          cache: true

      - name: Download dependencies
        run: go mod download

      - name: Run tests
        run: go test -v ./...

      - name: Run go vet
        run: go vet ./...

      - name: Run golangci-lint
        uses: golangci/golangci-lint-action@v3
        with:
          version: latest
          args: --config=.golangci.yaml

  build:
    runs-on: ubuntu-latest
    needs: test

    steps:
      - name: Check out code
        uses: actions/checkout@v4

      - name: Set up Go
        uses: actions/setup-go@v5
        with:
          go-version: '1.23.3'
          cache: true

      - name: Build application
        run: go build -v ./...

      - name: Build Docker image
        run: docker build -t grades-microservice:latest . 
```

## **Additional Resources**



- **Official Documentation**:
  - [API Gateway Documentation](api_docs.md)
  - [Microservices Documentation](microservices_docs)
  - [User Documentation](user_doc.md)

- **Development Tools**:
  - [Go Documentation](https://golang.org/doc/)
  - [Nuxt.js Documentation](https://nuxtjs.org/docs/)
  - [Vue.js Documentation](https://vuejs.org/v2/guide/)
  - [GraphQL Documentation](https://graphql.org/learn/)
  - [Keycloak Documentation](https://www.keycloak.org/documentation)

- **Deployment Tools**:
  - [Docker Documentation](https://docs.docker.com/)

- **CI Tools**:
  - [GitHub Actions Documentation](https://docs.github.com/en/actions)

- **Database Resources**:
  - [PostgreSQL Documentation](https://www.postgresql.org/docs/)

- **Community and Support**:
  - [BetterGR GitHub Organization](https://github.com/BetterGR)
  - [Contact Support](link-to-support-page)

