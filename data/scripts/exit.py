import sys
sys.path.insert(0,'../..')
import core

# WORKSPACE

import os

print(core.cfg['NAMESPACE']['ServerName'],'server shotdown')
os._exit(0)