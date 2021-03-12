pipeline {
  agent any
  stages {
    stage ('Build') {
      steps {
        echo 'Running build automation'
      }
    }
    stage('DeployToProd') {
            when {
                branch 'master'
            }
            steps {
                withCredentials([usernamePassword(credentialsId: 'webserver_login', usernameVariable: 'USERNAME', passwordVariable: 'USERPASS')]) {
                    sshPublisher(
                        failOnError: true,
                        continueOnError: false,
                        publishers: [
                            sshPublisherDesc(
                                configName: 'prod',
                                sshCredentials: [
                                    username: "$USERNAME",
                                    encryptedPassphrase: "$USERPASS"
                                ],
                                transfers: [
                                    sshTransfer(
                                        sourceFiles: 'main.py',
                                        sourceFiles: 'requirements.txt'
                                        remoteDirectory: '/graderapp'
                                    )
                                ]
                            )
                        ]
                    )
                }
            }
        }
  }
}
