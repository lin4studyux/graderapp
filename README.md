- graderapp
- to test this endpoint:
- Use browser to publicly access over the internet: using http://52.201.75.252:5001/grader/84.2/Fahrenheit/Rankine/543.94 
  or
- ssh into ec2-52-201-75-252.compute-1.amazonaws.com using: ssh testuser@ec2-52-201-75-252.compute-1.amazonaws.com
- your password is: testuser1234
-  use following url
- curl http://0.0.0.0:5001/grader/<num_value>/<unit_of_measure>/<target_unit_of_measure>/<student_response>
- Example below:
- curl http://0.0.0.0:5001/grader/84.2/Fahrenheit/Rankine/543.94
- Expected:
- {"data": {"grade": "correct"}}

To locally run the application:
1. git clone the repo: https://github.com/lin4studyux/graderapp
2. change directory into graderapp folder
3. install python3 on your computer (run executables for windows, sudo yum install -y python36 for linux)
4. For windows, pip3 would be inside Scripts folder of the installation, for linux install pip3 -> yum install -y python36-devel, python36-setuptools -> easy_install-3.6 pip
5. run command pip3 install -r requiremnts.txt to install dependencies
6. Start application by running: python3 main.py or run using pycharm IDE
7. test by running curl http://0.0.0.0:5001/grader/84.2/Fahrenheit/Rankine/543.94

To test the automated solution:
1. I have created a jenkins server on a virtual machine for CICD and code is available in github for CI.
2. Create AWS server infrastructure by using Cloudformation file: setup-env.yml (this takes care of all the dependencies installation too)
3. Capture the public-IP-Address of EC2 instance and manually edit (only once) into Jenkins Dashboard at http://a6adc139721c.mylabserver.com:8080/ -> manage jenkins -> configure system -> Publish over SSH -> hostname -> save
4. Either manually start the Build or commit a change in github repository at https://github.com/lin4studyux/graderapp
5. app will be deployed on EC2 and ready for use
6. Test by connecting to EC2 instance and running curl http://0.0.0.0:5001/grader/84.2/Fahrenheit/Rankine/543.94. Expected output: {"data": {"grade": "correct"}}
7. username and password for testuser are provided above.

A prioritized list of development tasks:
1. Improve the code performance by using better data structures and probably lambda expressions.
2. Instead of running a python program, set it up as a systemd service so that it can start automatically upon system reboot.
3. Automate jenkins server setup using terraform and ansible amd make it highly available.
4. Containerize the application deployment by leveraging Kubernetes and Docker.
5. Imlement autoscaling for app deployment to introduce faul-tolerance and cost optimisation.
