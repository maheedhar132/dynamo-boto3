pipeline{
    agent any
    stages{
        stage('Print'){
            sh "python3 Operations.py ${databaseName} ${Operations}"
        }
    }
}