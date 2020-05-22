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
			print("if2")
			for i in time:
				list.append(i)
			print(list)
			list[0] = '0'
			list[1] = '1'
			print(list)
			return ret.join(list)
		
		else:
			print("else2")
			for i in time:
				list.append(i)
			print(list)
			list[1] = str(int(list[1]) + 1)
			print(list)
			return ret.join(list)

