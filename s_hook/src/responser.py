'''
Created on Jun 18, 2011

@author: konstantin
'''
import os
import json
import cherrypy

from modules.auth import Auth
from configs_loader import ConfigLoader

class Responser(object):
    
    # Main page
    def index(self, **kwargs):
        cherrypy.response.headers['Content-Type'] = ' application/json'
        return json.dumps(Auth(kwargs).done())
    index.exposed = True
    
    # Reload configs
    def reload(self):
        c = ConfigLoader()
        c.load()
        return "reloaded"
    reload.exposed = True
    
    # Default page dummy
    def default(self):
        print cherrypy.request.show_tracebacks
        return "Fuck off, ebany hacker!"
    default.exposed = True