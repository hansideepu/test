pipeline {
    agent { docker { image 'python:2.7' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
                sh 'python src/test.py'
            }
        }
        //stage('test'){
        //    steps{
        //        sh 'python src/test.py'
        //    }
       // }
    }
}
