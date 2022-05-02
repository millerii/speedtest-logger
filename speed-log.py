#!usr/bin/env python3

import datetime
import speedtest
import sys


def test_speed():
	sptest = speedtest.Speedtest()
	date = datetime.datetime.now().strftime("%d.%m.%Y")
	time = datetime.datetime.now().strftime("%H:%M")

	sptest.get_best_server()

	server = sptest.results.server
	ping = round(sptest.results.ping, 1) # ms
	download = round(sptest.download() / 1000 / 1000) # Mbit/s
	upload = round(sptest.upload() / 1000 / 1000) # Mbit/s
	
	return date, time, server["name"], server["sponsor"], ping, download, upload

def excel_save():
	raise NotImplementedError("Save function not implemented yet")

def show_speed():
	speed_result = test_speed()
	print("Pvm:", speed_result[0] + " " + speed_result[1])
	print("Server:", speed_result[2] + ", " + speed_result[3])
	print("Ping:", speed_result[4], "ms")
	print("Download:", speed_result[5], "Mbit/s")
	print("Upload:", speed_result[6], "Mbit/s")


argv = sys.argv

if "--show" in argv:
	show_speed()
	sys.exit()

# excel_save()


"""
pvm, klo, sponsor, name, ping, download, upload, Mbit/s
Tallenna klo/pvm
Hae serveri
Testaa ping
Testaa nopeus

Tallenna tiedot

arg "-v" tallentaa ja tulostaa myös tulokset näytölle
"""