import vim
import os
import json
import subprocess

sockets = []
socket_name_prefix = 'vimkitty'

def spawn_terminal(options):
    num_sockets = len(sockets)
    socket_name = '{}-{}'.format(socket_name_prefix, num_sockets)

    another_num_sockets = 0 # to fix naming collision

    while(os.path.exists('/tmp/' + socket_name)):
        another_num_sockets += 1
        socket_name = socket_name_prefix + '-' + str(num_sockets) + '-' + str(another_num_sockets)

    # Create socket
    cmd = 'kitty -o {} -o allow_remote_control=yes --listen-on unix:/tmp/{}&'.format(options, socket_name, socket_name)
    os.system(cmd)

    sockets.append(socket_name)

def kill_terminal(sockets, socket_index):
    if(len(sockets) == 0):
        return 0

    socket_name = sockets[int(socket_index)]

    path = '/tmp/{}'.format(socket_name)

    sockets.pop(int(socket_index))

    if os.path.exists(path):
        socket_pid = get_terminal_PID(socket_name)

        os.system('kill -9 {}'.format(socket_pid))
    else:
        kill_terminal(sockets, socket_index)

def kill_all_terminal(sockets):
    for i in range(len(sockets)):
        kill_terminal(sockets, 0)

def get_terminal_PID(socket_name):
    p = subprocess.Popen(['kitty', '@', '--to', 'unix:/tmp/{}'.format(socket_name), 'ls'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()

    kitty_window = json.loads(out)
    pid = kitty_window[0]['tabs'][0]['windows'][0]['foreground_processes'][0]['pid']

    return pid

def send_text(sockets, socket_name, text):
    if len(sockets) == 0:
        print('No active terminal')
    path = '/tmp/{}'.format(socket_name)
    if os.path.exists(path):
        p = subprocess.Popen(['kitty', '@', '--to', 'unix:' + path, 'send-text', '{}\n'.format(text)])
    else:
        sockets = [x for x in sockets if x != socket_name]
        socket_name = sockets[0]
        send_text(sockets, socket_name, text)
