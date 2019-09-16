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

git_commit = input("enter commit comment: ")

subprocess.run(["git","add" , "."])
subprocess.run(["git","commit", "-m", "" + git_commit + ""])
subprocess.run(["git","push"])





    