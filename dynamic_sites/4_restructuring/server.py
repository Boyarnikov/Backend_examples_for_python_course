from http.client import responses
from http.server import BaseHTTPRequestHandler, HTTPServer
from jinja2 import Environment, FileSystemLoader
import os

from common import Handler, Response

hostName = "localhost"
serverPort = 8080

# Set up Jinja2 environment
env = Environment(loader=FileSystemLoader('templates'))


class MyServer(BaseHTTPRequestHandler):
    handlers: list[Handler] = []

    @classmethod
    def add_handler(cls, handler: Handler):
        if cls.handlers:
            cls.handlers[-1].set_next(handler)
        cls.handlers.append(handler)

    @classmethod
    def add_path(cls, path: str):
        def wrapper(func):
            cls.add_handler(Handler(func, path))
            return func
        return wrapper


    def do_GET(self):
        response = None
        print(self.handlers)
        if self.handlers:
            response = self.handlers[0].generate_response(self.path)

        if response is not None:
            self.send_response(response.code)
            for name, value in response.headers.items():
                self.send_header(name, value)
            self.end_headers()
            self.wfile.write(response.body.encode('utf-8'))
            return

        self.send_response(404)
        self.end_headers()


@MyServer.add_path("/style.css")
def get_style() -> Response:
    with open("static/style.css", "r") as file:
        body = file.read()
    response = Response(200, {"Content-type": "text/css"}, body)
    return response


@MyServer.add_path("/")
def get_root() -> Response:
    template = env.get_template('base.html')
    context = {
        'title': 'My Jinja2 Web Page',
        'heading': 'Welcome to My Jinja2 Page',
        'message': 'This page is served using Jinja2 templating.',
        'stylesheet': 'style.css'
    }
    body = template.render(context)

    response = Response(200, {"Content-type": "text/html"}, body)
    return response


@MyServer.add_path("/index")
def get_index() -> Response:
    template = env.get_template('base.html')
    context = {
        'title': 'This is INDEX page',
        'heading': 'HELLO FROM /index',
        'message': 'i was created using new function and @MyServer.add_path.',
        'stylesheet': 'style.css'
    }
    body = template.render(context)

    response = Response(200, {"Content-type": "text/html"}, body)
    return response


print(MyServer.handlers)


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print(f"Server started http://{hostName}:{serverPort}")

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")