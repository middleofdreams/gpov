def kamera (klasa):
	klasa.tb.insert(klasa.tb.get_end_iter(), "\ncamera{\nlocation<10,10,-10>\nlook_at<0,0,0>}\n "	)
	klasa.tb.create_mark("kam",klasa.tb.get_end_iter(),False)
	klasa.edytor.scroll_to_mark(klasa.tb.get_mark("kam"),0,False)
	
def swiatlo (klasa):
	klasa.tb.insert(klasa.tb.get_end_iter(), "\nlight_source{\n<0,20,-20>\ncolor rgb<1,1,1>}\n "	)
	klasa.tb.create_mark("kam",klasa.tb.get_end_iter(),False)
	klasa.edytor.scroll_to_mark(klasa.tb.get_mark("kam"),0,False)
def box (klasa):
	klasa.tb.insert(klasa.tb.get_end_iter(), "\nbox{\n<0,0,0><3,3,3>\ncolor pigment {rgb<1,1,1>}}\n "	)
	klasa.tb.create_mark("kam",klasa.tb.get_end_iter(),False)
	klasa.edytor.scroll_to_mark(klasa.tb.get_mark("kam"),0,False)

def kula (klasa):
	klasa.tb.insert(klasa.tb.get_end_iter(), "\nsphere{\n<-3,2,-5>2\ncolor pigment {rgb<0.3,1,0.7>}}\n "	)
	klasa.tb.create_mark("kam",klasa.tb.get_end_iter(),False)
	klasa.edytor.scroll_to_mark(klasa.tb.get_mark("kam"),0,False)
	
def obrotowy (klasa):
	klasa.tb.insert(klasa.tb.get_end_iter(), "sor{6,\n<0.2,0>,\n<1,1>,\n<0.8,2>,\n<0.3,3>,\n<0.4,4>,\n<1,5>\ncolor pigment {rgb<0.3,1,0.7>}\n translate<1,3,1>}\n "	)
	klasa.tb.create_mark("kam",klasa.tb.get_end_iter(),False)
	klasa.edytor.scroll_to_mark(klasa.tb.get_mark("kam"),0,False)
		
	
