pipeline {
    agent any

    environment {
        KUBECONFIG_CREDENTIAL_ID = 'minikubeID'  // ID of Jenkins Credential with kubeconfig
        GITHUB_REPO = 'https://github.com/Priyanshu-Raj/DevopsAssignment.git'  // Your GitHub repository URL
    }

    stages {
        stage('Checkout Code') {
            steps {
                // Pulls the latest code from the GitHub repository
                git branch: 'main', url: "${GITHUB_REPO}"
            }
        }

        stage('Build and Test') {
            steps {
                // Insert build/test steps here as required
                echo 'Building and testing...'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                withCredentials([file(credentialsId: "${KUBECONFIG_CREDENTIAL_ID}", variable: 'KUBECONFIG')]) {
                    sh '''
                    kubectl apply -f manifests/deployment.yaml
                    kubectl apply -f manifests/service.yaml
                    '''
                }
            }
        }
    }
}
