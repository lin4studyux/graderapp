pipeline {
  agent any
  stages {
    stage ('Build') {
      steps {
        echo 'Running build automation'
        archiveArtifacts artifacts: '/graderapp/main.py'
        sh ‘ssh cloud_user@c7d0db6c641c.mylabserver.com mkdir -p /graderapp’
        sh ‘scp -r main.py cloud_user@c7d0db6c641c.mylabserver.com:/graderapp/’
      }
    }
  }
}
