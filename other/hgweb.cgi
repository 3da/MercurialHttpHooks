#!/usr/bin/env python
#
# An example hgweb CGI script, edit as necessary
# See also https://mercurial-scm.org/wiki/PublishingRepositories

# Path to repo or hgweb config to serve (see 'hg help hgweb')
config = "hgweb.config"

# Uncomment and adjust if Mercurial is not installed system-wide
# (consult "installed modules" path from 'hg debuginstall'):
#import sys; sys.path.insert(0, "/path/to/python/lib")

# Uncomment to send python tracebacks to the browser if an error occurs:
#import cgitb; cgitb.enable()

import traceback
import sys
from mercurial import demandimport; demandimport.enable()
from mercurial.hgweb import hgweb, wsgicgi

sys.stderr = sys.stdout

application = hgweb(config)



try:
	wsgicgi.launch(application)
except Exception as ee:
	print "\n\n{}".format(ee)
	#traceback.print_exc()
