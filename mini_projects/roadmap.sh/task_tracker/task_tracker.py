# 2/1/2025
# Task Tracker project from https://roadmap.sh/projects/task-tracker

"""
Each task has the properties:
	id
	description
	status
	createdAt : Date and Time of creation of task
	updatedAt : Date and Time of last update of task
"""
import json
import datetime
import os

filepath = "tasks.json"

# User-Called Functions
def add(description):
	data = open_file()

	# Generate new ID
	last_id = data["tasks"][-1]["id"]
	new_id = last_id + 1

	# Retrieve Time
	current_time = "right this very moment"

	# Create new task
	new_task = {
		"id": new_id,
		"description": description,
		"status": "pending",
		"createdAt": current_time,
		"updatedAt": current_time
	}

	data["tasks"].append(new_task)

	write_file(data)
	print("Task Added!")

def update(id, description):
	# Open the file
	data = open_file()

	# Place reference to task into variable
	try:
		task = data["tasks"][id-1]
	except IndexError:
		print("Invalid Task ID")
		return
	except TypeError:
		print("Invalid Task ID: Provide an Integer")
		return

	# Mutate the task description and updated time
	task["description"] = description
	update_time(task)
	
	# Write to the file
	write_file(data)
	print("Task Updated!")

def update_status(id):
	statuses = ["none", "To-Do", "In Progress", "Done"]
	# Open file
	data = open_file()

	# Place task reference into a variable
	try:
		task = data["tasks"][id-1]
	except IndexError:
		print("Invalid Task ID")
		return
	except TypeError:
		print("Invalid Task ID: Provide an Integer")
		return

	# Receive User Input
	print("\nFor task: '" + task["description"]+"', " + task["status"])
	print("Update to what?")
	print("[1] - To-Do")
	print("[2] - In Progress")
	print("[3] - Done")
	try:
		status_code = int(input("> "))
	except ValueError:
		print("Input a number")
		return
	
	# Change Status Accordingly
	if status_code >= 1 and status_code <= 3:
		task["status"] = statuses[status_code]
	else: 
		print("Input the right number")
		return

	# Update time
	update_time(task)
	
	# Write to the file
	write_file(data)
	print("Status changed to " + statuses[status_code] + "!")

def delete(id):
	# Open the file
	data = open_file()

	# Place reference to task into variable
	try:
		task = data["tasks"][id-1]
	except IndexError:
		print("Invalid Task ID")
		return
	except TypeError:
		print("Invalid Task ID: Provide an Integer")
		return

	removed_task = data["tasks"].pop(id-1)
	print("Removed Task [ID : " + str(removed_task["id"]) + "] -",removed_task["description"])
	
	
	# Write to the file
	write_file(data)

def list_tasks(status = ""):
	data = open_file()
	print_list(data)

def list_done():
	pass

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

# Currently prints JSON format
# Change this to be more presentable
def print_list(data):
	#json_formatted = json.dumps(data, indent=2)
	#print(json_formatted)
	line_break = "______________________________________________________"
	print(line_break)
	for task in (data["tasks"]):
		
		print("[ID :",str(task["id"]) +"]")
		print(task["description"])
		print("	",task["status"])
		print("	","Created:",task["createdAt"])
		print("	","Last Update:",task["updatedAt"])
		print(line_break)

def write_file(data):
	with open(filepath, 'w') as file:
		json.dump(data, file, indent=2)

def update_time(task):
	task["updatedAt"] = "Updated!"





