pipeline{
    agent any
    stages{
        stage('Install Dependencies'){
            steps{
                sh 'pip install -r requirements.txt'
            }
        }
        stage('testing'){
            steps{
                sh 'pip install flask'
                sh 'python src/test.py'
            }
        }
    }
}
