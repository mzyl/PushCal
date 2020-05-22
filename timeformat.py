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

def calc_end_time_begin(time):
	list = []
	ret = ''
	if time[0] == '0':
		print("if")
		for i in time:
			list.append(i)
		print(list)
		list[1] = str(int(list[1]) + 1)
		print(list)
		return ret.join(list)

	else:
		print("else")
		if time[1] == '2':
			time[0] = 0
			time[1] = 1
			print(time)
			return time
		
		else:
			time[1] = int(time[1]) + 1
			print(time)
			return time
