import sys
sys.path.insert(0,'../..')
import core

# WORKSPACE

func_name = input(core.cfg['NAMESPACE']['ServerName'] + 'name new command --> ')
func_desk = input(core.cfg['NAMESPACE']['ServerName'] + 'description command --> ')

commandspace=[]
with open(core.cfg['PATH']['Commands']+'commandspace.cct','r',encoding='utf-8') as d:
		for line in d:
			commandspace.append(line.split('-')[0].replace('\n', '').replace(' ', ''))
		if func_name in commandspace:
			print(core.cfg['NAMESPACE']['ServerName'],'command not duplecate')
		else:
			with open(core.cfg['PATH']['Commands']+'commandspace.cct','a') as space:
				space.write('\n'+func_name.replace(' ','').lower() + ' - ' + func_desk)

			with open(core.cfg['PATH']['Commands']+'commandsprite.cct','a') as sprite:
				sample=[]
				firstUp = func_name.title()
				sample.append(firstUp)

				twolow = func_name.lower()
				sample.append(twolow)

				allup = func_name.upper()
				sample.append(allup)

				sprite.write('\n'+str(sample).replace('[','').replace(']','').replace("'",'').replace(' ',''))

			with open(core.cfg['PATH']['Scripts']+func_name.lower()+'.py','w') as pyfile:
				pyfile.write("""import sys
sys.path.insert(0,'../..')
import core

# WORKSPACE
		"""
							)
	
close = print(core.cfg['NAMESPACE']['ServerName']+' '+'command -create finished')