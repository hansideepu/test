pipeline{
    agent any
    stages{
        stage('Install Dependencies'){
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh 'pip install --user -r requirements.txt'
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
