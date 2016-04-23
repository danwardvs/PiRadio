#!/usr/bin/python

from subprocess import call


def play_sound( filename,frequency ):
   call(["/home/pi/Desktop/Code/PiRadio/pifm", filename,frequency])
   return
