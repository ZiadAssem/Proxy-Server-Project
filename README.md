# Project Description
This Python-based HTTP proxy server receives incoming connections on a designated port
and receives HTTP request messages from clients. If the requested URL is not on a list of blocked URLs
, the server will first check if the requested file is stored in the cache directory. 
If it is found in the cache, it is immediately sent to the client. If the file is not in the cache, 
the server establishes a connection with the host specified in the request message and sends an HTTP request for the file.
The response is then stored in the cache and sent to the client. In the event that an error occurs while trying to retrieve the file,
an HTTP error message will be sent to the client.
# Dependencies
The project Will run without Making any pip install
# How To use
Open the Tirnmenal and write the following command:

py Networks_Project.py 127.0.0.1 

This command will active your Proxy server
