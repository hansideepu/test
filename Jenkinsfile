pipeline {
    agent { docker { image 'python:2.7' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
        stage('test'){
            steps{
                sh 'python src/test.py'
            }
        }
    }
}
