pipeline{
    agent any
    stages{
        stage('Install Dependencies'){
            steps{
                bat "pip install boto3"
            }
        }
        stage('Print'){
            steps{
                print(params.Operations)
               bat "Operations.py ${databaseName} ${Operations}"
            }
        }
    }
}