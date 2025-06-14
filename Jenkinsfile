pipeline {
    agent any

    environment {
        ANSIBLE_HOST_KEY_CHECKING = 'False'
    }

    stages {
        stage('Clone Repo') {
            steps {
                // Replace with your actual GitHub repo
                git 'https://github.com/Siddhantt/insurance-flask-app.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    apt update
                    apt install -y ansible sshpass python3 python3-pip python3-venv
                '''
            }
        }

        stage('Run Ansible Playbook') {
            steps {
                sh '''
                    ansible-playbook -i inventory.ini deploy.yml
                '''
            }
        }
    }
}

