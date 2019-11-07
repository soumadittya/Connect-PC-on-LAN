from email_send import * # own module
from getpass import getpass
import os
from server_send import * # own module
import time
from threading import *

t_accept_connection=Thread(target=accept_connection)
t_server=Thread(target=server)

def print_option():

    print('\n'+'1. Setup Email')
    print('2. Run the server')
    print('3. Show who is connected')
    print('4. Stop the server')
    print('5. Send otp')
    print('6. Exit')

def select_option():
    option = str(input('\n\nSelect an option - '))
    if option !='1' and option != '2' and option !='3' and option !='4' and option!='5' and option!='6':
        print('invalid input')
        print_option()
        select_option()

    elif option == '6':
        verify_close=str(input('Are you sure you want to close the program - '))
        if verify_close == 'y' or  verify_close=='Y':
            pass

        elif verify_close == 'n' or  verify_close=='N':
            print_option()
            select_option()

        elif verify_close !='n' and 'N' and 'Y' and 'y':
            print('\ninvalid input')
            print_option()
            select_option()

    elif option == '1':
        try:
            email_addr=str(input('type your email address - '))
            email_password=getpass('type your email password - ')
            Email.setup_email(email_addr,email_password)
            print_option()
            select_option()
        except:
            print('\nsomething went wrong....')
            print_option()
            select_option()

    elif option == '2':
        try:
            globals()['t_accept_connection'].start()
            globals()['t_server'].start()
        except:
            print('\nserver cannot be started....')
        time.sleep(0.5)
        print('server started')
        print_option()
        select_option()

    elif option=='4':
        verify_stop=str(input('n\Are you sure you want to stop the server ?'))

        if verify_stop == 'y' or 'Y':
            s_stop_accept=socket.socket()
            s_stop_accept.connect(socket.gethostbyname(socket.gethostname()),1024)
            s_stop_accept.send('stop_accept'.encode('utf-8'))
            s_stop_accept.close()

            s_stop_server=socket.socket()
            s_stop_server.connect(socket.gethostbyname(socket.gethostname()))
            s_stop_server.send('stop_server'.encode('utf-8'))
            s_stop_server.close()

        elif verify_stop=='n' or 'N':
            print_option()
            select_option()

        else:
            print('\ninvalid input')
            print_option()
            select_option()

    elif option== '5':
        email_id_client=str(input('Enter the client email id - '))

        try:
            otp_send=Email()
        except:
            print('cannot access email file....')

        otp_send.send_email(email_id_client)

        print_option()
        select_option()

print_option()
select_option()