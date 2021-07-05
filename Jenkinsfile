pipeline{
    agent any
    stages{   
        stage('Install dependencies'){
          steps {
              sh 'pip install -r requirements.txt'
          }
        }
        stage('testing'){
            steps{
                sh 'python src/test.py'
            }
        }
    }
}
