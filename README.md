# kittyvim
Plugin allows vim to send text to a kitty terminal
<br/>
![kittyvim](https://i.imgur.com/PzjrtFi.gif)

## Installation
Install vim with python3 support and kitty terminal

### [Vundle](https://github.com/VundleVim/Vundle.vim)

`Plugin 'anhphan156/kittyvim'` 

## Usage
`:KittyvimSpawn` to spawn a new kitty terminal
`:KittyvimKillFirst` to kill the first terminal in the list
`:KittyvimKillAll` to kill all the terminals
`:KittyvimPrompt` to prompt for a text to be sent
`:KittyvimRun('text')` to send a text 
