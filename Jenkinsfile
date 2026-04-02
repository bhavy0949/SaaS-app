pipeline {
    agent any

    environment {
        // ID of the credentials stored in Jenkins for your Docker Hub username/password
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-credentials-id')
        // Replace this with your actual Docker Hub username and repository name
        IMAGE_NAME = 'yourdockerhubusername/saas-app'
        IMAGE_TAG = "${env.BUILD_NUMBER}"
    }

    triggers {
        // Triggers the build when code is pushed to Github (Requires a GitHub Webhook configured)
        githubPush()
    }

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build both a specific build number tag and the 'latest' tag
                    sh "docker build -t ${IMAGE_NAME}:${IMAGE_TAG} -t ${IMAGE_NAME}:latest ."
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    // Login to Docker Hub
                    sh "echo \$DOCKERHUB_CREDENTIALS_PSW | docker login -u \$DOCKERHUB_CREDENTIALS_USR --password-stdin"
                    
                    // Push the numbered tag
                    sh "docker push ${IMAGE_NAME}:${IMAGE_TAG}"
                    
                    // Push the latest tag
                    sh "docker push ${IMAGE_NAME}:latest"
                    
                    // Always logout
                    sh "docker logout"
                }
            }
        }
    }

    post {
        always {
            // Clean up old images locally to free up Jenkins disk space
            sh "docker rmi ${IMAGE_NAME}:${IMAGE_TAG} || true"
            sh "docker rmi ${IMAGE_NAME}:latest || true"
        }
        success {
            mail to: [EMAIL_ADDRESS]',
                subject: 'Build Success',
                body: 'Build passed'
        }
        failure {
            mail to: [EMAIL_ADDRESS]',
                subject: 'Build Failed',
                body: 'Check logs'
        }
    }
}
