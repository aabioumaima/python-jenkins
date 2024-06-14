pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                // Checkout your code from Git
                git 'https://github.com/aabioumaima/python-jenkins.git'
            }
        }
        
        stage('Build') {
            steps {
                // Execute Python script
                sh 'python your_script.py'
            }
        }
    }
    
    post {
        success {
            // Notify on success
            slackSend(color: 'good', message: "Pipeline successful!", channel: '#your-channel')
        }
        failure {
            // Notify on failure
            slackSend(color: 'danger', message: "Pipeline failed!", channel: '#your-channel')
        }
    }
}

def slackSend(def color, def message, def channel) {
    slackSend(
        color: color,
        message: message,
        channel: channel,
        tokenCredentialId: 'your-slack-token-credential-id'
    )
}

