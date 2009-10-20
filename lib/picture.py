import gtk
def picthide(widget):
		widget.get_parent_window().hide()

def pictresize(pict):
	height=pict.get_height()
	width=pict.get_width()
	maxheight=gtk.gdk.screen_height()*0.8
	maxwidth=gtk.gdk.screen_width()*0.8
	if width>maxwidth or height>maxheight:
		
		height_diff=height-maxheight
		width_diff=width-maxwidth
		height_percent=1-float(height_diff*100/height)*0.01
		width_percent=1-float(width_diff*100/width)*0.01
		if height_percent>width_percent:
			scale=width_percent
		else:
			scale=height_percent
		height=int(height*scale)
		width=int(width*scale)
		newpict=gtk.image_new_from_pixbuf(pict.scale_simple(width,height,gtk.gdk.INTERP_BILINEAR))
	else:
		newpict=gtk.image_new_from_pixbuf(pict)
	return newpict
	
def pictshow(image):
	
	okno=gtk.Window()
	okno.set_position(gtk.WIN_POS_CENTER)
	box=gtk.VBox()
	box2=gtk.HBox()
	okno.set_title("Wyrenderowany obraz:")
	lay=gtk.Layout()
	button=gtk.Button(stock=gtk.STOCK_CLOSE)
	box2.pack_start(lay,True,True,0)
	box2.pack_start(button,False,False,1)
	
	pict=gtk.gdk.pixbuf_new_from_file(image)
	
	generatedpicture=pictresize(pict)
	
	box.pack_start(generatedpicture,False,False,0)
	box.pack_start(box2,False,False,1)
	box2.show()
	button.show()
	lay.show()
	okno.add(box)
	box.show()
	button.connect("clicked",picthide)
	generatedpicture.show()
	okno.show()
