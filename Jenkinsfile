pipeline{
    agent any
    stages{
        stage('Print'){
            steps{
                print(params.Operations)
               bat "Operations.py ${Operations}"
            }
        }
    }
}