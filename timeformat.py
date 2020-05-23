#Adds '0' at beginning of time if needed
def format(time):
	try:
		if time[1] == ':':
			list = []
			ret = ''
			for i in time:
				list.append(i)
			list.insert(0, '0')
			return ret.join(list)
		else: raise

	except:
		return time

#Calculates the endTimeBegin attribute based on startTimeFinish as input
def calc_end_time_begin(time):
	list = []
	ret = ''
	if time[0] == '0':
		for i in time:
			list.append(i)
		list[1] = str(int(list[1]) + 1)
		return ret.join(list)

	else:
		if time[1] == '2':
			for i in time:
				list.append(i)
			list[0] = '0'
			list[1] = '1'
			return ret.join(list)
		
		else:
			for i in time:
				list.append(i)
			list[1] = str(int(list[1]) + 1)
			return ret.join(list)

