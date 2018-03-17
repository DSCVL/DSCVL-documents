# python frontend of the LiDAR ROS software
from appJar import gui
import tkinter 
from os import *
from rplidar import RPLidar



class Screen:

	def __init__(self):
	#	self.height = height
	#	self.width = width
		
		self.app = gui("DEPTH SENSING WITH COMPUTER VISION AND LYDAR", "800x600")
		#self.app.seltitle("LiDARWeb")
		# background color of the window
		self.app.setBg("Lightblue")
		self.app.setFont(16)	

	@property
	def counterlogin(self):
		self.app.startLabelFrame("Login infos")
		# these only affect the labelFrame
		self.app.setSticky("we")
		self.app.setPadding([50,50]) 

		self.app.addLabel("l1", "Username", 0, 0,1)
		user = self.app.addEntry("Username", 0, 1, 1)
		self.app.addLabel("l2", "Password", 1, 0,1)
		pwd = self.app.addLabelSecretEntry("Password", 1, 1)
		self.app.addButtons(["Submit", "Cancel"], None,2,0,2)
		self.app.stopLabelFrame()
		self.app.go()
	
	@classmethod 
	def change_resolution(cls, height, width):

		cls.height = height
		cls.width = width




class Interaction(Screen):

	
	
	def __init__(self):
		super().__init__()

		self.app.setBg("Lightgreen")
		self.app.setFont(16)
		self.tools = ["REFRESH", "HOME", "CLOSE", "SAVE",
         "PRINT", "SEARCH",  "HELP"]
		
		
		
		
	@property
	def tool(self):
		self.app.startLabelFrame("Interactive Tools")
	#	self.tbFunc = press(self)
		self.app.setPadding([20,20]) 
	#	self.app.addToolbar(self.tools,self.tbFunc, findIcon=True)
		self.app.addLabel("l1", "Raduis", 0, 0,4)
		self.app.addEntry("radius", 0, 1,4)
		self.app.addLabel("l2", "Angle", 1, 0,4)
		self.app.addEntry("Angle", 1, 1,4)
		self.app.addCheckBox("Speed", 2, 0,1)
		self.app.addCheckBox("Opacity", 2, 1,1)
		self.app.addCheckBox("Brightness", 2, 2, 1)
		self.app.addCheckBox("contrast", 2, 3,1)
		self.app.addButtons(["Submit", "Delete"],None,3,0,2 )
		self.app.addStatusbar(fields=3)
		self.app.setStatusbar("Radius: 2 cm", 0)
		self.app.setStatusbar("Speed: 30MHZ", 1)
		self.app.setStatusbar("angle: 45°", 2)
		self.app.stopLabelFrame()
		self.app.go()
		
	# handle button events
	@staticmethod		
	def press(self,button):

		if self.button == "Cancel":
		
			Screen.app.stop()
			Screen.counterlogin.app.startLabelFrame.hide()
		else:
			Screen.counterlogin.app.startLabelFrame.hide()	


welcome = Screen()
print(welcome.counterlogin)
 
interact = Interaction()
print(interact.tool)





#user_credentials = welcome.press()
#print(user_credentials)