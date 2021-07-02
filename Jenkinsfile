pipeline{
    agent any
    stages{
        stage('testing'){
            steps{
                sh 'pip install flask'
                sh 'python src/test.py'
            }
        }
    }
}
