import socket
import os
import sys
import subprocess
import email_send #own module

list_otp_accepted=['']

def accept_connection():
    try:
        while True:
            s_accept=socket.socket()
            host=''
            port=1025
            s_accept.bind((host,port))
            s_accept.listen(1)
            conn,addr=s_accept.accept()
            #if addr[0]==socket.gethostbyname(socket.gethostname()):
                #print('server stopped')
                #break
            otp_received=conn.recv(1025)
            otp_received=otp_received.decode('utf-8')
            for i in email_send.list_otp_generated: # checks whether the received otp is in generated otp list
                if otp_received == i:
                    globals()['list_otp_accepted'].append(addr[0])
                    conn.send('You are connected to the server....'.encode('utf-8'))
                elif email_send.list_otp_generated[-1]==i: # even if the last element in the list does not match then it will
                    conn.send('no'.encode('utf-8'))        #send no to the client so that client can show a message that the
    except:                                                # client is not authorised
            pass

def server():

    while True:
        s=socket.socket()
        host=''
        port=1024
        s.bind((host,port))
        s.listen(1)
        print('waiting for incoming connections....')
        conn, addr = s.accept()

        #if addr[0]==socket.gethostbyname(socket.gethostname()):
            #print('\nserver stopped....')
            #break

        command_received = conn.recv(1024)
        command_decoded=command_received.decode('utf-8')
        print('command decoded type', type(command_decoded))
        print(addr[0])
        print(type(addr[0]))
        print('server',id(addr[0]))

        if addr[0] in globals()['list_otp_accepted']: # checks whether the message is coming from accepted ip
            command_batch_file = open('command.bat', 'w')
            command_batch_file.write(command_decoded)
            command_batch_file.close()
            print(command_decoded)
            try:
                command_result = os.popen('command.bat').read()  # cmd takes , iterpretes and returns the result
                if command_result=='':
                    conn.send('Nothing to show....'.encode('utf-8'))
                else:
                    conn.send(command_result.encode('utf-8'))  # sends the result ack to kind
            except:
                conn.send('cannot process the request'.encode('utf-8'))
        else:
            conn.send('You are not authorised'.encode('utf-8'))

        s.close()