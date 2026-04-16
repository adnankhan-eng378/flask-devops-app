pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "adnankhan48/flask-devops-app"
        DOCKER_TAG = "latest"
        GIT_REPO = "https://github.com/adnankhan-eng378/flask-devops-app.git"
        GIT_BRANCH = "main"

        KUBECONFIG = "/var/lib/jenkins/.kube/config"
    }

    stages {

        stage('Checkout Code') {
            steps {
                git branch: "${GIT_BRANCH}", url: "${GIT_REPO}"
            }
        }

        stage('Test Kubernetes') {
            steps {
                sh 'kubectl get nodes'
            }
        }

        stage('Login to Docker Hub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-credentials',   // ✅ same as working one
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh '''
                    echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
                    '''
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                docker build -t $DOCKER_IMAGE:$DOCKER_TAG .
                '''
            }
        }

        stage('Push Docker Image') {
            steps {
                sh '''
                docker push $DOCKER_IMAGE:$DOCKER_TAG
                '''
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh '''
                kubectl apply -f deployment.yaml
                kubectl apply -f service.yaml
                '''
            }
        }

        stage('Verify Deployment') {
            steps {
                sh '''
                kubectl get pods
                kubectl get svc
                '''
            }
        }

        stage('Cleanup') {
            steps {
                sh '''
                docker logout
                docker system prune -f
                '''
            }
        }
    }
//dddddhhh
    post {
        success {
            echo "✅ Flask App Build & Deployment Successful!"
        }
        failure {
            echo "❌ Pipeline Failed - check logs"
        }
    }
}