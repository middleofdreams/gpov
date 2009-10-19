import os,sys,gtk,subprocess,gets,time,render
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
		
	
	
def picthide(widget):
		widget.get_parent_window().hide()

def pictshow(image):
	okno=gtk.Window()
	okno.set_position(gtk.WIN_POS_CENTER)
	box=gtk.VBox()
	box2=gtk.HBox()
	okno.set_title("Wyrenderowany obraz:")
	lay=gtk.Layout()
	przycisk=gtk.Button(stock=gtk.STOCK_CLOSE)
	box2.pack_start(lay,True,True,0)
	box2.pack_start(przycisk,False,False,1)
	obraz=gtk.Image()
	pict=gtk.gdk.pixbuf_new_from_file(image)
	
##################################################################
## sprawdzanie czy rozmiar jest wiekszy od ekranu + skalowanie	##
#################### wydzielic do funkcji! #######################
##################################################################

	wys=pict.get_height()
	szer=pict.get_width()
	maxheight=gtk.gdk.screen_height()-200
	maxwidth=gtk.gdk.screen_width()-240
	if szer>maxwidth or wys>maxheight:
		
		roznicawys=wys-maxheight
		roznicaszer=szer-maxwidth
		procentszer=1-float(roznicaszer*100/szer)*0.01
		procentwys=1-float(roznicawys*100/wys)*0.01
		if procentwys>procentszer:
			procent=procentszer
		else:
			procent=procentwys
		szer=int(szer*procent)
		wys=int(wys*procent)
		print wys
		print szer
		obraz.set_from_pixbuf(pict.scale_simple(szer,wys,gtk.gdk.INTERP_BILINEAR))
	else:
		obraz.set_from_pixbuf(pict)
	box.pack_start(obraz,False,False,0)
	box.pack_start(box2,False,False,1)
	box2.show()
	przycisk.show()
	lay.show()
	okno.add(box)
	box.show()
	przycisk.connect("clicked",picthide)
	obraz.show()
	okno.show()

def renderuj(klasa):
	if klasa.wybor.get_filename()==None:
		errorwindow(klasa)
	else:	
		win=showprogress()
		options=gets.getcmdoptions(klasa)
		render.threadinit(klasa,options,win)
			

	

		
