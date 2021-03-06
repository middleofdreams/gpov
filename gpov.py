#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys,pygtk,gtk,gtk.glade,gobject,os,locale,subprocess,time,threading
import gtksourceview2
dir=os.path.abspath(os.path.dirname(sys.argv[0]))
import lib
from lib.gpovbuffer import CodeBuffer
#--------KLASA GLOWNA-----------#

class gpov:
	def __init__(self):

# sparsowanie glade, polaczenie sygnalow  i inne standardowe dzialania
	
		self.gladefile = dir+"/gpov.glade"
		self.wTree = gtk.glade.XML(self.gladefile) 
		# pobieramy główne okno
		self.window = self.wTree.get_widget("window1")
		self.window.show()
		#skroty klawiszowe:
		self.window.connect("key_press_event", lib.keys.key_event,self)
		if (self.window):
			self.window.connect("destroy",gtk.main_quit)
		
		#pobranie obiektow z glade			
		self.antbtn = self.wTree.get_widget("checkbutton1")
		self.antialias = self.wTree.get_widget("spinbutton1")
		self.quality = self.wTree.get_widget("spinbutton2")
		self.wybor = self.wTree.get_widget("filechooserbutton1")
		self.height= self.wTree.get_widget("entry2")
		self.width = self.wTree.get_widget("entry1")
		self.edytor=gtksourceview2.View(gtksourceview2.Buffer())
		self.wTree.get_widget("scrolledwindow1").add(self.edytor)
		#self.edytor=self.wTree.get_widget("edytor")
		self.outt=self.wTree.get_widget("textview1")
		#modyfikacja buffera edytora - dla undo i redo
		#self.edytor.set_buffer(gtksourceview2.gtksourcebuffer())
		
		#pobranie bufferow edytora i outputu
		self.tb=self.edytor.get_buffer()
		self.tb2=self.outt.get_buffer()
		
		#sygnaly:
		dic={
		"on_button1_clicked": self.execute,
		"zamknij": gtk.main_quit,
		"toggle" : self.antialiastoggle,
		"edytuj" : self.edytuj,
		"save_file" : self.save,
		"on_file_loaded" : self.file_load,
		"newfile" : self.newfile}
	
		self.wTree.signal_autoconnect(dic)
		
		#numerowanie lini w edytorze:
		self.edytor.set_border_window_size(gtk.TEXT_WINDOW_LEFT, 30)
		self.edytor.connect("expose_event", self.edytorexpose_event)
		
		#filtr dla wyboru plikow
		filter = gtk.FileFilter()
		filter.set_name("Pliki .pov")
		filter.add_pattern("*.pov")
		self.wybor.add_filter(filter)
		self.wybor.set_filter(filter)
		#pobranie ostatnich ustawien
		lib.prefs.loadprefs(self)
		self.editorvisible=False
		self.tb.set_modified(False)
		dic ={"camera" : self.camera,
		"light" : self.light,
		"box"	: self.box,
		"sphere"	: self.sphere,
		"sor"	: self.sor,
		"polygon" :self.polygon,
		"prism" :self.prism,
		"cone" :self.cone,
		"plane" :self.plane,
		"lathe":self.lathe }
		self.wTree.signal_autoconnect(dic)
	
	
	def setfile(self):
		#time.sleep(1)
		while self.wybor.get_filename()==None:
			self.wybor.set_filename(self.filename)
	
	def newfile(self,widget):
		dlgbuttons=(gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL, gtk.STOCK_SAVE, gtk.RESPONSE_OK)
		self.filechooser=gtk.FileChooserDialog(title="Wybierz nazwe pliku", parent=None, action=gtk.FILE_CHOOSER_ACTION_SAVE, buttons=dlgbuttons, backend=None)
		
		if self.filechooser.run() == gtk.RESPONSE_OK:
			self.filename = self.filechooser.get_filename()
			self.filechooser.destroy()
			db = open(self.filename,"w")
			db.write("#include \"colors.inc\"\n")
			db.close()
			self.wybor.unselect_all()
			threading.Thread(target=self.setfile,args=()).start()	
			lib.events.editortoggle(self,self.filename)
	
	def file_load(self,widget):
		if self.editorvisible:
			lib.events.show_editor(self)
		
	def execute(self,widget):
		lib.prefs.saveprefs(self)
		lib.events.renderuj(self)
		
	def save(self,widget):
			lib.events.save_file(self)
			self.tb.set_modified(False)

	def edytuj(self,widget):
		lib.events.editortoggle(self)

		
	def antialiastoggle(self,widget):
		if self.antbtn.get_active():
			self.wTree.get_widget("spinbutton1").set_sensitive(1)			
		else:
			self.wTree.get_widget("spinbutton1").set_sensitive(0)
			
	def edytorexpose_event(self,widget, event):
		lib.numbering.line_numbers_expose(widget,event,self)
		if self.tb.get_modified():
			self.wTree.get_widget("button4").set_sensitive(1)
		else: 
			self.wTree.get_widget("button4").set_sensitive(0)
	def camera(self,widget): lib.povrayobjects.camera(self)
	def light(self,widget): lib.povrayobjects.light(self)
	def box(self,widget): lib.povrayobjects.box(self)
	def sphere(self,widget): lib.povrayobjects.sphere(self)
	def sor(self,widget): lib.povrayobjects.sor(self)
	def polygon(self,widget): lib.povrayobjects.polygon(self)
	def prism(self,widget): lib.povrayobjects.prism(self)
	def cone(self,widget): lib.povrayobjects.cone(self)
	def plane(self,widget): lib.povrayobjects.plane(self)
	def lathe(self,widget): lib.povrayobjects.lathe(self)
# wywołanie aplikacji
if __name__ == "__main__":
	gtk.gdk.threads_init()
	gl=gpov()
	gtk.main()	
