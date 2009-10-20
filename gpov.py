#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys,pygtk,gtk,gtk.glade,gobject,os,locale,subprocess,time
dir=os.path.abspath(os.path.dirname(sys.argv[0]))
import lib

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
		self.edytor=self.wTree.get_widget("edytor")
		self.outt=self.wTree.get_widget("textview1")
		#modyfikacja buffera edytora - dla undo i redo
		self.edytor.set_buffer(lib.undobuffer.UndoableBuffer())
		
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
		"on_file_loaded" : self.file_load}
	
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
		dic ={"kamera" : self.kamera,
		"swiatlo" : self.swiatlo,
		"box"	: self.box,
		"kula"	: self.kula,
		"wielokat"	: self.obrotowy}
		self.wTree.signal_autoconnect(dic)
	
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
		if self.wybor.get_filename()==None:
			self.errorwindow(self)
		else:
			if self.editorvisible:
				lib.events.hide_editor(self)
				self.editorvisible=False
				
			else: 
				lib.events.show_editor(self)
				self.editorvisible=True

		
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
	def kamera(self,widget): lib.povrayobjects.kamera(self)
	def swiatlo(self,widget): lib.povrayobjects.swiatlo(self)
	def box(self,widget): lib.povrayobjects.box(self)
	def kula(self,widget): lib.povrayobjects.kula(self)
	def obrotowy(self,widget): lib.povrayobjects.wielokat(self)


		
# wywołanie aplikacji
if __name__ == "__main__":
	gtk.gdk.threads_init()
	gl=gpov()
	gtk.main()	
