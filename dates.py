class Date():
	
	def __init__(self, day = None, startTime = None, breakTime = None, endTime = None):
		self.day = day
		self.startTime = startTime
		self.breakTime = breakTime
		self.endTime = endTime
	
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

