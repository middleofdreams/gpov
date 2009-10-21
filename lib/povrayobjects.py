def camera (klasa):
	klasa.tb.insert_at_cursor("\ncamera{\nlocation<10,10,-10>\nlook_at<0,0,0>}\n ")
	
def light (klasa):
	klasa.tb.insert_at_cursor("\nlight_source{\n<0,20,-20>\ncolor rgb<1,1,1>}\n "	)

def box (klasa):
	klasa.tb.insert_at_cursor("\nbox{\n<0,0,0><3,3,3>\ncolor pigment {rgb<1,1,1>}}\n "	)
	
def sphere (klasa):
	klasa.tb.insert_at_cursor("\nsphere{\n<-3,2,-5>2\ncolor pigment {rgb<0.3,1,0.7>}}\n "	)
	
def sor (klasa):
	klasa.tb.insert_at_cursor("sor{6,\n<0.2,0>,\n<1,1>,\n<0.8,2>,\n<0.3,3>,\n<0.4,4>,\n<1,5>\ncolor pigment {rgb<0.3,1,0.7>}\n translate<1,3,1>}\n "	)
	
def polygon (klasa):
	klasa.tb.insert_at_cursor("polygon {\n7,\n<-2,-2>, <2, -2>, <4, 0>,\n <2, 2>, <-2, 2>, <-4,0>, <-2,-2>\n pigment{color Red} \n translate<-2,0,3> \n}	")

def prism (klasa):
	klasa.tb.insert_at_cursor("prism { \n    linear_sweep\n   linear_spline\n    0, \n    8, \n    6, \n    <3,5>, <-3,5>, <-5,0>, <-3,-5>, <3, -5>, <3,5>\n    pigment{color Green}\n    rotate<0,0,-90>\n  }")

def plane (klasa):
	klasa.tb.insert_at_cursor("plane{\n<0,2,0>,1\n pigment {rgb<0.3,1,0.7>}\n translate<1,-6,1>}\n "	)
	
def lathe (klasa):
	klasa.tb.insert_at_cursor("lathe {\n  linear_spline\n  5,\n  <2, 0>, <3, 0>, <3, 5>, <2, 5>, <2, 0>\n  pigment {Red}\n }	")

def cone (klasa):
	klasa.tb.insert_at_cursor("cone{ \n  <0,0,0>, 5 <0,15,0>, 0\n pigment{color Blue}\n  }"	)
	
