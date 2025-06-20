pipeline {
    agent any

    environment {
        IMAGE_NAME = 'attidiany/my_data_app'
    }

    stages {
        stage('Nettoyer workspace') {
            steps {
                deleteDir()
            }
        }

        stage('Cloner le dépôt') {
            steps {
                git url: 'https://github.com/AliatTidiany/My_Data_App.git', branch: 'main'
            }
        }

        stage('Construire l’image') {
            steps {
                script {
                    dockerImage = docker.build(IMAGE_NAME)
                }
            }
        }

        stage('Connexion à Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-projetGroup4', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh "echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin"
                }
            }
        }

        stage('Pousser l’image') {
            steps {
                script {
                    dockerImage.push()
                }
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
