!/bin/sh
wget https://github.com/h8d13/Lighttpd-Steroids/releases/download/1.3/266749.zip
sleep 1
python3 run.py --unzip
echo "You can now use: doas python3 run.py --rebuild"
