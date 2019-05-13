ninja2
======

jinja2 command line client v 0.2

Dependencies
------------
* [Python 2](http://python.org/) (required)
* [jinja2](http://jinja.pocoo.org/docs/dev/) (required)
* [Pyyaml](http://pyyaml.org/) (optional)

Usage
-----

```
$ ninja2 -h
usage: ninja2 [-h] [-V] (-e | -j | -y) [-l {i18n,do,loopcontrols}] template.j2

read a jinja2 template from file and values from stdin either environment or json or yaml

positional arguments:
  template.j2           File with Jinja2 template

optional arguments:
  -h, --help            show this help message and exit
  -V, --version         show program's version number and exit
  -e, --env             render from environment
  -j, --json            render from json file
  -y, --yaml            render from yaml file
  -l {i18n,do,loopcontrols}, --load {i18n,do,loopcontrols}
                        load Jinja2 extentions, can be repeated

  (c) 2015 Sascha Spreitzer, MIT License
```

Render from environment
-----------------------
```
sspreitzer@s900x3c:~/git/ninja2⟫ cat test.j2 
{{ USER }}
sspreitzer@s900x3c:~/git/ninja2⟫ ./ninja2 -e test.j2 
sspreitzer
```

Render from json
----------------
```
sspreitzer@s900x3c:~/git/ninja2⟫ cat test.json 
{ "USER": "json-user" }
sspreitzer@s900x3c:~/git/ninja2⟫ ./ninja2 -j test.j2 < test.json
json-user
```

Render from yaml
----------------
Pyyaml must be installed
```
sspreitzer@s900x3c:~/git/ninja2⟫ cat test.yaml 
---
USER: yaml-user
sspreitzer@s900x3c:~/git/ninja2⟫ ./ninja2 -y test.j2 < test.yaml
yaml-user
```

Render from environment with all extentions loaded
-----------------------
```
sspreitzer@s900x3c:~/git/ninja2⟫ cat test.j2 
{{ USER }}
sspreitzer@s900x3c:~/git/ninja2⟫ ./ninja2 -e -l do -l i18n -l loopcontrols test.j2 
sspreitzer
```
