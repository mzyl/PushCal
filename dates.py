class Date():

	def __init__(self, day = None, startTime = None, startTimeFinish = None, endTimeBegin = None, endTime = None):
		self.day = day
		self.startTime = startTime
		self.startTimeFinish = startTimeFinish
		self.endTimeBegin = endTimeBegin
		self.endTime = endTime
	
	#Assigns day attribute using day found in text generated from image
	def assignDay(self, text):
		for i in text:
			if i == 'Sunday' or i == 'Monday' or i == 'Tuesday' or i == 'Wednesday' or i == 'Thursday' or i == 'Friday' or i == 'Saturday':
				self.day = i
				break
	
	#Assigns each time attribute based on preceeding indicator found in text generated from image
	def assignTime(self, text):
		for i in range(len(text)):
			if text[i] == 'Start:' or text[i] == 'Start':
				self.startTime = text[i+1]
			elif text[i] == 'Break:' or text[i] == 'Break':
				self.startTimeFinish = text[i+1]
			elif (text[-1] != 'End:' and text[-1] != 'End') and (text[i] == 'End:' or text[i] == 'End'):
				self.endTime = text[i+1]
	
	#Computes and assigns Start and End time blocks
	def assignBlock(self):
		try:
			self.endTimeBegin = int(self.breakTime[0]) + 1
		except:
			pass
	

	'''
	Accessors:
	'''
	def getDay(self):
		return self.day
	
	def getStartTime(self):
		return self.startTime
	
	def getStartTimeFinish(self):
		return self.startTimeFinish
	
	def getEndTimeBegin(self):
		return self.endTimeBegin
	
	def getEndTime(self):
		return self.endTime


	'''
	Mutators:
	'''
	def setDay(day):
		self.day = day
	
	def setStartTime(time):
		self.startTime = time
	
	def setStartTimeFinish(time):
		self.startTimeFinish = time
	
	def setEndTimeBegin(time):
		self.endTimeBegin = time

	def setEndTime(time):
		self.endTime = time

	#Resets wrongly assigned times to 'None'
	def clean(self):
		try:
			int(self.startTime[0])
		except:
			self.startTime = None

		try:
			int(self.breakTime[0])
		except:
			self.breakTime = None

		try:
			int(self.endTime[0])
		except:
			self.endTime = None
	

	'''
	Testing:
	'''
	def toString(self):
		print("Day: ", self.day)
		print("Start Time: ", self.startTime)
		print("Break Time: ", self.startTimeFinish)
		print("End Time Begin: ", self.endTimeBegin)
		print("End Time: ", self.endTime)
