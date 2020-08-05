if !has('python3')
    echo 'Compile Vim with +python3 in order to run kittyvim'
    finish
endif

"if exists('g:kittyvim')
    "finish
"endif
"let g:kittyvim = 1


function! kittyvim#version()
	return '1.0.0'
endfunction

let s:plugin_root_dir = fnamemodify(resolve(expand('<sfile>:p')), ':h')

function! kittyvim#run()
python3 << EOF
import sys
from os.path import normpath, join
import vim

plugin_root_dir = vim.eval('s:plugin_root_dir')
python_root_dir = normpath(join(plugin_root_dir, '..', 'python'))
sys.path.insert(0, python_root_dir)
import kittyvim

EOF

let g:kittyvim_run_terminal_index = 0

endfunction

function! kittyvim#spawn()
python3 << EOF
kittyvim.spawn_terminal('initial_window_height=400')
EOF
endfunction

function! kittyvim#kill(socket_index)
python3 << EOF
kittyvim.kill_terminal(kittyvim.sockets, vim.eval('a:socket_index'))
EOF
endfunction

function! kittyvim#killall()
python3 << EOF
kittyvim.kill_all_terminal(kittyvim.sockets)
EOF
endfunction

function! kittyvim#sendtext(terminal_index, text)
python3 << EOF
if len(kittyvim.sockets) > 0:
	socket_index = int(vim.eval('a:terminal_index'))
	socket_name = kittyvim.sockets[socket_index]
	kittyvim.send_text(kittyvim.sockets, socket_name, vim.eval('a:text'))
else:
	print('No active terminal')
EOF
endfunction

function! kittyvim#promptcommand(...)
let command = a:0 == 1 ? a:1 : ""
let l:command = input("Command? ", command)
call kittyvim#sendtext(g:kittyvim_run_terminal_index, l:command)
endfunction

call kittyvim#run()

command! KittyvimVersion call kittyvim#version()
command! KittyvimSpawn call kittyvim#spawn()
command! KittyvimKillFirst call kittyvim#kill(0)
command! KittyvimKillAll call kittyvim#killall()
command! -nargs=? KittyvimPrompt :call kittyvim#promptcommand(<args>)
command! -nargs=* KittyvimRun :call kittyvim#sendtext(g:kittyvim_run_terminal_index, <args>)
