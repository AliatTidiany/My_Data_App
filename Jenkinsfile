pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-projetGroup4')
        IMAGE_NAME = 'attidiany/my_data_app'
    }

    stages {
        stage('Cloner le dépôt') {
            steps {
                sh 'git clone https://github.com/AliatTidiany/My_Data_App.git'
                dir('My_Data_App') {
                    sh 'ls -la'  // Vérifie que le contenu est bien là
                }
            }
        }

        stage('Construire l’image') {
            steps {
                dir('My_Data_App') {
                    sh 'docker build -t $IMAGE_NAME .'
                }
            }
        }

        // ... autres étapes inchangées, mais toujours dans `dir('My_Data_App')` si nécessaires ...
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
#ggg