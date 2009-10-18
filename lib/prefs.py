import os,sys
dir=os.path.abspath(os.path.dirname(sys.argv[0]))

def loadprefs(klasa):
	f = open (dir+"/prefs.opt","r")
	file=f.readline().rstrip("\n")
	width=f.readline().rstrip("\n")
	height=f.readline().rstrip("\n")
	quality=f.readline().rstrip("\n")
	antialias=f.readline().rstrip("\n")
	antialiasvalue=f.readline().rstrip("\n")
	f.close()
	if file!="":
		klasa.wybor.set_filename(file)
	if width!="":
		klasa.width.set_text(width)
	if height!="":
		klasa.height.set_text(height)
	if quality!="":
		klasa.quality.set_value(float(quality))
	if antialias=="True":
		klasa.antbtn.set_active(1)
		if antialiasvalue!="":
			klasa.antialias.set_value(float(antialiasvalue))

def saveprefs(klasa):	
	if klasa.antbtn.get_active():
		antialias="True"
	else:
		antialias="False"		
	f = open (dir+"/prefs.opt","w")
	f.write(str(klasa.wybor.get_filename())+"\n")
	f.write(str(klasa.width.get_text())+"\n")
	f.write(str(klasa.height.get_text())+"\n")
	f.write(str(klasa.quality.get_value_as_int())+"\n")
	f.write(str(antialias)+"\n")
	f.write(str(klasa.antialias.get_value_as_int())+"\n")
	f.close()	
	
	
