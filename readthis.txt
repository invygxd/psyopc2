# psyopc2
c2 for keylogs, shots, cmds. http-based, stealthy.

# run
- python3, pip install requests keyboard pillow
- vm for client (win10/kali)
- server: `python server.py`
- client: `python client.py` (vm)
- ui: open websnipe.html, put client_id, get data or send cmds

# does
- server: takes client data, sends cmds
- client: sends keys (k.txt), shots (s.png), runs cmds
- ui: pulls client data, pushes cmds

# notes
- lab only. no real-world bs.
- tweak client sleep, add more cmds
- runs on localhost:8000
