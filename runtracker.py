#!/usr/bin/python3
import time
import os.path
import base64
import json
import datetime

directory="./"
filename=directory+"RunSaveData.dat"
output_filename="runs.csv"

last_modified=str()
row=""

prev_room=0
dasher=False
impaler=False
ume=False


def init():
    try:
        global last_modified
        last_modified=os.path.getmtime(filename)
        loglatest()
    except:
        print("cannot find or access :%s" % filename)
        if os.path.exists(directory+"SaveData.dat"):
            print("please launch the game and just click new game, and this script should work")
            #maybe useless i dunno
            last_modified=os.path.getmtime(SaveData.dat)
        else:
            print("doesn't sound like the right directory to me")
        quit()
    

def loglatest():
    global prev_room, row,  dasher, impaler, ume
    with open(filename, 'r') as file:
        json_decoded=json.loads(base64.b64decode(file.read()))
        time = str(datetime.timedelta(seconds=json_decoded['runStats']['time']))
        #location = json_decoded['mapSaveData']['currentLocationName'].replace("\n", " ")
        #room = json_decoded['progressionSaveData']['iRoomInProgress']
        room_cleared=json_decoded['runStats']['numberOfCombatRoomsCleared']
        if prev_room > room_cleared:
            # means a reset
            print("reset")
            prev_room=room_cleared
            
            if not dasher:
                row+="--;"
            if not impaler:
                row+="--;"
            if not ume:
                row+="--;"
            dasher=False
            impaler=False
            ume=False
            with open(output_filename, 'a') as output:
                output.write(row)
                row=""
        elif prev_room < room_cleared:
            prev_room = room_cleared
            
        elif room_cleared == 3 and not dasher:
        
            dasher=True
            row+=time+";"
            print("dasher killed: ", time)
            
        elif room_cleared == 6 and not impaler:
            impaler=True
            row+=time+";"
            print("impaler killed", time)
        
        elif room_cleared == 10 and not ume:
            ume=True
            row+=time+";"
            print("Ume killed: %s", time)
        #print(time, room_cleared) 
       
init()

while True:
    time.sleep(0.5)
    
    current_modified=os.path.getmtime(filename)
    if current_modified != last_modified:
        last_modified=current_modified
        try:
            loglatest()
        except:
            #sometimes weird stuff happens and this gets triggered out of nowhere
            print("ouchie")
