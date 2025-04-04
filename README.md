# Lighttpd-Steroids
My best attempt at making lighttpd modern again!

---

Prereqs: Docker

### Install instructions

Create a directory for this to live in, for example `mkdir awesomelua`

Download the run.py script this contains the docker script to start the container with proper commands (check if you want to modify anything)
Or use commands manually if you're a wizard. 

Go to the release page and download the tar archive:

[1.1 Release](https://github.com/h8d13/Lighttpd-Steroids/releases/tag/1.1)

Extract it: `tar -xvf 266749.tar -C ./yourfolder/266749` or using a file viewer :)

Move to the directory you created and just make sure it is so:
```
/awesomelua
\-- run.py
\-- 266749/
```

Good to go you can simply: `sudo python3 run.py`

----

### How this project works:

Simple start/rebuild python script.
`sudo python3 run.py --rebuild`

Uses Alpine (5-8Mb) for the core image. 
Dockerfile & start up scripts for init.

Lighttpd conf for custom modules

UTF-8 and HTTPS Built-in 

Finally markdown render using this project from 11 years ago: [luamarkdown](https://github.com/speedata/luamarkdown/tree/master) It contains 1300 lines of code of clever parsing. This is passed to smaller script that sets global styles for all .md content. 





