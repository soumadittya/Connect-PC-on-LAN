import socket
import time

ip_connected=''
stop=''
cd=''


def client_request(ip,otp):
    s=socket.socket()
    s.connect((ip,1025))
    print('channel formed....')
    s.send(otp.encode('utf-8'))
    print('otp sent')
    accept=s.recv(1025)
    print('response received....')
    accept=accept.decode('utf-8')
    print('processing response....')
    if accept=='You are connected to the server....':
        globals()['ip_connected']=ip
        print(accept)
    else:
        print('\nrequest denied! try again')
    s.close()

def client_use(ip):
    while True:
        s_use=socket.socket()
        print('========================\n')
        type_command=str(input('>> '))
        if type_command[:2] == 'cd':
            globals()['cd'] = globals()['cd']+'\n'+ type_command
        try:
            s_use.connect((ip,1024))
        except:
            print('\ncannot connect to the server....')
            client_use(ip_connected)
        try:
            if globals()['cd'] !='' and type_command[:2]!='cd':
                command_send=globals()['cd']+'\n'+type_command
                s_use.send(command_send.encode('utf-8'))
            elif type_command[:2]=='cd':
                s_use.send(type_command.encode('utf-8'))
            elif globals()['cd']=='':
                s_use.send(type_command.encode('utf-8'))
        except:
            print('\ncannot send the command....')
            client_use(ip_connected)
        try:
            result=s_use.recv(1024)
            result=result.decode('utf-8')
            print(result)
        except:
            print('cannot receive the response....')
            client_use(ip_connected)
        s_use.close()

if __name__=='__main__':
    client_request('192.168.137.1','2222')
    client_use(ip_connected)