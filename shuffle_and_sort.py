def shuffles(mapper_out):
	""" Shuffler to Organise the mapped values by key
		Args:
			mapper_out (list): mapped airport names
		Return:
			data(dict): Shuffled mapped airport names """

	data = {}
	#Remove the none values from the list
	mapper_out = list(filter(None, mapper_out))

	#Organise the mapped values by key
	for k, v in mapper_out:
		if k not in data:
			data[k] = [v]
		else:
			data[k].append(v)
	return data

def sort(lists):
	""" Sort by Airport name alphabetically

		Args:
			dicts (dict): Shuffled mapped airport names
		Return:
			sortedDict(dict): Sorted and Shuffled mapped airport names """
	data = {}
	for k, v in lists:
		data[k] = v
	sortedDict = dict(sorted(data.items()))
	return sortedDict