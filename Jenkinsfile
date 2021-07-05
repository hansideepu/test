pipeline{
    agent any
    stages{   
        stage('Setup') { // Install any dependencies you need to perform testing
          steps {
            script {
              sh """pip install -r requirements.txt"""
            }
        }
    }
        stage('testing'){
            steps{
                sh 'python src/test.py'
            }
        }
    }
}
