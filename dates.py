class Date():
	
	def __init__(day = None, startTime = None, breakTime = None, endTime = None):
		self.day = day
		self.startTime = startTime
		self.breakTime = breakTime
		self.endTime = endTime
	
	'''
	Accessors:
	'''
	def getDay():
		return self.day
	
	def getStartTime():
		return self.startTime
	
	def getBreakTime():
		return self.breakTime
	
	def getEndTime():
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

