from pysondb import db
import os
server_name = '[CoreDBConnectTEST]'
CLI_prefix = ' :// '
path = os.getcwd()+'\Data'

def initialize():
	global exitSprite
	commandspace=[]
	with open(path+'\CDBCT\commandspace.CDBCT','r') as d:
		for line in d:
			commandspace.append(line)
	with open(path+'\CDBCT\CommandSprite.CDBCT','r') as f:
		for line in f:
			lineQuer = line.partition(':')
			if lineQuer[0] in commandspace:
				exitSprite = lineQuer[2].split(',')


def CLIcommands(cli_str):
	global exitSprite
	if cli_str in exitSprite:
			print(server_name +' server shutdown')
			os._exit(0)
