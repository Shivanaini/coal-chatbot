# Coal Chatbot

AI-powered Telangana Coal Chatbot with multi-agent architecture.

## Features
- Coal knowledge agent
- Retriever agent
- Summarizer agent
- Flask backend
- HTML/CSS/JS frontend
- Dockerized deployment
- GitHub Actions CI/CD
- AWS ECS Fargate deployment

## Architecture

User → Frontend → Flask API → Router Agent  
Router → Coal Agent / Retriever Agent / Summarizer Agent

Deployment:  
GitHub → Actions → Docker → ECR → ECS Fargate

## Run locally

Install dependencies:

```bash
pip install -r backend/requirements.txt