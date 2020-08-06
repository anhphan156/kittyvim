# kittyvim
Plugin allows vim to send text to a [kitty terminal](https://sw.kovidgoyal.net/kitty/)
<br/>
![kittyvim](https://i.imgur.com/PzjrtFi.gif)

## Installation
Install vim with python3 support and [kitty terminal](https://sw.kovidgoyal.net/kitty/)

### [Vundle](https://github.com/VundleVim/Vundle.vim)

`Plugin 'anhphan156/kittyvim'` 

## Usage
`:KittyvimSpawn` to spawn a new terminal<br/>
`:KittyvimKillFirst` to kill the first terminal in the list<br/>
`:KittyvimKillAll` to kill all the terminals<br/>
`:KittyvimPrompt` to prompt for a text to be sent<br/>
`:KittyvimRun('text')` to send a text <br/>
