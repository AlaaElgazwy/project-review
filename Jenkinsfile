pipeline {
    agent any

    environment {
 
        DOCKER_IMAGE = 'alaaelgazwy/django-calculator'
     
        DOCKER_CREDENTIALS_ID = 'dockerhub'
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
                    echo 'Building Docker Image...'
                    sh "docker build -t $DOCKER_IMAGE:latest ."
                }
            }
        }

      
        stage('Login to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: DOCKER_CREDENTIALS_ID, passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USERNAME')]) {
                    sh "echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin"
                }
            }
        }
        stage('Push Image') {
            steps {
                script {
                    echo 'Pushing image to Docker Hub...'
                    sh "docker push $DOCKER_IMAGE:latest"
                }
            }
        }
    }
}