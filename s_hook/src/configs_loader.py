'''
Created on Jun 18, 2011

@author: konstantin
'''
import os
from ConfigParser import ConfigParser

class Singleton(object):
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls,*args, **kw)
        return cls._instance    

class ConfigLoader(Singleton):
    
    cache = {}
    path = None

    def __init__(self, path=None):
        if not path is None:
            self.path =  path
#        print "PATH: ",self.path
            

    def load(self):
        folder = os.listdir(self.path)
        for c in folder:
            if c.endswith('.conf'):
                print "Loading %s" % c
                config = ConfigParser()
                config.read(os.path.join(self.path, c))
                self.cache[c] = config
