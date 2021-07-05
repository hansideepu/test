pipeline{
    agent { docker { image 'python :3.7'} }
    stages{   
        stage('Build') { // Install any dependencies you need to perform testing
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
