import yaml
import random
import string

def rand():
	chars = string.ascii_uppercase + string.digits
	return ''.join(random.SystemRandom().choice(chars) for _ in range(32))

class Config:
	def __init__(self):
		self.distconfig = self.loadyaml("config.dist.yaml")
		try:
			self.userconfig = self.loadyaml("config.yaml")
		except:
			self.create_default_local_config()
			self.userconfig = self.loadyaml("config.yaml")

	def loadyaml(self, filename):
		with open(filename, "rb") as fp:
			string = fp.read()
			return yaml.load(string)		

	def create_default_local_config(self):
		def_user   = "default"
		def_passwd = rand()
		
		with open("config.yaml", "wb") as fp:
			fp.write('# This file was autogenerated\n\n' + 
				'backend_user: "' + def_user + '"\n' + 
				'backend_pass: "' + def_passwd + '"\n')

	def get(self, key):
		if key in self.userconfig:
			return self.userconfig[key]
		if key in self.distconfig:
			return self.distconfig[key]
		else:
			raise Exception("Option \""+ key +"\" not found in config")

config = Config()

