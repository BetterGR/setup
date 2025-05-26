# BetterGR Microservices Setup

##1. Go Version Consistency
  for each ms in go.mod:
  '''bash
  go 1.24.0
'''
  in Dockerfile:
  '''bash
  FROM golang:1.24-alpine AS base
'''
##2. Environment Variable Loading in server.go:
Update all server.go files in the microservices to safely load the .env file without failing if it’s missing.
Replace this code:
'''bash
err := godotenv.Load()
if err != nil {
	klog.Fatalf("Error loading .env file")
}
'''
with this code:
'''bash
if err := godotenv.Load(); err != nil {
	klog.Warning("Warning: No .env file loaded, proceeding with environment variables only")
}
'''


This repository contains the Docker Compose setup and microservices for the BetterGR system, including services for:

- Students
- Staff
- Courses
- Grades
- Homework
- Keycloak (Auth)
- PostgreSQL (Database)

---

## 🐳 Docker Compose Setup

Run the following command from the `main-root/setup` directory to build and start all services:

```bash
docker compose up --build
