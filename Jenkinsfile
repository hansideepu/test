pipeline{
    agent any
    stages{
        stage('Install Dependencies'){
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh 'virtualenv venv && . venv/bin/activate && pip install -r requirements.txt'
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
