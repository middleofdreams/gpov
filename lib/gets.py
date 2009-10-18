import os,sys
dir=os.path.abspath(os.path.dirname(sys.argv[0]))

def getpicdir(klasa):
	obrazek=klasa.wybor.get_filename().rstrip("pov")
	obrazek=obrazek.split(klasa.wybor.get_current_folder())[1]
	obrazek=obrazek+"png"
	obrazek=dir+obrazek
	return obrazek


def getoutput(proces,klasa):	
	pid=proces.wait()
	if pid==0:
		stdout_value = proces.communicate()[1]
		klasa.tb2.insert(klasa.tb2.get_end_iter(), str(stdout_value))
		klasa.tb2.create_mark("kam",klasa.tb2.get_end_iter(),False)
		klasa.outt.scroll_to_mark(klasa.tb2.get_mark("kam"),0,False)
		if "parse error" in stdout_value.lower():
			klasa.tb2.insert(klasa.tb2.get_end_iter(), "\n\nParse Error")
			klasa.tb2.create_mark("kam",klasa.tb2.get_end_iter(),False)
			klasa.outt.scroll_to_mark(klasa.tb2.get_mark("kam"),0,False)
			return False
		else:
			klasa.tb2.insert(klasa.tb2.get_end_iter(), "\n\n")
			klasa.tb2.create_mark("kam",klasa.tb2.get_end_iter(),False)
			klasa.outt.scroll_to_mark(klasa.tb2.get_mark("kam"),0,False)
			return True
				
				
def getcmdoptions(klasa):
	options=" "+str(klasa.wybor.get_filename())
	options=options+" +Q"+str(klasa.quality.get_value_as_int())
	if klasa.antbtn.get_active():
		options=options+" +A0."+str(klasa.antialias.get_value_as_int())
	options=options+" +H"+str(klasa.height.get_text())
	options=options+" +W"+str(klasa.width.get_text())+" "
	return options
	

