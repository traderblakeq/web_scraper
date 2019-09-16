import subprocess
import requests as reqs
import os

url = 'https://kea.dk/'
response = reqs.get(url)
response.encoding = 'utf-8'
print_str = response.text

print(response.text)
file = open('kea.html','a+')
file.write(print_str)
file.close()

subprocess.run(["git","add" , "."])
subprocess.run(["git","commit", "-m", "\"First commit\""])
subprocess.run(["git","push"])





    