#! /usr/bin/env python

import requests
import uuid
import json

headers = {'Content-type': 'application/json',
                   'Accept': 'text/plain'}


# add a item
#requests.post("%s/v1/fractal" % "http://localhost:5000",
#              json.dumps({'uuid':str(uuid.uuid4()),'username':'test2'}),headers=headers)


# update a item
#requests.put("%s/v1/fractal/%s" % ("http://localhost:5000",'f0e3480e-60f9-42e9-9769-cd7dd62dd138'),
#              json.dumps({'username':'test3'}),headers=headers)

# delete a item
#requests.delete("%s/v1/fractal/%s" % ("http://localhost:5000",'f0e3480e-60f9-42e9-9769-cd7dd62dd138'),
#                 headers=headers)

# get a item
#result = requests.get("%s/v1/fractal/%s" % ("http://localhost:5000",'a2746f2b-c905-4389-a8e0-e758749f0b35'),
#                 headers=headers)

#if result.status_code == 200:
#    print result.text
