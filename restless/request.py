#! /usr/bin/env python
import requests
import uuid
import json

headers = {'Content-type': 'application/json',
                   'Accept': 'text/plain'}

requests.post("%s/v1/fractal" % "http://localhost",
              json.dumps({'uuid':str(uuid.uuid4()),'username':'test'}),headers=headers)

