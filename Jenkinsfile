pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-projetGroup4')
        IMAGE_NAME = 'attidiany/my_data_app'
    }

    stages {
        stage('Nettoyer workspace') {
            steps {
                deleteDir()
            }
        }

        stage('Checkout') {
            steps {
                git url: 'https://github.com/AliatTidiany/My_Data_App.git', branch: 'main'
            }
        }

        stage('Construire l’image') {
            steps {
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Connexion à Docker Hub') {
            steps {
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
            }
        }

        stage('Pousser l’image') {
            steps {
                sh 'docker push $IMAGE_NAME'
            }
        }

        stage('Déployer') {
            steps {
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
