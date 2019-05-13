import sshclient

if __name__ == "__main__":
    conn = sshclient.SSHConnection('gamedebug.iok.la', 8202, 'root', '1qaz@WSX3edc$')
    conn.exec_command('ls -ll')
    #conn.exec_command('cd /root;pwd')  # cd需要特别处理
    #conn.exec_command('pwd')
    print(conn.exec_command('tree /root'))
