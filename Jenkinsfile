pipeline {
    agent any

    environment {
        ANSIBLE_HOST_KEY_CHECKING = 'False'
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'staging', url: 'https://github.com/Siddhantt/Insurance-flask-app.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip3 install --user -r requirements.txt'
            }
        }

        stage('Run Ansible Playbook') {
            steps {
                sh 'ansible-playbook -i inventory.ini deploy.yml'
            }
        }
    }
}

