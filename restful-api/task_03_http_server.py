#!/usr/bin/python3
"""Develop a simple API using Python with the `http.server` module"""
import http.server
import json


class Handler(http.server.BaseHTTPRequestHandler):
    """Handles GET requests"""

    def _send(self, status, content_type, body):
        """Send a response"""
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.end_headers()
        self.wfile.write(body.encode("utf-8"))

    def do_GET(self):
        """Route GET requests to the right endpoint"""
        if self.path == "/":
            self._send(200, "text/plain", "Hello, this is a simple API!")
        elif self.path == "/data":
            data = {"name": "John", "age": 30, "city": "New York"}
            self._send(200, "application/json", json.dumps(data))
        elif self.path == "/status":
            self._send(200, "text/plain", "OK")
        elif self.path == "/info":
            info = {"version": "1.0",
                    "description": "A simple API built with http.server"}
            self._send(200, "application/json", json.dumps(info))
        else:
            self._send(404, "text/plain", "Endpoint not found")


def run(port=8000):
    """Start server on port 8000"""
    server = http.server.HTTPServer(("", port), Handler)
    server.serve_forever()


if __name__ == "__main__":
    run()
