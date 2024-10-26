# DevopsAssignment

This project demonstrates a CI/CD pipeline setup for deploying a FastAPI application. It includes instructions for running the application locally, setting up GitHub Actions for CI, and configuring Jenkins for continuous deployment to a Kubernetes cluster.

## Prerequisites

Ensure you have the following installed on your machine:
- [Python 3.9+](https://www.python.org/downloads/)
- [Docker](https://www.docker.com/get-started)
- [Minikube (for local Kubernetes testing)](https://minikube.sigs.k8s.io/docs/start/)
- [kubectl](https://kubernetes.io/docs/tasks/tools/)
- [Jenkins (for CD)](https://www.jenkins.io/doc/book/installing/)

## Running the Application Locally

  1. **Clone the repository**:
     ```bash
     git clone [https://github.com/your-username/DevopsAssignment.git](https://github.com/Priyanshu-Raj/DevopsAssignment.git)
     cd DevopsAssignment
  2. **Install dependencies**:
      pip install -r requirements.txt
  
  3. **Run the FastAPI Application**:
      uvicorn OnlineCalculator:app --reload
  
  4. **Test the API**:
      Access the API at http://127.0.0.1:8000/

## Setting up GitHub Actions for CI

  In the .github/workflows/ directory, a file named ci.yml is created with the required configurations. 
  Every time anyone push changes to the main branch, this workflow will:
     - Check out the code.
     - Install dependencies.
     - Run tests using pytest. 

## Configuring Jenkins for Continuous Deployment    

  1. **Create a New Jenkins Pipeline Job**:
       - Go to New Item in Jenkins and create a Pipeline job.
       - Configure it to poll for changes in your GitHub repository (you can set up a webhook in GitHub as well).
  2. **Add Pipeline Script and Verify Deployment**:
        - Add a Jenkins Pipeline script to build the Docker image.
        - Push it to a local Docker registry (or DockerHub if using it), and deploy it to Kubernetes
        - check the deployment status in Minikube:
             kubectl get pods
             kubectl get services


## Jenkins Secrets     

    Go to Manage Jenkins > Manage Credentials.
    Add credentials for DockerHub or any other secrets, such as a minikubeID file for Kubernetes access
  
  

   
     
