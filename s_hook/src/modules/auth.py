'''
Created on Jun 18, 2011

@author: konstantin
'''
import __main__
import os

from ConfigParser import ConfigParser

#from configs_loader import config_storage 

from modules.i_controller import Controller


class Auth(Controller):
    '''
    Auth responser
    '''
    
    CONFIG_FILE = os.path.join(os.path.dirname(__main__.__file__),'auth.conf')
    good_ips = []
    bad_ips  = []
    
    def __init__(self,params):
        super(Auth, self).__init__(params)
        
        # Get configs from preloaded storage
        self.good_ips = self.configs_cache['auth.conf']._sections['IP']['good'].split(",")
        self.bad_ips  = self.configs_cache['auth.conf']._sections['IP']['bad'].split(",")
        
        print self.good_ips, self.bad_ips