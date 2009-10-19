import threading,events,subprocess,gets,time

class testrunning():
	def __init__(self):
		self.running=True
	def get_running(self):
		return self.running
	def set_running(self,running):
		self.running=running
	
	
def progressbar(progress,var):
	while var.get_running():
		time.sleep(0.1)
		if progress.child!=None:
			progress.child.pulse()
	#var.destroy()

def renderowanie(klasa,options,progress,var):	
	proces = subprocess.Popen("povray "+options+" -D", shell=True,stderr=subprocess.PIPE)
	if gets.getoutput(proces,klasa): 
		events.pictshow(gets.getpicdir(klasa))
	var.set_running(False)
	progress.destroy()

		

def threadinit(klasa,options,progress):
	var=testrunning()
	threading.Thread(target=progressbar,args=(progress,var)).start()
	threading.Thread(target=renderowanie,args=(klasa,options,progress,var)).start()



	 
	 
	 
