#!/usr/bin/env python3

from http.server import HTTPServer

from cgi import RequestHandler

def print_exception(message):
    import sys
    sys.stderr = sys.stdout
    print('Content-Type: text/plain')
    print()
    print('{}'.format(message))

PORT = 8000
server = HTTPServer(('', PORT), RequestHandler)
print('Starting web server on port {}...'.format(PORT))
try:
    server.serve_forever()
except Exception as e:
    print_exception(e)
