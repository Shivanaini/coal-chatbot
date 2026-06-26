#!/bin/bash
set -e

echo "Deploying network stack..."
aws cloudformation deploy \
  --template-file infra/cloudformation/network.yaml \
  --stack-name coal-chatbot-network

echo "Deploying security stack..."
aws cloudformation deploy \
  --template-file infra/cloudformation/security.yaml \
  --stack-name coal-chatbot-security

echo "Deploying ECR stack..."
aws cloudformation deploy \
  --template-file infra/cloudformation/ecr.yaml \
  --stack-name coal-chatbot-ecr

echo "Deploying IAM stack..."
aws cloudformation deploy \
  --template-file infra/cloudformation/iam.yaml \
  --stack-name coal-chatbot-iam