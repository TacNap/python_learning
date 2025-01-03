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

def update(id, description, status = ""):
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
	task["updatedAt"] = "Updated!"
	if status != "": task["status"] = status
	
	# Write to the file
	write_file(data)

def delete(id = 0):
	pass

def mark_done(id = 0):
	pass

def mark_prog(id = 0):
	pass

def list_done():
	pass

def list_todo():
	pass

def list_prog():
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

def print_list(data):
	print(data)

def write_file(data):
	with open(filepath, 'w') as file:
		json.dump(data, file, indent=2)

	print(data)





