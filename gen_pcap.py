import os
import sys
import re
import subprocess

template = """flow default tcp example.com:44123 > baidu.com:80 (tcp.initialize;);
default > (content:"GET {URL} HTTP/1.1\x0d\x0aHost:baidu.com\x0d\x0aUser-Agent: DogBot\x0d\x0a\x0d\x0a";);
default < (content:"HTTP/1.1 200 OK\x0d\x0aContent-Length: 26\x0d\x0a\x0d\x0aWelcome to Google.com!\x0d\x0a\x0d\x0a";);"""

def gen_fs(url):
    fs = template.format(URL=url)
    with open('test.fs' ,'w') as f:
        f.write(fs)
        
        
def compile_fs():
    cmd = "flowsynth test.fs -f pcap -w test.pcap -d --display json"
    print subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE).stdout.read()
    
if __name__ == "__main__":
    gen_fs('/index.php')
    compile_fs()