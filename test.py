import sshclient

if __name__ == "__main__":
    conn = sshclient.SSHConnection('10.0.0.1', 22, 'root', '123456')
    conn.exec_command('ls -ll')
    #conn.exec_command('cd /root;pwd')  # cd需要特别处理
    #conn.exec_command('pwd')
    print(conn.exec_command('tree /root'))
