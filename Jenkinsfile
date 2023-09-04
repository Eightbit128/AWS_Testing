pipeline {
    agent any
    environment {
        IMAGE_TAG = "${BUILD_NUMBER}"
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
                    withCredentials([usernamePassword(credentialsId: 'Docker_hub', usernameVariable: 'DOCKER_HUB_USERNAME', passwordVariable: 'DOCKER_HUB_PASSWORD')]) {
                        sh "docker login -u ${env.DOCKER_HUB_USERNAME} -p ${env.DOCKER_HUB_PASSWORD}"

                        sh 'docker build -t eightbit128/reply-app:${BUILD_NUMBER} .'

                        sh 'docker push eightbit128/reply-app:${BUILD_NUMBER}'
                    }
                }
            }
        }

        stage('Update Docker Compose') {
            steps {
                script {
                    def composeFilePath = "$WORKSPACE/docker-compose.yml"

                    def composeFileContents = readFile(file: composeFilePath).trim()

                    composeFileContents = composeFileContents.replace('image: eightbit128/reply-app:latest', "image: eightbit128/reply-app:${IMAGE_TAG}")

                    writeFile(file: composeFilePath, text: composeFileContents)
                }
            }
        }

        stage('Copy File') {
            steps {
                sh 'sudo -u ec2-user cp $WORKSPACE/docker-compose.yml /home/ec2-user/app'
            }
        }
    }
}
