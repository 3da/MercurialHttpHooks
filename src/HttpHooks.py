from mercurial.node import bin, nullid
from mercurial import util

import json
import requests
from mercurial.utils import (
    procutil,
)

import simplejson as json


def hook(ui, repo, hooktype, node=None, **kwargs):
    def warn(message):
        if node:
            ui.warn(message)
    
    def write(message):
        if node:
            ui.write(message)
    
    
    url = ui.config("httphooks", 'url')
    if not url:
        warn('httphooks.url is null')
        return -2
    try:
        changesets=list()
        if node and repo:
            for rev in xrange(repo[node].rev(), len(repo)):
                item = repo[rev]
                change = createCommitInfo(item,2)
                
                changesets.append(change)
        data = {'Commits': changesets,
                'HookType': hooktype,
                'UserName': procutil.getuser()}
        #write('{}\n'.format(json.dumps(data)))
        resp = requests.post(url, json=data)
        #write('{}\n'.format(resp.text))
        result = resp.json()
        if result['success']:
            if result['message']:
                write('{}\n'.format(result['message']))
            return 0
        if result['message']:
            warn('{}\n'.format(result['message']))
            return 1
    except Exception as ee:
        warn('Exception: {}\n'.format(ee))
    return -1


def createCommitInfo(item, depth):
    return {'Message' : item.description().decode('windows-1251'),
                     'Rev' : item.rev(),
                     'Branch' : item.branch(),
                     'Tags' : item.tags(),
                     'Hex' : item.hex(),
                     'User' : item.user(),
                     'MercurialDate' : item.date(),
                     'Files' : item.files(),
                     'Parents' : [createCommitInfo(i,depth-1) for i in item.parents()] if depth>0 else None}