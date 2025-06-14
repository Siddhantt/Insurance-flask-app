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
                sh '''
                     apt-get update
                     apt-get install -y python3-pip sshpass ansible
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

