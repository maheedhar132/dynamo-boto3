pipeline{
    agent any
    stages{
        stage('Print'){
            steps{
                print(params.Operations)
               bat "python Operations.py"
            }
        }
    }
}