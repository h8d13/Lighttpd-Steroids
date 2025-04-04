#!/usr/bin/python
import uuid
import os
import datetime
import subprocess
import sys

image = "alpine:latest" 
short_project_uuid = "266749"
pprefix = "sudo"
host_port = "443"
container_port = "443"

## Helper to properly close
def stop_docker():
    command = f"{pprefix} docker stop {short_project_uuid}"
    subprocess.run(command, shell=True)

def start_docker():
    command = f"{pprefix} service docker start && {pprefix} docker start {short_project_uuid} && {pprefix} docker attach {short_project_uuid}"
    subprocess.run(command, shell=True)

def build_custom_image():
    dockerfile_dir = f"./{short_project_uuid}"
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
    command = f"{pprefix} docker run -p {host_port}:{container_port} -v ./{short_project_uuid}:/app{short_project_uuid} -it --name {short_project_uuid} {custom_image}"
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
