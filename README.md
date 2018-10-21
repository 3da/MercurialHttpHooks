# MercurialHttpHooks

## Install
1. Install library 'requests' (`pip install requests`)
2. Copy HttpHooks.py to your python lib directory.
For example: C:\Python27\Lib\site-packages\hgext
3. Add `pretxnchangegroup` hook to your hgrc file and specify API url as described below.

### Exmple config

Add to your .hg\hgrc file
```
[hooks]
pretxnchangegroup.HttpHooks = python:hgext.HttpHooks.hook

[httphooks]
url = http://localhost:36884/api/
```
