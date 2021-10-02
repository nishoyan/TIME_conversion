#!/usr/bin/env python3

def timeConversion(s):
	if s[-2:] == "PM":
		nice = str(int(s[:1])+12) + s[2:-2]
		return nice
	else:
		return s


timeConversion("07:05:45PM")
