pipeline {
    agent any

    triggers {
        githubPush()
    }

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-projetGroup4')
        IMAGE_NAME = 'attidiany/my_data_app'
    }

    stages {
        stage('Construire l’image') {
            steps {
                echo "Construction de l’image Docker"
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Connexion à Docker Hub') {
            steps {
                echo "Connexion à Docker Hub"
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
            }
        }

        stage('Pousser l’image') {
            steps {
                echo "Envoi de l’image vers Docker Hub"
                sh 'docker push $IMAGE_NAME'
            }
        }

        stage('Déployer') {
            steps {
                echo "Déploiement de l’application"
                sh 'docker stop my_data_app || true && docker rm my_data_app || true'
                sh 'docker run -d --name my_data_app -p 8501:8501 $IMAGE_NAME'
            }
        }
    }

    post {
        success {
            mail to: 'ambodj92@gmail.com,diopmadicke351@gmail.com',
                 subject: "Déploiement réussi",
                 body: "Votre application a été déployée avec succès."
        }
        failure {
            mail to: 'ambodj92@gmail.com',
                 subject: "Échec du déploiement",
                 body: "Une erreur est survenue pendant le pipeline Jenkins."
        }
    }
}
// This Jenkinsfile defines a pipeline for building, pushing, and deploying a Docker image.
// It includes stages for building the Docker image, logging into Docker Hub, pushing the image,
// and deploying the application. It also includes post actions to send email notifications on success or failure.
// The pipeline is triggered by a GitHub push event and uses environment variables for credentials and image name.
// The Docker commands are executed in a shell environment, and the deployment stage ensures that any existing container
