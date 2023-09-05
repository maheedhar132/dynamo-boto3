pipeline{
    agent any
    stages{
        stage('install'){
            steps{sh"sudo apt install python3-pip
            pip3 install boto3"}
        }
        stage('Print'){
            steps{sh "python3 Operations.py ${databaseName} ${Operations}"}
        }
    }
}