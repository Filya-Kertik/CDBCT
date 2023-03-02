from pysondb import db
import os
import runpy as patch
import configparser

def initialize():
	global commandspace,commandsprite
	commandspace=[]
	commandsprite=[]
	with open(cfg['PATH']['Commands']+'commandspace.cct','r',encoding='utf-8') as d:
		for line in d:
			commandspace.append(line.split('-')[0].replace('\n', '').replace(' ', ''))
	with open(cfg['PATH']['Commands']+'commandsprite.cct','r') as f:
		for line in f:
			query = line.split(',')
			for sample in query:
				commandsprite.append(sample.replace('\n', '').replace(' ', ''))

def CLIcommands(cli_str):
	global commandsprite
	if cli_str in commandsprite:
		try:
			patch.run_path(cfg['PATH']['Scripts']+cli_str.lower()+'.py')
		except Exception as e:
			print(cfg['NAMESPACE']['ServerName'] + ' command not worked please check '+cfg['PATH']['Scripts']+cli_str+'.py')
			print('[ERROR] -'+cli_str + ' return error')
			print(e)
	else:
		print(cfg['NAMESPACE']['ServerName'] + ' this command was not found in the list of commands write -help to find out all existing commands')

def create_cfg():
	if os.path.exists(os.getcwd()+'/data/'+'settings.ini'):
		global cfg
		cfg = configparser.ConfigParser()
		cfg.sections()
		cfg.read(os.getcwd()+chr(92)+'data'+chr(92)+'settings.ini')
		print(cfg['NAMESPACE']['ServerName'],'config loaded')
	else:
		print('[CoreDBConnectTEST]','create config...')
		conf = open(os.getcwd()+'/data/'+'settings.ini','w',encoding='utf-8')
		cfg = configparser.ConfigParser()
		cfg['NAMESPACE']={'CLI':'://',
						  'ServerName':'[CoreDBConnectTEST]'
						}
		cfg['PATH']={'Data':os.getcwd()+chr(92)+'data'+chr(92),
					 'Scripts':os.getcwd()+chr(92)+'data'+chr(92)+'scripts'+chr(92),
					 'Commands':os.getcwd()+chr(92)+'data'+chr(92)+'ctt'+chr(92),
					 'Main':os.getcwd()
					}
		cfg.write(conf)
		conf.close()
		print('[CoreDBConnectTEST]','config created')
