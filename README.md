# Connect-PC-over-LAN

Libraries Used – 
1.	Thread – Here used for running two functions (accept_connections and server) simultaneously
2.	Socket – Used for connecting two computers
3.	OS – Used for running the system commands on server side.
4.	Smtplib – Used for logging into server side email id and sending the ip address.
5.	Getpass – Used for entering the server side email password in the asterick form.

The software is basically having two parts –

1.	Authorizing connection between client and server.

•	On the request of the user at the server side an email address is entered.
•	Using smtplib an email consisting of the local IP address of the server and an unique otp is sent to the client’s email address.
•	Then the user at the client side enter the IP address and the otp sent via email on the client side program.
•	If the otp sent by the client machine matches is found on the generated otp list ( a list in the server machine that contains all the otps which have been sent to clents on their requests) then a confirmation message will be sent to the client machine and the IP address of the client machine will be stored in a list.

2.	Using the linux server – 

•	As soon as the user gets connected, he/ she gets into the terminal of the linux machine through the client side programs.
•	Now each time the user types a command, the command is first converted to bytes and sent to the linux machine using a particular port number (in our case 1024).
•	Each time the linux machine receives a command it first checks the IP address of the machine from which the command has been sent and if the IP address is found in the accepted IP address list then it will proceed.
•	Then by using the popen command from the os library it will execute the command on the linux machine and store the output in a variable.
•	Then the output will be encoded by ‘utf - 8’ and will be sent to the client machine.
•	The client machine will then show the output after decoding using ‘utf-8’.
