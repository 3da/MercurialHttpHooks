from mercurial.node import bin, nullid
from mercurial import util

import json
import requests
from mercurial.utils import (
    procutil,
)


def hook(ui, repo, hooktype, node, **kwargs):
    url = ui.config("httphooks", 'url')
    if not url:
        ui.warn('httphooks.url is null')
        return -2
    try:
        changesets=list()
        for rev in xrange(repo[node].rev(), len(repo)):
            item = repo[rev]
            change = createCommitInfo(item,2)
            
            changesets.append(change)
        data = {'Commits': changesets,
                'HookType': hooktype,
               'UserName': procutil.getuser()}
        resp = requests.post(url, json=data)
        result = resp.json()
        
        if result['success']:
            if result['message']:
                ui.write('{}\n'.format(result['message']))
            return 0
        if result['message']:
            ui.warn('{}\n'.format(result['message']))
            return 1
    except Exception as ee:
        ui.warn('{}'.format(ee))
    return -1


def createCommitInfo(item, depth):
    return {'Message' : item.description(),
                     'Rev' : item.rev(),
                     'Branch' : item.branch(),
                     'Tags' : item.tags(),
                     'Hex' : item.hex(),
                     'User' : item.user(),
                     'MercurialDate' : item.date(),
                     'Files' : item.files(),
                     'Parents' : [createCommitInfo(i,depth-1) for i in item.parents()] if depth>0 else None}