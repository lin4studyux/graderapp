pipeline {
  agent any
  stages {
    stage ('Build') {
      steps {
        echo 'Running build automation'
      }
    }
    stage('DeployToStaging') {
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
                                configName: 'staging',
                                sshCredentials: [
                                    username: "$USERNAME",
                                    encryptedPassphrase: "$USERPASS"
                                ],
                                transfers: [
                                    sshTransfer(
                                        sourceFiles: 'main.py',
                                        remoteDirectory: '/tmp'
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
