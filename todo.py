import argparse
import os

TASK_FILE = ".tasks.txt"

def add_task(task):
    """Function: add_task
    
    Input - a task to add to the list
    Return - nothing
    """
    with open (TASK_FILE, "a", encoding="utf-8") as file:
        file.write(task + "\n")


def list_tasks():
    """
    Lists the tasks in the provided task list with their index.
    
    Args: 
        list_tasks: A list of strings, where each string represents a task.
        
    Returns:
        str: A formatted string containing the numbered tasks, or an empty string if the todo list is empty.
    """

    # read in the file TASK_FILE
    with open (TASK_FILE, "r", encoding="utf-8") as file:
        tasks = file.readlines()
        
    output_string = "Your task list:\n"
    formatted_tasks = []
    for index, task in enumerate(tasks):
       formatted_tasks.append(f"{index + 1}. {task}")
    output_string += "".join(formatted_tasks)
    print(output_string)
    return output_string.rstrip('\n')

     
               



def remove_task(index):
    
    return

def main():
    parser = argparse.ArgumentParser(description="Command-line Todo List")
    parser.add_argument(
            "-a",
            "--add",
            help="Add a new task"
            )
    parser.add_argument(
            "-l",
            "--list",
            action="store_true",
            help="List all tasks")
    parser.add_argument(
            "-r",
            "--remove",
            help="Remove a task by index")

    args = parser.parse_args()

    if args.add:
        add_task(args.add)
    elif args.list:
        tasks = list_tasks()
        print(tasks)
    elif args.remove:
        remove_task(int(args.remove))
    else:
        parser.print_help()


if __name__ == "__main__":
    main()

