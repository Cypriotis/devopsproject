pipeline {
    agent any


    stages {
        stage('Build') {
            steps {
                // Get some code from a GitHub repository
                git branch: 'main', url: 'git@github.com:Cypriotis/devopsproject.git'

                
            }
        }
        
        stage('Test') {
            steps {
                sh '''
                    python3 -m venv myvenv
                    . ./myvenv/bin/activate
                    pip install -r requirements.txt
                    echo here
                    cd devopsproject
                    cp devopsproject/.env.example devopsproject/.env'''
            }
        }
        stage('Install Ansible prerequisites') {
            steps {
                sh '''
                    ansible-galaxy install geerlingguy.mysql
                '''

                sh '''
                    mkdir -p ~/workspace/ansible-example/files/certs
                    cd ~/workspace/ansible-example/files/certs
                    openssl req -x509 -newkey rsa:4096 -keyout server.key -out server.crt -days 365 --nodes -subj '/C=GR/O=myorganization/OU=it/CN=myorg.com'
                '''
            }
        }
        stage('Prepare DB') {
            steps {
                sshagent(credentials: ['ssh-deployment-1']) {
                sh '''
                    pwd
                    echo $WORKSPACE

                    ansible-playbook -i ~/workspace/ansible-example/hosts.yml -l db01 ~/workspace/ansible-example/playbooks/mysql-database.yml
            '''
        }
    }
}
        stage('deploym to vm 1') {
            steps{
                sshagent (credentials: ['ssh-deployment-1']) {
                    sh '''
                    pwd
                    echo $WORKSPACE
                        ansible-playbook -i ~/workspace/ansible-example/hosts.yml -l db01 --extra-vars "user_dir=/home/azureuser" ~/workspace/ansible-example/playbooks/django-project-install.yml
                    '''
                }

            }

        
    }
}
}