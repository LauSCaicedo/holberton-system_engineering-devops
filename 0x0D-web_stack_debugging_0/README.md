# Web stack debugging #0
## Background Context

_The Webstack debugging series will train you in the art of debugging. Computers and software rarely work the way we want (that’s the “fun” part of the job!)._

_Being able to debug a webstack is essential for a Full-Stack Software Engineer, and it takes practice to be a master of it._

_In this debugging series, broken/bugged webstacks will be given to you, the final goal is to come up with a Bash script that once executed, will bring the webstack to a working state. But before writing this Bash script, you should figure out what is going on and fix it manually._

_Let’s start with a very simple example. My server must:_

- _have a copy of the /etc/passwd file in /tmp_
- _have a file named /tmp/isworking containing the string OK_
_Let’s pretend that without these 2 elements, my web application cannot work._
