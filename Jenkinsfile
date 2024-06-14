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
                sh 'python3 script.py'
            }
        }
    }
    
    post {
        success {
            // Notify on success
            slackSend(color: 'good', message: "Pipeline successful!", channel: '#sending-notifications')
        }
        failure {
            // Notify on failure
            slackSend(color: 'danger', message: "Pipeline failed!", channel: '#sending-notifications')
        }
    }
}

def slackSend(def color, def message, def channel) {
    slackSend(
        color: color,
        message: message,
        channel: channel,
        tokenCredentialId: 'U05eNBeTfzexuZaxxOGvPUiN'
    )
}

