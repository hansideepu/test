pipeline{
    agent any
    stages{
        stage('Install Dependencies'){
            steps {
                 sh 'virtualenv venv && . venv/bin/activate && pip install -r requirements.txt && python src/test.py'
                }
            }    
        stage('testing'){
            steps{
                sh 'python src/test.py'
            }
        }
    }
}
