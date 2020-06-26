import time
from datetime import datetime
import win32gui
import uiautomation as auto
from activity import *

CONST_ACTIVITIES = ['Gmail', 'Command Prompt', 'Youtube', 'Facebook'] #.......
start_time = datetime.now()
_active_window_name = None
first_time = True
activities = []

def get_name(window_text):
	for element in CONST_ACTIVITIES:
		if element in window_text:
			window_text = element

	if "-" in window_text:
		return " ".join(window_text[window_text.rindex('-')+1:None].split())
	else:
		return window_text
	
while True:
	window = win32gui.GetForegroundWindow()
	active_window_name = win32gui.GetWindowText(window)

	if _active_window_name != active_window_name:
		_active_window_name = active_window_name
		
		if not first_time:
			end_time = datetime.now()
			
			current_active_window = Activity(get_name(active_window_name))
			current_active_window.set_prev_time(end_time)
			current_active_window.calculate_diference(start_time)
			exists = False
			
			#check if we have the activity registered
			for active_window in activities:
				if active_window.name == get_name(_active_window_name):
					exists = True
					active_window.set_prev_time(end_time)
					active_window.calculate_diference(start_time)
					print("Focus Activity: ", active_window.name , " Duration: ", (active_window.entry_time))
			
			#check if doesn't exist
			if not exists:
				if get_name(_active_window_name):
					activities.append(current_active_window)
					print("Focus Activity: ", current_active_window.name , " Duration: ", (current_active_window.entry_time))
			
		first_time = False	
		
	time.sleep(1)
