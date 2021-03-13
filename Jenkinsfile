pipeline {
  agent any
  stages {
    stage ('Build') {
      steps {
        echo 'Running an empty build step.'
      }
    }
    stage('DeployToProd') {
            when {
                branch 'master'
            }
            steps {
                withCredentials([sshUserPrivateKey(credentialsId: 'webserver_login1')]) {
                    sshPublisher(
                        failOnError: true,
                        continueOnError: false,
                        publishers: [
                            sshPublisherDesc(
                                verbose: true,
                                configName: 'cloud',
                                transfers: [
                                    sshTransfer(
                                        sourceFiles: 'main.py, requirements.txt',
                                        remoteDirectory: '/tmp',
                                        execCommand: "kill -9 \$(ps aux | grep main | grep -v grep |awk '{print \$2}') ; /usr/bin/python3 /tmp/main.py >> /dev/null 2>&1 &"
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
