pipeline {
  agent any
  stages {
    stage ('Build') {
      steps {
        echo 'Running build automation'
        mkdir /graderapp
        archiveArtifacts artifacts: '/graderapp/main.py'
      }
    }
  }
}
