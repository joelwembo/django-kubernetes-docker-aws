pipeline {
    agent any

    stages {
        stage('Start') {
            steps {
                echo 'Starting the Entrypoint...'
            }
        }
        stage('Build') {
            steps {
                echo 'Building...'
                python3 manage.py runserver
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing...'
            }
        }

         stage('Release') {
            steps {
                echo 'Releasing...'
            }
        }
    }
}