pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                // Checkout your code from Git
                git 'https://github.com/your/repository.git'
            }
        }
        
        stage('Build') {
            steps {
                // Execute Python script
                sh 'python script.py'
            }
        }
    }
    
    post {
        success {
            // Notify on success
            echo 'Pipeline successful!'
        }
        failure {
            // Notify on failure
            echo 'Pipeline failed!'
        }
    }
}

