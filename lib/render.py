import threading,events,subprocess,gets,time

def progressbar(progress):
	while progress !=None:
		time.sleep(0.1)
		progress.pulse()

def renderowanie(klasa,options,progress):	
		proces = subprocess.Popen("povray "+options+" -D", shell=True,stderr=subprocess.PIPE)
		if gets.getoutput(proces,klasa): 
			events.pictshow(gets.getpicdir(klasa))
		
		progress.destroy()

		

def threadinit(klasa,options,progress):
	threading.Thread(target=progressbar,args=(progress)).start()
	threading.Thread(target=renderowanie,args=(klasa,options,progress)).start()



	 
	 
	 
