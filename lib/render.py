import threading,events,subprocess,gets,time

class watek(threading.Thread):
	
	 
	 def __init__ (self,klasa,options,progress):
		threading.Thread.__init__(self)
		self.klasa=klasa
		self.options=options
		self.progress=progress
		self.running=True
		threading.Thread(target=self.renderowanie,args=()).start()
		threading.Thread(target=self.progressbar,args=()).start()
			
	 def renderowanie(self):	
		proces = subprocess.Popen("povray "+self.options+" -D", shell=True,stderr=subprocess.PIPE)
		if gets.getoutput(proces,self.klasa): 
			events.pictshow(gets.getpicdir(self.klasa))
		self.running=False
		self.progress.hide()
		
	 def progressbar(self):
		while self.running:
			time.sleep(0.1)
			self.progress.get_children()[0].pulse()
