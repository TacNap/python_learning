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
from datetime import datetime
import os

filepath = "tasks.json"
new_list = {"tasks": []}
_statuses = ["", "To-Do", "In Progress", "Done"]


# User-Called Functions
def add(description):
	data = open_file()
	# Generate new ID
	new_id = 1 if not data["tasks"] else data["tasks"][-1]["id"]+1

	# Retrieve Time
	time = str(datetime.now())


	# Create new task
	new_task = {
		"id": new_id,
		"description": description,
		"status": _statuses[1],
		"createdAt": time,
		"updatedAt": time
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
		task["status"] = _statuses[status_code]
	else: 
		print("Input the right number")
		return

	# Update time
	update_time(task)
	
	# Write to the file
	write_file(data)
	print("Status changed to " + _statuses[status_code] + "!")

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
	if status not in _statuses:
		print("Invalid Status")
		return
	data = open_file()
	print_list(data, status)


# --- Helper Functions --- #
def open_file():
	try:
		with open(filepath, 'r') as file:
			data = json.load(file)
	except FileNotFoundError:
		data = new_list
		write_file(data)
	except json.JSONDecodeError:
		data = new_list
		write_file(data)
	return data

# Currently prints JSON format
# Change this to be more presentable
def print_list(data, status = ""):
	line_break = "______________________________________________________"
	if not data["tasks"]:
		print("No Tasks Yet!")
		return
	print(line_break)

	for task in (data["tasks"]):
		if not status or task["status"] == status:
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
	task["updatedAt"] = str(datetime.now())





