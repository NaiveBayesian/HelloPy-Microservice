# Much of the code below is taken shamelessly from https://daanlenaerts.com/blog/2015/06/03/create-a-simple-http-server-with-python-3/
from http.server import BaseHTTPRequestHandler, HTTPServer

# HTTPRequestHandler class
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):

    # GET
    def do_GET(self):
        # Send response status code
        self.send_response(200)

        # Send headers
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # Send message back to client
        message = "Hello world!"
        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))
        return

# Define the global 'run' function for our server
def run(port):
    print(f"Starting server on port {port}...")

    #Server settings
    server_address = ('127.0.0.1', port)
    httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
    print("Running server...")
    httpd.serve_forever()


# Now run our new server!
run(8081)