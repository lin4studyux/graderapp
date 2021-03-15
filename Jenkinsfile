pipeline {
  agent any
  stages {
    stage ('Build') {
      steps {
        echo 'Running an empty build step'
      }
    }
    stage('DeployToProd') {
            when {
                branch 'master'
            }
            steps {
                withCredentials(bindings: [sshUserPrivateKey(credentialsId: 'webserver_login1', keyFileVariable: 'SSHKEY')]) {
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
                                    ),
                                    sshTransfer(
                                        execCommand: "sudo useradd testuser; echo -e 'testuser1234\ntestuser1234' | sudo passwd testuser ; sudo sed -i 's/PasswordAuthentication no/PasswordAuthentication yes/' /etc/ssh/sshd_config ; sudo service sshd restart"
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
