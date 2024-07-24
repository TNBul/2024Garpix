import json, sys, os
from itertools import compress, combinations, chain, count
from collections import deque
from contextlib import contextmanager, redirect_stdout

@contextmanager
def silencer(is_silent = True):
	"""A context manager that redirects stdout to devnull"""

	if is_silent:
		with open(os.devnull, 'w') as fnull, redirect_stdout(fnull) as out:
			yield out
	else:
		print("The code is verbose")
		yield sys.stdout

###

def main(json_str = None, json_file_path = "data.json"):
	if json_str == None:
		with open(json_file_path) as file:
			json_str = file.read()
	data_list = json.loads(json_str)
	return shmain(data_list)

@silencer(True)
def shmain(data_list):
	#ordering data; optimizing time by calculating key density
	print(f"{data_list = }")
	density_list = [(density(key, data_list), key) for key in data_list[0].keys()] #O(n*m) + sorting
	density_list.sort(reverse = True)
	masked_key_iter = chain(*map(lambda comb_len: #~2^(n-1)
		combinations(map(lambda x: x[1], density_list), comb_len), range(1,len(density_list)))
	) 
	# print(f"{list(masked_key_iter) = }") #comment to preserve iter
	print(f"{density_list = }")

	for key_tuple in masked_key_iter:
		if are_all_unique(map(dict_freezer(key_tuple), data_list)):
			print("Success!")
			return ",\n".join(key_tuple)
	else:
		print(f"Search unseccessful; return all keys")
		return ",\n".join(data_list[0].keys())
	print("Something was skipped")



	"""
	1. keys -> space = {key0, key1 ...}; vals -> matrix = (*point0, *point1, ...) | pointi = (vali0, vali1, ...)^T
	2. P * M = m | P is diag & bin AND columns of m - unique
	3. start iterating over P_i
		3.1 sparse key -> dense key (the less identical vals clusters - the denser)
		3.2 min P      -> max P     (the less tr(P) - the less is )
	"""

def density(key, data_list):
	"""
	returns a number of unique vals from data_list via key
	a.k.a. number of clusters
	"""
	different_vals = {cur_dict[key] for cur_dict in data_list}
	return len(different_vals)

def dict_freezer(key_tuple):
	"""
	dict_freezer(key_tuple)(some_dict)
	creates a tuple of some_dict items, such that keys are in key_tuple
	"""
	def to_frozen_dict(cur_dict):
		return tuple(filter(lambda keyval: keyval[0] in key_tuple, cur_dict.items()))
	return to_frozen_dict

def are_all_unique(iterable, element_number = None):
	"""
	determines, whether the elements in iterable are unique, consuming it
	"""
	if element_number != None:
		return len(set(iterable)) == element_number
	else:
		frozen_iter = tuple(iterable)
		return len(set(frozen_iter)) == len(frozen_iter)

def count_iter_items(iterable):
    """
    consumes an iterable not reading it into memory; returns the number of items.
    """
    counter = count()
    deque(zip(iterable, counter), maxlen = 0)  #consume at C speed
    return next(counter)

print(main())