# Lighttpd-Steroids
Light httpd is a lightweight C server. It's both light but also fast. With a bit of lua scripting we can also enable more fun stuff: 

---

Prereqs: Docker

### Install instructions

Create a directory for this to live in, for example `mkdir awesomeclua`

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
Or use the `.zip` in the repo. 

Extract it: 

`$ tar -xvf 266749.tar -C ./yourfolder/266749` or using a file viewer :)

Move to the directory you created using `cd` and just make sure it is as so:
```
/awesomeclua
|-- 266749/
|-- run.py
```

**If you directory looks like that^ you're good to go!**

`$ sudo python3 run.py`

Then open your browser to `https://localhost` 
> Note: you will get a warning because of self-signed certificate. 
> You normally just accept.

----

### How this project works:

Simple start/rebuild python script using `--rebuild` arg. 
`sudo python3 run.py --rebuild`

> This saves enourmous time creating new features or adding system packages / configs.
> Also both should have a proper close mechanism which makes it convenient as it detects `exit`  

Uses Alpine (5-8Mb) for the core image. 
Dockerfile & start up scripts for init.

Lighttpd conf for custom modules

UTF-8 and HTTPS Built-in 

Finally markdown render using this project from 11 years ago: [luamarkdown](https://github.com/speedata/luamarkdown/tree/master) It contains 1300 lines of code of clever parsing. 

This is passed to smaller CGI-BIN script that sets global css/html styles for all .md content. 
This with added emojis makes it more fun to work with as you can create kind of mini sites quickly and link them together with the convenience of this format over HTML/CSS. 

![Screenshot from 2025-04-04 03-38-08](https://github.com/user-attachments/assets/ce0faedf-46a0-43a5-b071-9e0b36fad881)

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

----

You can also edit from an IDE directly, you might run into perms issues use `chown` and/or `chmod`.

How the build script works:
```
def stop_docker():
    command = f"{pprefix} docker stop {short_project_uuid}"
    subprocess.run(command, shell=True)

def start_docker():
    command = f"{pprefix} service docker start && {pprefix} docker start {short_project_uuid} && {pprefix} docker attach {short_project_uuid}"
    subprocess.run(command, shell=True)

def build_custom_image():
    dockerfile_dir = f"./{proj_dir}/{short_project_uuid}"
    custom_image_name = f"custom-{short_project_uuid}"
    print(f"Building custom Docker image from Dockerfile...")
    command = f"{pprefix} service docker start && {pprefix} docker build -t {custom_image_name} {dockerfile_dir}"
    result = subprocess.run(command, shell=True)
    if result.returncode == 0:
        print(f"Successfully built custom image: {custom_image_name}")
        return custom_image_name
    else:
        print(f"Failed to build custom image. Using original image: {image}")
        return image

def create_new_container(custom_image):
    print(f"Creating new container from custom image...")
    command = f"{pprefix} docker rm {short_project_uuid} 2>/dev/null || true"
    subprocess.run(command, shell=True)
    command = f"{pprefix} docker run -p {host_port}:{container_port} -v ./{proj_dir}/{short_project_uuid}:/app{short_project_uuid} -it --name {short_project_uuid} {custom_image}"
    subprocess.run(command, shell=True)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--rebuild":
        custom_image = build_custom_image()
        create_new_container(custom_image)
        print(f"Container ready with web server. Access at httpS://localhost:{host_port}")
        print(f"Make changes to ./{proj_dir}/{short_project_uuid}/index.html to see live updates")
        print(f"To start the container again, run: python3 run.py")
        stop_docker()
    else:
        start_docker()
        stop_docker()

print("To rebuild with Dockerfile (including web server): python3 run.py --rebuild")

```

Just a whole lot of scripting to properly close/rm a docker container, then rebuild/run. 


