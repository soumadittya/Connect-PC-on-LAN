import socket
from client_send import *

def print_option():
    print('\n1. Enter otp and connect')
    print('2. Use the server')
    print('3. Exit')

def select_option():
    option = str(input('\nSelect an option - '))
    if option !='1' and option != '2' and option !='3':
        print('invalid input')
        print_option()
        select_option()

    elif option == '3':
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

    elif option=='1':
        ip=str(input('Enter the ip address - '))
        otp =  str(input('Enter the otp - '))
        client_request(ip,otp)
        print('\ninput taken')
        time.sleep(1)
        print_option()
        select_option()

    elif option=='2':
        if ip_connected!='':
            print('you are not connected')
        else:
            try:
                client_use(ip_connected)
            except:
                print('cannot connect....')

print_option()
select_option()