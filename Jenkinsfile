pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('Docker_hub')
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build and Push Docker Image') {
            steps {
                script {
                    // Use the DockerHub credentials
                    withCredentials([usernamePassword(credentialsId: DOCKERHUB_CREDENTIALS, usernameVariable: 'DOCKERHUB_USERNAME', passwordVariable: 'DOCKERHUB_PASSWORD')]) {
                        // Authenticate with DockerHub
                        sh 'docker login -u $DOCKERHUB_USERNAME -p $DOCKERHUB_PASSWORD'

                        // Build the Docker image using the Dockerfile
                        sh 'docker build -t Eightbit128/reply-app:latest .'

                        // Push the Docker image to DockerHub
                        sh 'docker push Eightbit128/reply-app:latest'
                    }
                }
            }
        }
    }
}
