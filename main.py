from pysondb import db
import os
import core
server_name = '[CoreDBConnectTEST]'
CLI_prefix = ' :// '
path = os.getcwd()+'\Data'

db = db.getDb(path+'\db.json')

core.initialize()

while True:
	CLI = input(server_name	+ CLI_prefix)
	core.CLIcommands(CLI)