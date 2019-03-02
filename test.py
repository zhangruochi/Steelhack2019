import time
from http.server import HTTPServer
from http.server import SimpleHTTPRequestHandler
from http.server import BaseHTTPRequestHandler 


class MyHttpHandler(BaseHTTPRequestHandler):     
    def do_GET(self):     
         # Send response status code
        self.send_response(200)
 
        # Send headers
        self.send_header('Content-type','text/html')
        self.end_headers()
 
        # Send message back to client
        message = "Hello world!"
        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))

        return
        
    def do_POST(self):
        self.send_response(200)
 
        # Send headers
        self.send_header('Content-type','text/html')
        self.end_headers()
 
        # Send message back to client
        message = "Hello world!"
        with open("test.txt") as f:
            f.write("hello world!")
        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))

        return
        


HOST_NAME = '192.52.165.203'
PORT_NUMBER = 9000

if __name__ == '__main__':
    httpd = HTTPServer((HOST_NAME, PORT_NUMBER), MyHttpHandler)
    print(time.asctime(), 'Server UP - %s:%s' % (HOST_NAME, PORT_NUMBER))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass

    httpd.server_close()
    print(time.asctime(), 'Server DOWN - %s:%s' % (HOST_NAME, PORT_NUMBER))