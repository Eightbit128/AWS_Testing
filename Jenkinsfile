pipeline {
    agent any
    environment {
        // Set IMAGE_TAG based on BUILD_NUMBER
        IMAGE_TAG = "${BUILD_NUMBER}"
        DOCKERHUB_CREDENTIALS = credentials('Docker_hub')
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }


        stage('Copy File') {
            steps {
                sh 'sudo -u ec2-user cp $WORKSPACE/docker-compose.yml /home/ec2-user/app'
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
                    // Define the path to your Docker Compose file
                    def composeFilePath = "$WORKSPACE/docker-compose.yml"

                    // Read the Docker Compose file into a string
                    def composeFileContents = readFile(file: composeFilePath).trim()

                    // Replace the existing image tag with IMAGE_TAG
                    composeFileContents = composeFileContents.replaceFirst(/image: eightbit128\/reply-app:\d+/, "image: eightbit128/reply-app:${IMAGE_TAG}")

                    // Write the updated Docker Compose file back
                    writeFile(file: composeFilePath, text: composeFileContents)
                }
            }
        }
    }
}
