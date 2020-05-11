class Date():
	
	def __init__(self, day = None, startTime = None, breakTime = None, endTime = None):
		self.day = day
		self.startTime = startTime
		self.breakTime = breakTime
		self.endTime = endTime
	
	def assignDay(self, text):
		for i in text:
			if i == 'Sunday' or i == 'Monday' or i == 'Tuesday' or i == 'Wednesday' or i == 'Thursday' or i == 'Friday' or i == 'Saturday':
				self.day = i
	
	def assignTime(self, text):
		for i in range(len(text)):
			if text[i] == 'Start:' or text[i] == 'Start':
				self.startTime = text[i+1]
			elif text[i] == 'Break:' or text[i] == 'Break':
				self.breakTime = text[i+1]
			elif (text[i] == 'End:' or text[i] == 'End'):
				print(text[i])
				self.endTime = text[i+1]
	

	'''
	Accessors:
	'''
	def getDay(self):
		return self.day
	
	def getStartTime(self):
		return self.startTime
	
	def getBreakTime(self):
		return self.breakTime
	
	def getEndTime(self):
		return self.endTime


	'''
	Mutators:
	'''
	def setDay(day):
		self.day = day
	
	def setStartTime(time):
		self.startTime = time
	
	def setBreakTime(time):
		self.breakTime = time
	
	def setEndTime(time):
		self.endTime = time


	'''
	Testing:
	'''
	def toString(self):
		print("Day: ", self.day)
		print("Start Time: ", self.startTime)
		print("Break Time: ", self.breakTime)
		print("End Time: ", self.endTime)
