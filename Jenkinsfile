groovy
pipeline {
    agent any
    stages {
        stage('Test') {
            steps {
                sh 'pytest test/ --alluredir=allure-results'

            }
        }

        stage('Report') {
            steps {
                sh 'allure serve allure-results'
            }
        }
    }
}
