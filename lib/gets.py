import os,sys,gtk,gobject
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
			for i in stdout_value.splitlines():
				if "Line: " in i:
					linenumber= int(i.split(" ")[4])
					#klasa.tb.remove_all_tags(klasa.tb.get_start_iter(),  klasa.tb.get_end_iter())
					start=klasa.tb.get_iter_at_line(linenumber-1)
					end=klasa.tb.get_iter_at_line(linenumber)		
					klasa.tb.show_error(start,end)
					end_mark = klasa.tb.create_mark(
						"end_mark", end, False);
					klasa.edytor.scroll_to_mark(end_mark,0,False,)
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
	

