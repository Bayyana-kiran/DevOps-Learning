# Deploying a Node.js + MongoDB App with Docker Compose and Uploading to Docker Hub

This project showcases a simple yet complete full-stack setup using Node.js, MongoDB, and Docker. The application is designed to manage a user profile, allowing you to view and update user data through a clean HTML interface. On the backend, an Express server handles API requests and connects to a MongoDB database for persistent storage. The entire stack is containerized using Docker, with services defined in a `docker-compose.yml` file to streamline orchestration. Mongo Express is also included for easy database management through a web interface. In addition to running everything locally, this setup demonstrates how to build a Docker image of the Node.js application and push it to Docker Hub for distribution or deployment. Whether you're experimenting locally or preparing for production, this project provides a clear example of how to bring together key components in a modern, containerized development environment.




```mermaid

sequenceDiagram
    participant Dev as Developer
    participant Dockerfile
    participant DockerHub
    participant Compose as docker-compose.yml
    participant App as Node.js App (Express)
    participant Mongo as MongoDB
    participant ME as Mongo Express
    participant Browser

    Dev->>Dockerfile: Write Dockerfile (Node + App)
    Dev->>Compose: Define services (Mongo, Mongo Express, App)
    Dev->>Dev: Create image with `docker build`
    Dev->>DockerHub: Push image using `docker tag` & `docker push`

    Dev->>Compose: Run `docker-compose up`
    Compose->>Mongo: Start MongoDB container
    Compose->>ME: Start Mongo Express container
    Compose->>App: Start Node.js App container

    Browser->>App: GET / (index.html)
    App->>Mongo: GET profile from MongoDB
    Mongo-->>App: Return profile data
    App-->>Browser: Send profile HTML + data

    Browser->>App: POST /update-profile (updated user data)
    App->>Mongo: Update user in MongoDB
    Mongo-->>App: Acknowledge update
    App-->>Browser: Respond with updated profile

    Browser->>ME: Access Mongo Express (localhost:3000)
    ME->>Mongo: GUI-based MongoDB interaction

```

## 🛠️ Prerequisites

Before you begin, ensure you have the following tools installed on your local machine to build, run, and manage the Dockerized application:

<p align="left">
  <img src="https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=nodedotjs&logoColor=white" alt="Node.js"/>
  <img src="https://img.shields.io/badge/npm-CB3837?style=for-the-badge&logo=npm&logoColor=white" alt="npm"/>
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker"/>
  <img src="https://img.shields.io/badge/Docker Compose-3854FF?style=for-the-badge&logo=docker&logoColor=white" alt="Docker Compose"/>
  <img src="https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white" alt="MongoDB"/>
  <img src="https://img.shields.io/badge/YAML-FFA500?style=for-the-badge&logo=yaml&logoColor=black" alt="YAML"/>
</p>

### Install links

- [Install Node.js and npm](https://nodejs.org/en/download/)
- [Install Docker](https://docs.docker.com/get-docker/)
- [Install Docker Compose](https://docs.docker.com/compose/install/)
- [Install MongoDB (optional, for local debugging)](https://www.mongodb.com/try/download/community)

### Step 1: Build and Start the Containers
```bash
docker-compose up --build
```

Check in Localhost:3000 through postman

![Screenshot 2025-04-15 122012](https://github.com/user-attachments/assets/fb8b3619-ee15-4ecf-a9e6-f4bd926bd403)


### Step 2: login 

```bash
docker login
```



### Step 3: Build the Docker image
```bash
docker build -t yourdockerhubusername/node-profile-app .
```
![Screenshot 2025-04-15 124844](https://github.com/user-attachments/assets/0380c47d-8b07-4496-9a04-de82ca1f4f71)

![Screenshot 2025-04-15 130653](https://github.com/user-attachments/assets/815f9883-7b19-4f1c-beda-49c7ab7e6d17)



### Step 4: Push to Docker Hub
```bash
docker push yourdockerhubusername/node-profile-app
```
![Screenshot 2025-04-15 131953](https://github.com/user-attachments/assets/98dd5721-a841-4f96-b551-c3873bc6d29c)

![Screenshot 2025-04-15 132032](https://github.com/user-attachments/assets/fca73df2-cd90-4470-8395-ed22a7755147)


### Step 5: Stop and Clean Up
```bash
docker-compose down
```



