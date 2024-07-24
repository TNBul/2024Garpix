with open("data.json", "r+") as data, open("default_data.json", "r+") as default:
	data.write(default.read())
