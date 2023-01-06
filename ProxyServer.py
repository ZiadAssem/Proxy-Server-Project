from socket import *
import sys as sys

if len(sys.argv) <= 1:
    print ('Usage : "python ProxyServer.py server_ip"\n[server_ip : It is the IP Address Of Proxy Server')
    sys.exit(2)

#  Create a server socket, bind it to a port and start listening
tcpSerSock = socket(AF_INET, SOCK_STREAM)

# Fill in start.
serverPort = 12000
tcpSerSock.bind((sys.argv[1], serverPort))
tcpSerSock.listen(10)
# Fill in end.

# Blocked urls
with open('blockedUrl.txt') as f:
    blocked_urls = set(f.read().splitlines())

while 1:
    # Start receiving data from the client
    print ('\n\nReady to serve...')
    tcpCliSock, addr = tcpSerSock.accept()
    print ('Received a connection from:', addr)
    # Fill in start.
    message = tcpCliSock.recv(1024)
     # Fill in end.
    if message:
        print (message)
        filename = message.split()[1].decode("utf-8").rpartition("/")[2]
        filenameTest = message.split()[1].decode("utf-8")

        if not ( filenameTest in blocked_urls):
            fileExist = "false"
            filetouse = "\\cache\\" + filename
            print("The File is not blocked")


            try:
                # Check wether the file exist in the cache
                f = open(filetouse[1:], "rb")
                outputdata = f.readlines()
                fileExist = "true"
                # ProxyServer finds a cache hit and generates a response message
                tcpCliSock.send(b"HTTP/1.0 200 OK\r\n")
                tcpCliSock.send(b"Content-Type:text/html\r\n")
                # Fill in start.
                for line in outputdata:
                    tcpCliSock.send(line)
                f.close()
                # Fill in end.
                print ('Read from cache')
            # Error handling for file not found in cache
            except IOError:
                try:
                    if fileExist == "false":
                        print("File not found in cache")
                        # Create a socket on the proxyserver
                        c = socket(AF_INET, SOCK_STREAM)
                        # Fill in start. # Fill in end.
                        hostn = message.split()[4].decode("utf-8")
                        print( "hostn is "+hostn)
                        
                        
                        print('Attempting cache')
                        # Connect to the socket to port 80
                        # Fill in start.
                        c.connect((hostn, 80))
                        # Fill in end.
                        # Create a temporary file on this socket and ask port 80 for the file requested by the client
                        fileobj = c.makefile('w', None)
                        fileobj.write("GET " + message.split()[1].decode("utf-8") + " HTTP/1.0\n\n")
                        fileobj.close()
                        # Read the response into buffer
                        # Fill in start.
                        print('cache complete')
                        fileobj = c.makefile('rb', None)
                        buff = fileobj.readlines()
                        # Fill in end.
                        print('test cache')
                        # Create a new file in the cache for the requested file.
                        # Also send the response in the buffer to client socket and the corresponding file in the cache
                        
                        tmpFile = open("./cache/" + filename, "wb")
                        
                        print('test cache2')
                        # Fill in start.
                        for line in buff:
                            tmpFile.write(line)
                            tcpCliSock.send(line)
                        print('test cache3')
                        # Fill in end.
                        tmpFile.close()
                        c.close()
                except:
                    print ("Illegal request")

        else:
            print("The File is blocked")

            tcpCliSock.close()
            print("socket closed")   
    else:
        ...
        # HTTP response message for file not found
        tcpCliSock.send("HTTP/1.0 404 sendError\r\n")
        tcpCliSock.send("Content-Type:text/html\r\n")
        # Close the client and the server sockets
        tcpCliSock.close()
        print("socket closed")
# Fill in start.
# Fill in end.