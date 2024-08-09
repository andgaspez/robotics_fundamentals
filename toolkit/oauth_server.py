import http.server
import socketserver
import urllib.parse

# Execute this script. If succesful, it will retrieve a 'Serving at port 8080' response.

PORT = 8080

class OAuthHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Parse the query parameters
        query_components = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
        code = query_components.get('code')
        
        if code:
            print(f"Authorization code received: {code[0]}")
            # Here you would exchange the code for a token
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Authorization successful. You can close this window.")
        else:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"Missing authorization code.")

# Set up the HTTP server
with socketserver.TCPServer(("", PORT), OAuthHandler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()

# Create CLIENT_ID and REDIRECT_URL=http://localhost:8080/callback in https://dev.mendeley.com/myapps.html
# It is assumed that you already got your CLIENT_ID and REDIRECT_URL values.
# https://api.mendeley.com/oauth/authorize?client_id=YOUR_CLIENT_ID&response_type=code&redirect_uri=YOUR_REDIRECT_URI&scope=all
# Execute the previous line on a web browser after executing this script
# If it was succesful, you will get an 'Authorization successful. You can close this window.' on the web browser
# In CLI you will get an Authorization code received value.

