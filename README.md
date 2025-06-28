# Lighttpd-Steroids
Light httpd is a lightweight C server. It's both light but also fast. With a bit of lua scripting we can also enable more fun stuff: 

---

Prereqs: Docker, Linux host system

### Install instructions

Create a directory for this to live in, for example `mkdir awesomeclua`

Download the `run.py` script (in the repo) this contains the docker script to start the container with proper commands (check if you want to modify anything)
Or use commands manually if you're a wizard. 

It also contains configuration:

```
image = "alpine:latest" 
short_project_uuid = "266749"
host_port = "8443"
container_port = "443"
``` 

Go to the release page and download the ZIP archive: [1.1 Release](https://github.com/h8d13/Lighttpd-Steroids/releases/tag/1.1)

Extract it: 

`$ sudo python3 run.py --unzip`

Move to the directory you created using `cd` and just make sure it is as so:
```
/awesomeclua
|-- 266749/
|-- run.py
```

**If you directory looks like that^ you're good to go!**

`$ sudo python3 run.py`

This will simply run/attach the container with specified settings: If it's your first use use: `--rebuild` 

Then open your browser to `https://localhost`
> Note: you will get a warning because of self-signed certificate. 
> You normally just accept press advanced > accept.

----

### How this project works:

Simple start/rebuild python script using `--rebuild` arg. 
`sudo python3 run.py --rebuild`

> This saves enourmous time creating new features or adding system packages / configs.
> Also both should have a proper close mechanism which makes it convenient as it detects `exit`  

## Features 

Uses Alpine (5-8Mb) for the core image. 
Dockerfile & start up scripts for init.

Lighttpd conf for custom modules

UTF-8 and HTTPS Built-in 

**Finally markdown render using this project from 11 years ago:**

[luamarkdown](https://github.com/speedata/luamarkdown/tree/master) It contains 1300 lines of code of clever parsing. (Also the same year this paper was published: [Why K2_OS](https://www.yecl.org/publications/lin2014asplos.pdf)

This is passed to smaller CGI-BIN script that sets global css/html styles for all .md content. 
This with added emojis makes it more fun to work with as you can create kind of mini sites quickly and link them together with the convenience of this format over HTML/CSS. 

----

From there I created two directories:
```
/tree
|-- .hid/
|---- sources/
|---- static/
|-- intro.md

/protected
|-- hello.md
```
Username/password for `/protected` is set in dockerfile. 
> File listing is automatic of these dirs (hides "." files in tree so it's less clutered.

What is cool is you can simply create a new .md file and directly see it, link it, etc or even a folder and an index.html and it's up and running.

### Previews

![Screenshot from 2025-04-05 14-40-36](https://github.com/user-attachments/assets/24b8b39d-e65a-43a9-b3d8-6adf36af3dee)
![Screenshot from 2025-04-05 14-40-29](https://github.com/user-attachments/assets/8ab45c79-d68a-43ee-90e0-d7215062cda8)
![Screenshot from 2025-04-05 14-40-18](https://github.com/user-attachments/assets/65330b7e-f4d2-47de-86ad-124207b9dcf5)


----

### Make it your own. 

You can also edit from an IDE directly, you might run into perms issues use `chown` and/or `chmod`.

Just a whole lot of scripting to properly close/rm a docker container, then rebuild/run. 
And the same for Ziping/Unzip which makes it convenient to save current state/ future releases. 
