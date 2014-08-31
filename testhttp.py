#!/bin/env python
#!encoding:utf-8
import socket
import urlparse

def url(siteurl,port=80):
	site = urlparse.urlparse(siteurl)
	host = site[1]
	path = site[2]
	client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client_socket.settimeout(0.50)
	server_address = (host, 80)
	client_socket.connect(server_address)
	 
	request_header = 'GET %s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path,host)
	client_socket.send(request_header)
	 
	response = ''
	while True:
	    recv = client_socket.recv(10240)
	    if not recv:
	        break
	    response += recv 
	return response

url('http://nop.pw/')