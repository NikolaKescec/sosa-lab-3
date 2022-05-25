pipeline {
    agent any

    stages {
        stage('prepartaion') {
            steps{
                echo "Logs folder prepared."
                sh "mkdir -p logs"
            }
        }
        stage('test') {
            steps {
                echo 'Cloning into test directory...'
                dir('test') {
                    git 'https://github.com/NikolaKescec/sosa-lab-3'
                    sh "pwd"
                    catchError {
                        sh "python dodatak_A_test.py 2>> ../logs/${env.BUILD_TIMESTAMP}.log"
                    }
                    catchError {
                        sh "bandit -r dodatak_A.py >> ../logs/${env.BUILD_TIMESTAMP}.log"
                    }
                }
            }
            post {
                failure {
                    error "Failure!"
                }
            }
        }
        stage('production') {
            steps {
              echo "Copying to production!"
              dir("production") {
                sh "rm -rf *"
                sh "cp ../test/*.py ." 
              }
            }
        }
    }
    post {
        always {
            echo 'Cleaning up remaining files from pipeline'
            dir('test') {
                deleteDir()
            }
        }
    }
}

