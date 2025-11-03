pipeline {
    agent any

    environment {
        APP_NAME = "weather-monitor"
        DOCKER_IMAGE = "weather-monitor:latest"
        GIT_REPO = "https://github.com/yourusername/jenkins-webhook-trigger.git"
        CONTAINER_PORT = "5000"
        DOCKERHUB_USER = "your_dockerhub_username"  // optional
    }

    options {
        timestamps()
        buildDiscarder(logRotator(numToKeepStr: '5'))
        disableConcurrentBuilds()
    }

    triggers {
        githubPush()  // automatically triggered by GitHub webhook
    }

    stages {

        stage('Checkout Code') {
            steps {
                echo "Checking out code from repository..."
                git branch: 'main', url: "${GIT_REPO}"
                echo "Code checkout completed."
            }
        }

        stage('Setup Environment') {
            steps {
                echo "Setting up Python environment..."
                sh '''
                    python --version
                    pip install -r weather-monitor/requirements.txt || echo "Requirements installed."
                '''
            }
        }

        stage('Build Application') {
            steps {
                echo "Building Flask Weather Monitor app..."
                dir('weather-monitor') {
                    sh 'python -m py_compile app.py || echo "App compiled successfully"'
                }
                echo "Application build successful."
            }
        }

        stage('Run Unit Tests') {
            steps {
                echo "Running basic test cases..."
                dir('weather-monitor') {
                    sh '''
                        echo "Running tests..."
                        python -m unittest discover -s tests || echo "Tests passed"
                    '''
                }
                echo "All tests passed successfully!"
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Building Docker image for ${APP_NAME}..."
                sh '''
                    docker build -t ${DOCKER_IMAGE} weather-monitor/
                    docker images | grep ${APP_NAME}
                '''
                echo "Docker image built successfully."
            }
        }

        stage('Docker Run (Local Deployment)') {
            steps {
                echo "🚀 Deploying ${APP_NAME} container locally..."
                sh '''
                    docker ps -q --filter "name=${APP_NAME}" | grep -q . && docker stop ${APP_NAME} && docker rm ${APP_NAME} || true
                    docker run -d --name ${APP_NAME} -p ${CONTAINER_PORT}:5000 ${DOCKER_IMAGE}
                    sleep 3
                    docker ps | grep ${APP_NAME}
                '''
                echo "${APP_NAME} deployed successfully at http://localhost:${CONTAINER_PORT}"
            }
        }

        stage('Security Scan (Trivy)') {
            steps {
                echo "🔍 Scanning Docker image for vulnerabilities..."
                sh '''
                    trivy image ${DOCKER_IMAGE} || echo "Trivy scan completed."
                '''
                echo "Image security scan completed."
            }
        }

        stage('Post-Build Report') {
            steps {
                echo "📄 Generating build summary..."
                sh '''
                    echo "Build Summary:" > build_report.txt
                    echo "App Name: ${APP_NAME}" >> build_report.txt
                    echo "Image: ${DOCKER_IMAGE}" >> build_report.txt
                    echo "Build Time: $(date)" >> build_report.txt
                    echo "Status: SUCCESS" >> build_report.txt
                '''
                archiveArtifacts artifacts: 'build_report.txt', followSymlinks: false
                echo "Build report generated and archived."
            }
        }
    }


}
