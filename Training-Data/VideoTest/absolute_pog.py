import paramiko

host = "173.48.66.87"
port = 22
username = "daqureshi"
password = "Dq03252003"
command = "cat test.txt"


ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(host, port, username, password)
