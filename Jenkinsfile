pipeline {
    agent any
    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'staging', url: 'https://github.com/Siddhantt/Insurance-flask-app.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }
        stage('Run Ansible Playbook') {
            steps {
                sh '''
                    ansible-playbook -i inventory.ini playbook.yml
                '''
            }
        }
    }
}

