import os,sys,gtk,subprocess,gets,time,render,picture
dir=os.path.abspath(os.path.dirname(sys.argv[0]))

def showprogress():
	okno=gtk.Window(gtk.WINDOW_TOPLEVEL)
	okno.set_keep_above(True)
	okno.set_decorated(False)
	okno.show()
	okno.resize(400,100)
	okno.set_decorated(False)
	okno.set_position(gtk.WIN_POS_CENTER_ALWAYS)
	progress=gtk.ProgressBar()
	progress.set_text("Trwa renderowanie")
	okno.add(progress)
	progress.show()
	return okno
					
def show_editor(klasa):
	klasa.edytor.show()
	klasa.wTree.get_widget("button4").show()
	klasa.wTree.get_widget("hboxx").show()
	klasa.wTree.get_widget("hbox3").show()
	f=open(klasa.wybor.get_filename(),'r')
	klasa.edytor.set_sensitive(False)
	klasa.tb.begin_not_undoable_action()
	buff = klasa.edytor.get_buffer()
	buff.set_text(f.read())
	buff.set_modified(False)
	klasa.edytor.set_sensitive(True)	
	klasa.tb.end_not_undoable_action()
	f.close()
	klasa.window.move(gtk.gdk.screen_width()/4, gtk.gdk.screen_height()/6)

def hide_editor(klasa,*widget):
	klasa.edytor.hide()
	klasa.wTree.get_widget("button4").hide()
	klasa.wTree.get_widget("hboxx").hide()
	klasa.wTree.get_widget("hbox3").hide()
	klasa.window.resize(230,230)
	
def save_file(klasa,*widget):
	buff = klasa.edytor.get_buffer()
	klasa.edytor.set_sensitive(False)
	text = buff.get_text(buff.get_start_iter(), buff.get_end_iter())
	klasa.edytor.set_sensitive(True)
	buff.set_modified(False)
	# set the contents of the file to the text from the buffer
	fout = open(klasa.wybor.get_filename(), "w")
	fout.write(text)
	fout.close()

def errorwindow(klasa, *widget):
	klasa.response = klasa.wTree.get_widget("messagedialog1").run() 
	if klasa.response == gtk.RESPONSE_DELETE_EVENT or klasa.response == gtk.RESPONSE_CANCEL:
		klasa.wTree.get_widget("messagedialog1").hide()	
		
	
	

def renderuj(klasa):
	if klasa.wybor.get_filename()==None:
		errorwindow(klasa)
	else:	
		win=showprogress()
		options=gets.getcmdoptions(klasa)
		render.threadinit(klasa,options,win)
			

	

		
