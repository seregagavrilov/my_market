# README 

Simple framework who is allow you meet about wsgi realization of back-end application.

## Getting Started

For install this framework you need to clone this repositori and not forget to meet with exempls.py file.

### Installing

to run the application you need wsgi server implementation - uwsgi

```
pip install uwsgi
```

How to clone repo:

```
git clone https://github.com/seregagavrilov/mywebframework
```
in folder with project you need creat folder names: img - store image files your site
                                                    stylesheets -  store css files
                                                    templates - for store templates your HTML files your site
                                                    
for start your application you should create your application.py file and import need modules
```
from application import run_aplication
```
create your function and call special function for run application
```
def application(environ, start_responce):

    return run_application(environ, statr_responce) 
```
and of course you only need pythone 3

### run uwsgi

for run uwsgi server use this exemple :

```
$ uwsgi --http :9090 --wsgi-file app.py

http - protocol

9090 - port on work your server

app.py - you need write name your script

