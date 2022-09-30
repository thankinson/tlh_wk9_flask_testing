pipeline {
    agent any

    stages {
        stage('install requirments') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Testing'){
            steps {
                sh 'python -m pytest --tb=short --cov=test_app'
            }
        }
        stage('Start App'){
            steps {
                sh 'python ./app.py'
            }
        }

    }
}