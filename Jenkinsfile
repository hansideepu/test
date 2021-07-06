pipeline {
    agent { docker { image 'python:3.7' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
        stage('test'){
            steps{
                sh 'sudo -H pip install flask'
                sh 'python src/test.py'
            }
        }
    }
}
