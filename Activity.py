
class Activity:
	def __init__(self, name):
		self.name = name
		self.entry_time = None
		self.prev_time = [None] * 2
		
	def calculate_diference(self, start_time):
		if self.prev_time[0] == None:
			self.entry_time = self.prev_time[1] - start_time # will give you the timedelta difference between racer "a" and racer "b" 
		else: 
			self.entry_time = ( (self.prev_time[1] - self.prev_time[0]) )
			
	def get_time_entry(self):
		return self.entry_time	
	
	def set_prev_time(self, end_time):
		if end_time not in self.prev_time:
			self.prev_time.append(end_time)
			if(len(self.prev_time)>2):
				del self.prev_time[0]
