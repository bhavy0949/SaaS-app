pipeline {
    agent any

    environment {
        // Replace this with your actual Docker Hub username and repository name
        
        IMAGE_NAME = 'bhavy0949/saas-app'
        IMAGE_TAG = "${env.BUILD_NUMBER}"
    }


    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/bhavy0949/SaaS-app'
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
        stage('Docker Login') {
           steps {
            withCredentials([string(credentialsId: 'docker-token', variable: 'DOCKER_TOKEN')]) {
             sh 'echo $DOCKER_TOKEN | docker login -u bhavy0949 --password-stdin'
            }
           }
          }

        stage('Push Docker Image') {
            steps {
                script {
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
            mail to: $EMAIL_ADDRESS,
                subject: 'Build Success',
                body: 'Build passed'
        }
        failure {
            mail to: $EMAIL_ADDRESS,
                subject: 'Build Failed',
                body: 'Check logs'
        }
    }
}
