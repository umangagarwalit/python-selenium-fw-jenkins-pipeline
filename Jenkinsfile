pipeline {
    agent any
    
    stages {
	
        stage('Checkout Code') {
            steps {
                git url: 'https://github.com/umangagarwalit/python-selenium-fw-jenkins-pipeline.git', branch: 'main'
            }
        }

        stage('Install Python & Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Python Script') {
            steps {
                bat 'pytest -s -v tests\\test_login.py --html=reports/report.html --self-contained-html --capture=tee-sys'
            }
        }
    }
}
