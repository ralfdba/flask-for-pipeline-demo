pipeline {
    agent any
    environment {
        scannerHome = tool "sonarqubescanner"
    }
    stages {
        stage('Iniciando'){
            steps {
                sh 'echo $WORKSPACE'
            }
        }
        stage('Check-gitsecrets'){
            steps {
                sh 'docker run ghcr.io/trufflesecurity/trufflehog:latest github --repo https://github.com/ralfdba/flask-for-pipeline-demo'
            }
        }
        stage('SCA'){
            steps {
                sh 'rm owasp* || true'
                sh 'wget https://raw.githubusercontent.com/ralfdba/demo-pipeline-jenkins/main/owasp-sca.sh'
                sh 'chmod +x owasp-sca.sh'
                sh 'bash owasp-sca.sh'
                sh 'chown jenkins:jenkins odc-reports'                
            }
        }
        stage('SAST'){
            steps {
                withSonarQubeEnv('sonarqubeid') {
                    sh "${scannerHome}/bin/sonar-scanner -Dsonar.projectKey=develop"
                }
            }
        }
        stage('DAST'){
            steps {
                sh 'docker run -t owasp/zap2docker-stable zap-baseline.py -t https://blazedemo.com/'
            }
        }
    }
}