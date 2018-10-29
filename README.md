# socket-service

e.g. socket systemd service on debian.

It's a echo wall sample app.

## Env

- Debian GNU/Linux 9.5 (stretch)
- python3

## How to use

- Upload files to debian server
  - `tcp_server.py`
  - `systemd/test-tcp-server.service` to Debian's `/usr/lib/systemd/system` folder
- Start with boot
  - `systemctl enable test-tcp-server.service`, create the soft link to `/etc/systemd/system/multi-user.target.wants`
- start the TCP server
  - `systemctl start test-tcp-server.service`
- Before starting `tcp_client.py` to connect the remote server, change the ip address
- start the client at a remote terminal
    - `python3 tcp_client.py` (I use iterm2's `Broadcast Input` function for multi-connections at one time)
- sent some `MSG`, got `MSG, Done!` response

## Log

log file is at `/tmp` named `myapp.log`

## Todo

- [ ] How do I use the Django-orm in this project?
