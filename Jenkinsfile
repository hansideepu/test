pipeline{
    agent any
    stages{   
        stage("Python Test") {
          agent { 
            docker {
              label "docker && linux" 
              image "python:3.7"
            }
          }
          steps {
            withEnv(["HOME=${env.WORKSPACE}"]) {
              sh "pip install -r requirements.txt --user"
            }
          }
        stage('testing'){
            steps{
                sh 'python src/test.py'
            }
        }
    }
}
