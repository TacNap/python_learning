import task_tracker
from datetime import datetime

# List tasks. Create new file if none exists
task_tracker.list_tasks()

# Add new task and list tasks to reflect changes
task_tracker.add("New Task")
task_tracker.list_tasks()

task_tracker.add("Second Task")
task_tracker.list_tasks()

task_tracker.add("Third Task")
task_tracker.list_tasks()

# Update existing task
task_tracker.update(2, "Updated Task & Time!")
task_tracker.list_tasks()

# Delete Task
task_tracker.delete(2)

# List All Tasks, then only Done tasks
task_tracker.list_tasks()
print("Only Done:")
task_tracker.list_tasks("Done")
print("Invalid Call:")
task_tracker.list_tasks("yellow")

# Doesn't work in sublime. Requires input from terminal window.
#task_tracker.update_status(1)
