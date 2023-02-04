#!/usr/bin/env python3

from http.server import HTTPServer

from web_cgi import RequestHandler

def print_exception(message):
    '''
    When an exeption is triggered, we have to convert HTML output to normal
    text so we can properly display the stack trace
    '''
    # Import the system module
    import sys

    # Set standar error equal to standard out
    sys.stderr = sys.stdout

    # Set page content type to plain text
    print('Content-Type: text/plain')

    # Print empty space
    print()

    # Print error message from exception
    print('{}'.format(message))

# Set listen port to 8000.
PORT = 8000

# Create the HTTP server object, and for each incoming connect, run the 
# RequestHandler handler. 
server = HTTPServer(('', PORT), RequestHandler)

# Print output to user
print('Starting web server on port {}...'.format(PORT))

# Start the server by wrapping in try/except block
try:
    # Loop forever
    server.serve_forever()
except Exception as e:
    # If an exception is thrown, the reason for the error will be captured
    # in the 'e' variable
    print_exception(e)
