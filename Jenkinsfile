pipeline{
    agent any
    stages{
        stage('Prepare Build Env') {
            steps {
                sh """
                    python3 --version
                    python3 -m venv .venv
                    . .venv/bin/activate
                    pip3 install -r requirements.txt
                """
            }
        }
    //stages{   
    //    stage('Install dependencies'){
    //      steps {
    //          sh 'pip install -r requirements.txt'
    //      }
    //    }
        stage('testing'){
            steps{
                sh 'python src/test.py'
            }
        }
    }
}
