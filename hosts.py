#!/usr/bin/python
from docker import Client
import json,traceback,commands

hostMaps={
	'localhost':'127.0.0.1',
	'localhost2':'127.0.0.1',
}

class DockerManager:
	def __init__(self):
		self.cli = Client(base_url='unix://var/run/docker.sock')
		self.events = self.cli.events()

	def run(self):
		while True:
			message = self.events.next()
			try:
				self.handler(json.loads(message))
			except Exception, e:
				traceback.print_exc()
			
	def handler(self,message):
		if not message.has_key('status'):
			return

		# ipdb.set_trace()

		status = message['status']
		actor = message['Actor']

		if u'start'==status:
			print 'on cteate'
			self.on_connect(actor)
		 	
		elif u'stop'==status:
			print 'on destroy'
			self.on_disconnect(actor)

	def on_connect(self,actor):
		containerID = actor['ID']
		containerName = actor['Attributes']['name']

		containerIP = self.getIpById(containerID)

		if not containerIP:
			print 'containerIP can not find'
			# print actor
			return

		self.add_host(containerName,containerIP)

		self.write_host()
		self.restartDns()

	def on_disconnect(self,actor):
		containerID = actor['ID']
		containerName = actor['Attributes']['name']

		# containerIP = self.getIpById(containerID)
		# containerName,containerIP = self.getIpNameById(containerID)

		self.remove_host(containerName)
		self.write_host()

	def getIpById(self,containerID):
		m = self.cli.containers(filters={'id':containerID})
		# print containerID,m
		if not m:
			# print containerID,m
			return False

		return m[0]['NetworkSettings']['Networks']['bridge']['IPAddress']

	def write_host(self):
		content = ''
		for h,i in hostMaps.items():
			content = ''.join([content,i,'    ',h,'\n'])
		
		fd = open('/etc/hosts','w')
		fd.write(content)
		fd.close()

	def add_host(self,name,ip):
		print 'add host ',name,ip
		hostMaps[name]=ip
		print hostMaps

	def remove_host(self,name):
		if hostMaps.has_key(name):
			print 'remove host ',name
			del hostMaps[name]
			print hostMaps

	def restartDns(self):
		startDns='dnsmasq -q -8 /tmp/dnsmasq.log --port 53 -R -u root'
		stopDns='kill $(cat /var/run/dnsmasq.pid)'

		commands.getstatusoutput(stopDns)
		commands.getstatusoutput(startDns)

if __name__=='__main__':
	dm = DockerManager()
	dm.run()
