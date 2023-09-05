pipeline{
    agent any
    stages{
        stage('install'){
            steps{sh "apt install python3-pip -y"
            sh "pip3 install boto3"}
        }
        stage('Print'){
            steps{sh "python3 Operations.py ${databaseName} ${Operations}"}
        }
    }
}