#!/usr/bin/env python3

import cgi
import cgitb
cgitb.enable()

from http.server import HTTPServer, CGIHTTPRequestHandler

def print_exception():
    import sys
    sys.stderr = sys.stdout
    print('Content-Type: text/plain')
    print()
    print('I AM AN EXCEPTION!')

def main_page(request):
    # Main page of the web application
    content = '''
    <html>
    <head>
    <body>
    <h1>Welcome to the web application</h1>
    </body>
    </head>
    </html>
    '''
    return content.encode('utf-8')

def result_page(request):
    # The result page of the web application
    form = cgi.FieldStorage(fp=request.rfile, headers=request.headers, environ={'REQUEST_METHOD': 'POST'})
    name = form.getvalue('name')
    content = '''
    <html>
    <head>
    <body>
        <h1>Hello, {}!</h1>
    </body>
    </head>
    </html>
    '''.format(cgi.escape(name))
    return content.encode('utf-8')

# Define the handler for the CGIHTTPRequestHandler
class RequestHandler(CGIHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(main_page(self))
        else:
            CGIHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        if self.path == '/result':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(result_page(self))
        else:
            CGIHTTPRequestHandler.do_POST(self)



PORT = 8000

# form = cgi.FieldStorage()
# user = form.getfirst('user', '').upper()
# print('hi')
server = HTTPServer(('', PORT), RequestHandler)
print('Starting web server on port {}...'.format(PORT))
server.serve_forever()


