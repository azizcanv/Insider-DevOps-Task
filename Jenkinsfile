pipeline {
    agent any

    environment {
        HOME_DIR = sh(script: 'echo $HOME', returnStdout: true).trim()
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    def repoUrl = 'https://github.com/azizcanv/Insider-DevOps-Task.git'
                    git branch: 'main', url: repoUrl
                }
            }
        }

        stage('Build') {
            steps {
                script {
                    sh 'python run_tests.py' // run_tests.py scriptini çalıştır
                }
            }
        }

        stage('Publish Reports') {
            steps {
                script {
                    archiveArtifacts artifacts: 'report.html', allowEmptyArchive: true // Test raporlarını arşivle
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}