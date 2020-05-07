from rdflib import Graph

def start_server():
    from http.server import HTTPServer, CGIHTTPRequestHandler
    httpd = HTTPServer(('', 8000), CGIHTTPRequestHandler)
    httpd.serve_forever()

def run_daemon():
  import threading
  daemon = threading.Thread(name='daemon_server', target=start_server)
  daemon.setDaemon(True)
  daemon.start()

def parse_html():
  g = Graph()
  g.parse('http://localhost:8000', format='html')
  return g

def print_graph(g):
  import re
  output = str(g.serialize(format='turtle')).replace('b\'', '').replace('\\n', '\n')
  output = re.sub(r'(?m)^\@prefix.*\n?', '', output) 
  print(output)
  print('\nExtracted triples count: ' + str(len(g)))

def at_least_10_triples():
  run_daemon()
  g = parse_html()
  print_graph(g)
  assert len(g) > 10, 'The document should include at least 10 triples'

if __name__ == "__main__":
    print('Run HTTP Server on port 8000')
    start_server()
