from http.server import BaseHTTPRequestHandler, HTTPServer
import random

HTML = html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple Web Server</title>
</head>
<body>
    <h1>Hello, World!</h1>
    <p>This is served from a simple HTTP server. {}</p>
</body>
</html>
"""


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(HTML.format(random.random()), "utf-8")
    )


if __name__ == "__main__":
    hostname = "localhost"
    port = 8000

    webServer = HTTPServer((hostname, port), MyServer)
    print(f"Server started http://{hostname}:{port}")

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")