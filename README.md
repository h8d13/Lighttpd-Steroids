# Lighttpd-Steroids
My best attempt at making lighttpd modern again!

---

Prereqs: Docker

### Install instructions

Create a directory for this to live in, for example `mkdir awesomelua`

Download the `run.py` script (in the repo) this contains the docker script to start the container with proper commands (check if you want to modify anything)
Or use commands manually if you're a wizard. 

It also contains configuration:
```
image = "alpine:latest" 
short_project_uuid = "266749"
pprefix = "sudo"
proj_dir = "Projects"
host_port = "443"
container_port = "443"
``` 

Go to the release page and download the tar archive: [1.1 Release](https://github.com/h8d13/Lighttpd-Steroids/releases/tag/1.1)

Extract it: `tar -xvf 266749.tar -C ./yourfolder/266749` or using a file viewer :)

Move to the directory you created using `cd` and just make sure it is as so:
```
/awesomelua
|-- 266749/
|-- run.py
```

If it is like this, good to go you can simply: `sudo python3 run.py`

Then open your browser to `https://localhost` 
> Note: you will get a warning because of self-signed certificate. 
> You normally just accept.

----

### How this project works:

Simple start/rebuild python script. `--rebuild`
`sudo python3 run.py --rebuild`
> This saves enourmous time creating new features or adding system packages / configs.
> ALso should have a proper close mechanism. 

Uses Alpine (5-8Mb) for the core image. 
Dockerfile & start up scripts for init.

Lighttpd conf for custom modules

UTF-8 and HTTPS Built-in 

Finally markdown render using this project from 11 years ago: [luamarkdown](https://github.com/speedata/luamarkdown/tree/master) It contains 1300 lines of code of clever parsing. 

This is passed to smaller CGI-BIN script that sets global css/html styles for all .md content. 
This with added emojis makes it more fun to work with as you can create kind of mini sites quickly and link them together with the convenience of this format over HTML/CSS. 

![Screenshot from 2025-04-04 03-38-08](https://github.com/user-attachments/assets/ce0faedf-46a0-43a5-b071-9e0b36fad881)

