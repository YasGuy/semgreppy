pipeline {
    agent any

    environment {
        SEMGREP_VERSION = '0.79.0'
    }

    stages {
        stage('Setup') {
            steps {
                sh 'python3 -m venv venv'
                sh './venv/bin/pip install semgrep==${SEMGREP_VERSION}'
                sh './venv/bin/pip install -r requirements.txt'
            }
        }

        stage('Build') {
            steps {
                script {
                    def buildScript = '''
                    echo "Building the project..."
                    # Add any build steps if necessary, e.g., compiling, packaging, etc.
                    '''
                    sh buildScript
                }
            }
        }

        stage('Semgrep Analysis') {
            steps {
                sh './venv/bin/semgrep --config .semgrep.yml'
            }
        }

        stage('Test') {
            steps {
                sh './venv/bin/pytest'
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
