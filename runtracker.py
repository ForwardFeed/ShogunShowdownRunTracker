#!/usr/bin/python3
import time
import os.path
import base64
import json
import datetime



def SSRunTracker:
	def __init__(self, directory):
		self.filename=directory+"RunSaveData.dat"
		self.prev_room=0
		self.boss=[0, 0, 0]
		self.boss_beat_room=[3,6,10]
		self.current_boss=0
		
		try:
		    self.last_modified=os.path.getmtime(self.filename)
		except:
		    print("cannot find or access :%s" % filename)
		    if os.path.exists(directory+"SaveData.dat"):
		        print("please launch the game and just click new game, and this script should work")
		    else:
		        print("doesn't sound like the right directory to me")
		    quit()
	
	def reset(self):
		self.boss=[0, 0, 0]
		self.current_boss=0
		self.prev_room=0
		
	def hasbeenbeaten(self, room_cleared):
		if self.room_cleared === self.boss_beat_room[self.current_boss]:
			return True
		return False
	
	def beaten(self, time):
		self.boss[self.current_boss]=time
		self.current_boss+=1
	
	def scan(self):
		 with open(filename, 'r') as file:
		 	json_decoded=json.loads(base64.b64decode(file.read()))
		 	time = str(datetime.timedelta(seconds=json_decoded['runStats']['time']))
		 	room_cleared=json_decoded['runStats']['numberOfCombatRoomsCleared']
		 	#location = json_decoded['mapSaveData']['currentLocationName'].replace("\n", " ")
        	#room = json_decoded['progressionSaveData']['iRoomInProgress']
		 	
		 	if self.prev_room > room_cleared:
				self.reset()
				return True
				
			if self.hasbeenbeaten(room_cleared):
				self.beaten(time)
			return False
	
	def log(self):
		with open("runs.csv", 'a') as output:
            row=""
            for boss in self.boss
            	if boss == 0:
            		row+=";"
            	else:
            		row+=boss+";"
            
            output.write(row)
	
	def checkfile(self):
		current_modified=os.path.getmtime(self.filename)
		if current_modified != self.last_modified:
        	self.last_modified=current_modified
        	return true
        return false
        	

    
#init()
tracker = SSRunTracker()
while True:
    time.sleep(0.5)
    if tracker.checkfile():
    	if tracker.scan():
    		tracker.log
   
