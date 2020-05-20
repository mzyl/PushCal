def format(time):
	try:
		if time[1] == ':':
			list = []
			ret = ''
			for i in time:
				list.append(i)
			list.insert(0, '0')
			return ret.join(list)
	except:
		print('nope')
		return time
