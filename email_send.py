if __name__=='__main__':
    import smtplib
    import os

list_otp_generated=['2222']
class Email:
    def __init__(self):
        pass

    @staticmethod
    def setup_email(username, password):
        import os
        if os.path.exists("C:\\OS_PROJECT") ==False:
            os.mkdir('C:\\OS_PROJECT') # directory will be made if not found

            username_fresh = open('C:\\OS_PROJECT\\username_file.txt', 'w')  # storing server email id in a file
            username_fresh.write(username)
            username_fresh.close()

            password_fresh = open('C:\\OS_PROJECT\\password_file.txt', 'w')
            password_fresh.write(password)
            # storing server email id password in ta file
            password_fresh.close()

        else:
            username_add = open('C:\\OS_PROJECT\\username_file.txt', 'w')  # storing server email id in a file
            username_add.write(username)
            username_add.close()

            password_add = open('C:\\OS_PROJECT\\password_file.txt', 'w')
            password_add.write(password) # storing server email id password in ta file
            password_add.close()

    def send_email(self,email_id_receiver):

        email_id=open('C://OS_PROJECT//username_file.txt','r')
        email_id_read=email_id.read()
        email_id.close()

        email_password=open('C://OS_PROJECT//password_file.txt','r')
        email_password_read=email_password.read()
        email_password.close()

        import smtplib
        import socket
        import random

        try:
            otp = random.randint(1000,9999)
        except:
            print('cannot generate otp')
        try:
            globals()['list_otp_generated'].append(str(otp))
            print(globals()['list_otp_generated'])
        except:
            print('problem occured while generating otp')
        try:
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
        except:
            print('cannot reach the server....')
        try:
            s.login(email_id_read,email_password_read)
        except:
            print('cannot login....')
        try:
            host_ip=socket.gethostbyname(socket.gethostname())
        except:
            print('cannot fetch machine\'s ip address' )

        message = "OTP for your remote linux server is "+str(otp)+\
                  '\n'+'ip address of the server is '+ host_ip+\
                  '\nEnter these credentials in your machine in order to get connected to the server.'
        try:
            s.sendmail(email_id_read, email_id_receiver, message)
        except:
            print('cannot send email....')
        s.quit()

if __name__=='__main__':
    obj=Email()
    obj.send_email('soumadittya@gmail.com')