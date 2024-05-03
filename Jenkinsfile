pipeline {
    agent any

    parameters {
        string(name: 'BUILD_NAME', description: 'Name for the build')
        choice(name: 'NODE_COUNT', choices: ['1', '2', '3', '4', '5'], description: 'Number of nodes', defaultValue: '1')
    }

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

    options {
        buildDiscarder(logRotator(numToKeepStr: '10'))
    }

    // Build name
    displayName("${params.BUILD_NAME}")
}