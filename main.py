from http.server import HTTPServer, CGIHTTPRequestHandler
import threading
from rdflib import Graph

def start_server():
    httpd = HTTPServer(('', 8000), CGIHTTPRequestHandler)
    httpd.serve_forever()

daemon = threading.Thread(name='daemon_server', target=start_server)
daemon.setDaemon(True)
daemon.start()

g = Graph()
g.parse('http://localhost:8000', format='html')

print(str(g.serialize(format='turtle')).replace('\\n', '\n'))
print('\nExtracted triples count: ' + str(len(g)))

assert len(g) > 10, 'The document should include at least 10 triples'