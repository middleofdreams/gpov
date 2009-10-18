import gtk
def get_lines(first_y, last_y, buffer_coords, numbers,self):
	text_view = self.edytor

	iter, top = text_view.get_line_at_y(first_y)

	count = 0
	size = 0
	while not iter.is_end():
		y, height = text_view.get_line_yrange(iter)
		buffer_coords.append(y)
		line_num = iter.get_line()
		numbers.append(line_num)
		count += 1
		if (y + height) >= last_y:
			break
		iter.forward_line()
	return count
	
def line_numbers_expose(widget, event, self):
	text_view = widget
	left_win = text_view.get_window(gtk.TEXT_WINDOW_LEFT)
	right_win = text_view.get_window(gtk.TEXT_WINDOW_RIGHT)
	if event.window == left_win:
		type = gtk.TEXT_WINDOW_LEFT
		target = left_win
	elif event.window == right_win:
		type = gtk.TEXT_WINDOW_RIGHT
		target = right_win
	else:
		return False
	first_y = event.area.y
	last_y = first_y + event.area.height
	x, first_y = text_view.window_to_buffer_coords(type, 0, first_y)
	x, last_y = text_view.window_to_buffer_coords(type, 0, last_y)      
	numbers = []
	pixels = []
	count = get_lines(first_y, last_y, pixels, numbers, self)
	layout = widget.create_pango_layout("")
	for i in range(count):
		x, pos = text_view.buffer_to_window_coords(type, 0, pixels[i])
		numbers[i]=numbers[i]+1
		str = "%d" % numbers[i]
		layout.set_text(str)
		widget.style.paint_layout(target, widget.state, False, None, widget, None, 2, pos + 2, layout)
	return False
