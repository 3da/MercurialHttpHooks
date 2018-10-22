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
incoming.HttpHooks = python:hgext.HttpHooks.hook
txnclose.HttpHooks = python:hgext.HttpHooks.hook

[httphooks]
url = http://localhost:36884/api/
```

### Example request
```
{
  "UserName": "IUSR",
  "Commits": [
    {
      "Message": "Performance improvements",
      "Rev": 790,
      "Tags": [
        "tip"
      ],
      "Hex": "c3ae4169983c55cc46b2ce06655d056fc82201e8",
      "User": "John Doe",
      "MercurialDate": [
        1540059873.0,
        -10800.0
      ],
      "Branch": "Release",
      "Parents": [
        {
          "Message": "Small fix",
          "Rev": 789,
          "Tags": [],
          "Hex": "cb5c943930314b3e2bb70c96efe5a350a51214d9",
          "User": "John Doe",
          "MercurialDate": [
            1540058889.0,
            -10800.0
          ],
          "Branch": "default",
          "Parents": null,
          "Files": [
            "src/Main.c"
          ]
        }
      ],
      "Files": [
        "src/HelloWorld.cs"
      ]
    }
  ]
}
```


### Example response
```
{
  "Success": false,
  "Message": "Wrong commit name. Please write ticket number"
}
```
