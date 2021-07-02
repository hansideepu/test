pipeline{
    agent any
    stages{
        stage('testing'){
            steps{
                sh 'pip install Flask'
                sh 'python src/test.py'
            }
        }
    }
}
