import threading,subprocess,gets,time,picture

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
	klasa.wTree.get_widget("button1").set_sensitive(0)
	proces = subprocess.Popen("povray "+options+" -D", shell=True,stderr=subprocess.PIPE)
	if gets.getoutput(proces,klasa): 
		time.sleep(0.1)
		picture.pictshow(gets.getpicdir(klasa))
	var.set_running(False)
	progress.destroy()
	time.sleep(0.1)
	klasa.wTree.get_widget("button1").set_sensitive(1)


		

def threadinit(klasa,options,progress):
	var=testrunning()
	threading.Thread(target=progressbar,args=(progress,var)).start()
	threading.Thread(target=renderowanie,args=(klasa,options,progress,var)).start()



	 
	 
	 
