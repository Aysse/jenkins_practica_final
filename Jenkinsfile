pipeline {
  agent any
  stages {
    stage('practicaFinal') {
      agent {
        node {
          label 'master'
        }

      }
      steps {
        sh '''cd /home/aysse/practicafinal/py/jenkins_practica_final
python3 test_triangle.py'''
      }
    }

  }
}