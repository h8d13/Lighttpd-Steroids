#!/usr/bin/python
import os
import subprocess
import sys
import zipfile

image = "alpine:latest" 
short_project_uuid = "266749"
pprefix = "sudo"
host_port = "443"
container_port = "443"
zip_file = f"{short_project_uuid}.zip"

def stop_docker():
    subprocess.run(f"{pprefix} docker stop {short_project_uuid}", shell=True)

def start_docker():
    subprocess.run(f"{pprefix} service docker start && {pprefix} docker start {short_project_uuid} && {pprefix} docker attach {short_project_uuid}", shell=True)

def build_custom_image():
    dockerfile_dir = f"./{short_project_uuid}"
    custom_image_name = f"custom-{short_project_uuid}"
    print(f"Building custom Docker image from Dockerfile...")
    result = subprocess.run(f"{pprefix} service docker start && {pprefix} docker build -t {custom_image_name} {dockerfile_dir}", shell=True)
    return custom_image_name if result.returncode == 0 else image

def create_new_container(custom_image):
    print(f"Creating new container from custom image...")
    subprocess.run(f"{pprefix} docker rm {short_project_uuid} 2>/dev/null || true", shell=True)
    subprocess.run(f"{pprefix} docker run -p {host_port}:{container_port} -v ./{short_project_uuid}:/app{short_project_uuid} -it --name {short_project_uuid} {custom_image}", shell=True)

def zip_directory():
    if os.path.exists(f"./{short_project_uuid}"):
        # Create a zip file
        with zipfile.ZipFile(zip_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(f"./{short_project_uuid}"):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, '.')
                    zipf.write(file_path, arcname)
        
        # Set permissions
        subprocess.run(f"chmod 777 {zip_file}", shell=True)
        print(f"Project compressed to {zip_file}")
    else:
        print(f"Error: Directory ./{short_project_uuid} does not exist")

def unzip_archive():
    if os.path.exists(zip_file):
        if os.path.exists(f"./{short_project_uuid}"):
            subprocess.run(f"rm -rf ./{short_project_uuid}", shell=True)
        
        # Extract the zip file
        with zipfile.ZipFile(zip_file, 'r') as zipf:
            zipf.extractall('.')
        
        print(f"Project extracted from {zip_file}")
    else:
        print(f"Error: {zip_file} not found")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "--rebuild":
            custom_image = build_custom_image()
            create_new_container(custom_image)
            print(f"Container ready with web server. Access at https://localhost")
            stop_docker()
        elif sys.argv[1] == "--zip":
            zip_directory()
        elif sys.argv[1] == "--unzip":
            unzip_archive()
        else:
            print("Available commands: --rebuild, --zip, --unzip")
    else:
        start_docker()
        stop_docker()

print("To rebuild with Dockerfile: python3 run.py --rebuild")
print("To zip the project: python3 run.py --zip")
print("To unzip the project: python3 run.py --unzip")
