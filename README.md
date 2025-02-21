# Embeded Status Page
## _A simple, low resource, webserver for embedded systems_
Full feature Webservers are typically too expensive to run on a embedded system. 
It is preferable to be able to just hit a simple webpage to see status of your system instead of ssh etc.
This was my solution
## Features
Interesting feature that I added is that the server will try to bind to localhost at port 4321. If that socket is already bound it will try 4322 and the 4333 and so on.
## Tech
This is built in python and ueses the following libraries:
http.server
and
socketserver
## Installation
Just download and run with python, and it should work.
