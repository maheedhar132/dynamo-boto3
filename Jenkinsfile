pipeline{
    agent any
    stages{
        stage('Print Vars'){
            steps{
             print(params.Operations)
        }
        stage('Python'){
            steps{
                bat "python3 Operations.py ${Operations}"
            }
        }
    }
}
}