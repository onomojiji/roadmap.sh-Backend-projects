# import natives packages
import os
import json
from datetime import datetime

#############################
# VARIABLES
#############################

file_path = os.path.join(os.getcwd(), "tasks.json") # "$PWD/tasks.json"

#############################
# Functions
#############################

# get json file content
def get_json_content() -> dict:
    if os.path.exists(file_path):
        with open(file_path, "r") as json_file:
            return json.load(json_file)
    else:
        return {}

task_dict = get_json_content()

# Save to json file
def save_to_json(data: dict) -> None:
    with open(file_path, "w") as json_file:
        json.dump(data, json_file, indent=2)

# Adding new task 
def add_task(desciption: str) -> dict:
    
    id = len(task_dict) + 1
    while str(id) in task_dict:
        id += 1
    description = desciption
    status = "todo"
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    task_dict[id] = {
        "description": description,
        "status": status,
        "created_at": created_at,
        "updated_at": updated_at
    }

    save_to_json(task_dict)

    return task_dict
     
# Update existing task
def update_task(task_id : int, new_description) -> dict:
    local_task_dict = get_json_content()
    if str(task_id) in local_task_dict:
        local_task_dict[str(task_id)]["description"] = new_description
        local_task_dict[str(task_id)]["updated_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        save_to_json(local_task_dict)
        return local_task_dict
    else:
        return {"error": "Task not found"}

# Delete task
def delete_task(task_id : int) -> dict:
    local_task_dict = get_json_content()
    if str(task_id) in local_task_dict:
        del local_task_dict[str(task_id)]
        save_to_json(local_task_dict)
        return local_task_dict
    else:
        return {"error": "Task not found"}
    
# Change task status
def change_task_status(task_id : int, new_status : str) -> dict:
    local_task_dict = get_json_content()
    if str(task_id) in local_task_dict:
        local_task_dict[str(task_id)]["status"] = new_status
        local_task_dict[str(task_id)]["updated_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        save_to_json(local_task_dict)
        return local_task_dict
    else:
        return {"error": "Task not found"}
    
# List all tasks
def list_tasks(status=None) -> dict:
    all_local_tasks = get_json_content()
    # Check if status given
    if status:
        filtered_tasks = {task_id: task for task_id, task in all_local_tasks.items() if task["status"] == status}
        return filtered_tasks
    else:
        return all_local_tasks
    