from http.server import BaseHTTPRequestHandler, HTTPServer
from jinja2 import Environment, FileSystemLoader
import os

hostName = "localhost"
serverPort = 8080

# Set up Jinja2 environment
env = Environment(loader=FileSystemLoader('templates'))


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/style.css':
            self.send_response(200)
            self.send_header("Content-type", "text/css")
            self.end_headers()
            with open("static/style.css", "rb") as file:
                self.wfile.write(file.read())
            return
        if self.path == '/':
            title = 'This page is served using Jinja2 templating'
            style = 'style.css'
            header = 'My Jinja2 Web Page'
            body = 'Welcome to My Jinja2 Page'

            site = f"""
                <!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>{ title }</title>
                    <link rel="stylesheet" href="{ style }">
                </head>
                <body>
                    <h1>{ header }</h1>
                    <p>{ body }</p>
                </body>
                </html>
            """

            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(site.encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()


class MyServerJinja(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/style.css':
            self.send_response(200)
            self.send_header("Content-type", "text/css")
            self.end_headers()
            with open("static/style.css", "rb") as file:
                self.wfile.write(file.read())
            return
        if self.path == '/':
            template = env.get_template('base.html')
            context = {
                'title': 'My Jinja2 Web Page',
                'heading': 'Welcome to My Jinja2 Page',
                'message': 'This page is served using Jinja2 templating.',
                'stylesheet': 'style.css'
            }
            rendered_template = template.render(context)

            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(rendered_template.encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print(f"Server started http://{hostName}:{serverPort}")

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")