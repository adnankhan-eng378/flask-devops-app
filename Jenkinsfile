pipeline {
    agent any

    stages {

        stage('Clone') {
            steps {
                git 'https://github.com/adnankhan-eng378/flask-devops-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t adnankhan48/flask-devops-app:latest .'
            }
        }

        stage('Push Image') {
            steps {
                sh 'docker login -u adnankhan48 -p YOUR_DOCKERHUB_PASSWORD'
                sh 'docker push adnankhan48/flask-devops-app:latest'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f deployment.yaml'
                sh 'kubectl apply -f service.yaml'
            }
        }
    }
}