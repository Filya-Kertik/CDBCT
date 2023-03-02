from pysondb import db
import os
import core

core.create_cfg()
core.initialize()

db = db.getDb(core.cfg['PATH']['Data']+'\db.json')

while True:
	try:
		CLI = input(core.cfg['NAMESPACE']['ServerName'] +' '+ core.cfg['NAMESPACE']['cli']+' ')
		core.CLIcommands(CLI)
	except Exception as e:
		print('[ERROR] ','Core error')
		print(e)