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
                    withCredentials([usernamePassword(credentialsId: 'Docker_hub', usernameVariable: 'DOCKER_HUB_USERNAME', passwordVariable: 'DOCKER_HUB_PASSWORD')]) {
                        // Authenticate with DockerHub
                        sh "docker login -u ${env.DOCKER_HUB_USERNAME} -p ${env.DOCKER_HUB_PASSWORD}"

                        // Build the Docker image using the Dockerfile
                        sh 'docker build -t eightbit128/reply-app:latest .'

                        // Push the Docker image to DockerHub
                        sh 'docker push eightbit128/reply-app:latest'
                    }
                }
            }
        }
    }
}
