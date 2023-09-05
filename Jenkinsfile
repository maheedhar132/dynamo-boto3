pipeline{
    agent any
    stages{
        stage('Print'){
            steps{
                print(params.Operations)
                script{
                  bat "python Operations.py --var=${Operations}"
                }
            }
        }
    }
}