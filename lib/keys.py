import gtk,events

def key_event(widget, event, klasa):
	if event.type == gtk.gdk.KEY_PRESS:
		if event.state==gtk.gdk.CONTROL_MASK:
			if gtk.gdk.keyval_name(event.keyval)== 's' :
				events.save_file(klasa)
			elif gtk.gdk.keyval_name(event.keyval)== 'r':
				klasa.execute(klasa)
			elif gtk.gdk.keyval_name(event.keyval)== 'q':
				gtk.main_quit(klasa)
			elif gtk.gdk.keyval_name(event.keyval)== 'z':
				klasa.tb.undo()
			elif gtk.gdk.keyval_name(event.keyval)== 'y':
				klasa.tb.redo()
