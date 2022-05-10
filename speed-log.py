#!usr/bin/env python3

import datetime
import speedtest
import sys


sptest = speedtest.Speedtest()
now = datetime.datetime.now()

def Get_Server() -> dict:
	return sptest.get_best_server() # as dictionary

def Test_Speed() -> dict:
	down = round(sptest.download() / 1000 / 1000) # Mbit/s
	up = round(sptest.upload() / 1000 / 1000) # Mbit/s

	return {"download": down,
			"upload": up,
			} # as dictionary in Mbit/s

def Excel_Save():
	raise NotImplementedError("Save function not implemented yet")

def Show_Speed():
	server = Get_Server()
	speed_result = Test_Speed()
	print("Pvm:", now.strftime("%d.%m.%Y %H:%M"))
	print("Server:", server['country'] + ", " + server['sponsor'])
	print("Ping:", round(server['latency']), "ms")
	print("Download:", speed_result['download'], "Mbit/s")
	print("Upload:", speed_result['upload'], "Mbit/s")


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
Ping sisältyy serveriin
Testaa nopeus

Tallenna tiedot

arg "-v" tallentaa ja tulostaa myös tulokset näytölle
"""
