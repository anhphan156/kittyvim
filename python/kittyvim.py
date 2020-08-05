import vim
import os
import json
import subprocess

sockets = []
socket_name_prefix = 'vimkitty'

def spawn_terminal(options):
    socket_name = '{}-{}'.format(socket_name_prefix, len(sockets))

    # Create socket
    cmd = 'kitty -o {} -o allow_remote_control=yes --listen-on unix:/tmp/{}&'.format(options, socket_name, socket_name)
    os.system(cmd)

    sockets.append(socket_name)

def kill_terminal(sockets, socket_index):
    if(len(sockets) == 0):
        return 0

    socket_name = sockets[int(socket_index)]

    path = '/tmp/{}'.format(socket_name)
    if os.path.exists(path):
        socket_pid = get_terminal_PID(socket_name)

        os.system('kill -9 {}'.format(socket_pid))
        sockets.pop(int(socket_index))

def kill_all_terminal(sockets):
    for i in range(len(sockets)):
        kill_terminal(sockets, 0)

def get_terminal_PID(socket_name):
    p = subprocess.Popen(['kitty', '@', '--to', 'unix:/tmp/{}'.format(socket_name), 'ls'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()

    kitty_window = json.loads(out)
    pid = kitty_window[0]['tabs'][0]['windows'][0]['foreground_processes'][0]['pid']

    return pid

def send_text(socket_name, text):
    path = '/tmp/{}'.format(socket_name)
    if os.path.exists(path):
        p = subprocess.Popen(['kitty', '@', '--to', 'unix:' + path, 'send-text', '{}\n'.format(text)])
