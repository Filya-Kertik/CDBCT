import sys
sys.path.insert(0,'../..')
import core

# WORKSPACE

with open(core.cfg['PATH']['Commands']+'commandspace.cct','r',encoding='utf-8') as f:
	print(f.read())