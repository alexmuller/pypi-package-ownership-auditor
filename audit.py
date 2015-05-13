try:
    import xmlrpclib
except ImportError:
    import xmlrpc.client as xmlrpclib

from itertools import groupby

import pprint
import sys
import time

client = xmlrpclib.ServerProxy('https://pypi.python.org/pypi')

if len(sys.argv) > 1:
    monitored_packages = sys.argv[1].split(',')
else:
    print "Please supply a list of packages when executing the command"
    exit()

for package in monitored_packages:
    print "== {0} ==".format(package)

    users = client.package_roles(package)

    for role, name_list in groupby(sorted(users), lambda x: x[0]):
        names = ', '.join(list(x[1] for x in name_list))
        print "{0}: {1}".format(role, names)

    print ""
    time.sleep(1)
