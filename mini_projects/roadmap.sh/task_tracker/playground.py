import json
import datetime

filepath = "tasks.json"

# --- Helper Functions --- #
def open_file():
	try:
		with open(filepath, 'r') as file:
			data = json.load(file)
	except FileNotFoundError:
		data = {}
	except json.JSONDecodeError:
		data = {}
	return data

def write_file(data):
	with open(filepath, 'w') as file:
		json.dump(data, file, indent=2)

def update(id, description, status = ""):
	# Open the file
	data = open_file()

	# Place reference to task into variable
	try:
		task = data["tasks"][id-1]
	except IndexError:
		print("Invalid Task ID")


	# Mutate the task description and updated time
	task["description"] = description
	task["updatedAt"] = "Updated!"
	if status != "": task["status"] = status
	
	# Write to the file
	write_file(data)