from typing import Callable


class Response:
    body: str
    headers: dict
    code: int

    def __init__(self, code, header, body):
        self.body = body
        self.headers = header
        self.code = code


class Handler:
    _next_handler = None
    _render: Callable[[], Response]
    _path: str

    def __init__(self, render_func: Callable[[], Response], path: str):
        self._render = render_func
        self._path = path

    def set_next(self, handler: "Handler"):
        self._next_handler = handler

    def generate_response(self, path: str) -> Response|None:
        print(f"Trying {path} with handler {self._path}")
        if path == self._path:
            return self._render()
        if self._next_handler:
            return self._next_handler.generate_response(path)
        return None


