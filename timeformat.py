#Adds '0' at beginning of time if needed
def format(time):
	list = []
	ret = ''

	try:
		if time[1] == ':':
			for i in time:
				list.append(i)
			list.insert(0, '0')

		else: raise

	except:
		for i in time:
			list.append(i)

	list.extend(':' + '0' + '0')
	return ret.join(list)

#Calculates the endTimeBegin attribute based on startTimeFinish as input
def calc_end_time_begin(time):
	list = []
	ret = ''
	num = ''
	
	for i in time:
		list.append(i)

	num = int(list[0]+list[1])
	num += 1
	num = str(num)

	if len(num) == 2:
		list[0] = str(num[0])
		list[1] = str(num[1])
		
	else:
		list[1] = str(num)

	return ret.join(list)

