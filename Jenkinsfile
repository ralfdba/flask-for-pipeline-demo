pipeline {
    agent any
    environment {
        scannerHome = tool 'sonarqubescanner'
    }    
    stages {
        stage('Iniciando-pipeline') {
          steps {
            sh 'echo $WORKSPACE'
          }
        }
        stage('Check-git-secrets') {
          steps {
            sh 'docker run ghcr.io/trufflesecurity/trufflehog:latest github --repo https://github.com/ralfdba/flask-for-pipeline-demo'
          }
        }
        
        stage('SCA') {
          steps {
            sh 'rm owasp* || true'
            sh 'wget https://raw.githubusercontent.com/ralfdba/demo-pipeline-jenkins/main/owasp-sca.sh'
            sh 'chmod +x owasp-sca.sh'
            sh 'bash owasp-sca.sh'
            sh 'chown jenkins:jenkins odc-reports'
          }
        }        
        
        stage('SAST') {
            steps {
                withSonarQubeEnv('sonarqubeid') {
                    sh "${scannerHome}/bin/sonar-scanner -Dsonar.projectKey=develop"
                }
            }
        }
        
        stage('Build Project') {
            steps {
                sh 'pip install -r requirements.txt'
                sh 'flask --app hello run'
            }
        }
    }
}
