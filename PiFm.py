#!/usr/bin/python

from subprocess import call


def play_sound( filename,frequency ):
   call(["./pifm", filename,frequency])
   return
