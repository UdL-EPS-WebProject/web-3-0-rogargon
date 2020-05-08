from http.server import HTTPServer, CGIHTTPRequestHandler


def start_server():
    httpd = HTTPServer(('', 8000), CGIHTTPRequestHandler)
    httpd.serve_forever()


def run_daemon():
    import threading
    daemon = threading.Thread(name='daemon_server', target=start_server)
    daemon.setDaemon(True)
    daemon.start()


if __name__ == "__main__":
    print('Visit http://localhost:8000')
    start_server()
