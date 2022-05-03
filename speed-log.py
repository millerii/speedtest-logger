#!usr/bin/env python3

import datetime
import speedtest
import sys


sptest = speedtest.Speedtest()
	
def Get_Server() -> dict:
	return sptest.get_best_server() # as dictionary, include ping

def Test_Speed() -> dict:
	down = round(sptest.download() / 1000 / 1000) # Mbit/s
	up = round(sptest.upload() / 1000 / 1000) # Mbit/s

	return {"download": down,
			"upload": up,
			} # as dictionary in Mbit/s

def Excel_Save():
	raise NotImplementedError("Save function not implemented yet")

def Show_Speed():
	raise NotImplementedError("Broken")


Get_Server()
print(Test_Speed())

argv = sys.argv

if "--show" in argv:
	Show_Speed()
	sys.exit()

# Excel_Save()


"""
pvm, klo, sponsor, name, ping, download, upload, Mbit/s
Tallenna klo/pvm
Hae serveri
Testaa ping
Testaa nopeus

Tallenna tiedot

arg "-v" tallentaa ja tulostaa myös tulokset näytölle
"""
