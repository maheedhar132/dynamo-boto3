pipeline{
    agent any
    stages{
        stage('Print'){
            steps{sh "python3 Operations.py ${databaseName} ${Operations}"}
        }
    }
}