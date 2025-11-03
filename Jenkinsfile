pipeline {
    agent any

    triggers {
        githubPush()
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/mihirhebalkar/jenkins-webhook-trigger.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t weather-monitor:latest ./weather-monitor'
                }
            }
        }

        stage('Run Container') {
            steps {
                script {
                    sh 'docker run -d -p 5000:5000 weather-monitor:latest'
                }
            }
        }
    }
}
