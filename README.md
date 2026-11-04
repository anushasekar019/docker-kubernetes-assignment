# DevOps Student Portal

## Project Description
A simple Flask application containerized using
Docker and deployed using Kubernetes.

## Technologies Used
- Python Flask
- Docker
- Kubernetes
- Minikube
- kubectl

## Docker Build
docker build -t devops-student-portal:v1 .

## Run Docker Container
docker run -d -p 5000:5000 \
--name student-portal devops-student-portal:v1

## Kubernetes Deployment
minikube image load devops-student-portal:v1

kubectl apply -f kubernetes/deployment.yaml

kubectl apply -f kubernetes/service.yaml

## Access Application
minikube service student-portal-service --url

## Verify Kubernetes
kubectl get deployments
kubectl get pods
kubectl get services
