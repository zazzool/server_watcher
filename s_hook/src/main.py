'''
Created on Jun 18, 2011

@author: konstantin
'''
import sys, os
import cherrypy

from help import startup_help
#from configs_loader import ConfigLoader
from responser import Responser

def _main_(argv):
    # Show startup help
    startup_help()
    
    # Check configure file in ARGV dict
    conf_file = "server.conf"
    if len(argv) > 1:
        conf_file = argv[0]
        
    conf = os.path.join(os.path.dirname(__file__), conf_file)
    
    # Loading configs
#    c = ConfigLoader(os.path.dirname(__file__))
#    c.load()
    
    # Run CherryPy server
    print ("Server running...")
    
    try:
        cherrypy.quickstart(Responser(), config=conf)
    except:
        # Ooops! We have error...
        print (sys.exc_info())
        sys.exit()

if __name__ == '__main__':
    _main_(sys.argv)