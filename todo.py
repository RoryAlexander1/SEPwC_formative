""" This module handles command-line argument parsing using argparse."""
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
        str: A formatted string containing numbered tasks, or an empty string
        if todo list is empty.
    """

    # read in the file TASK_FILE
    # used Gemini
    with open (TASK_FILE, "r", encoding="utf-8") as file:
        tasks = file.readlines()
    output_string = "Your task list:\n"
    formatted_tasks = []
    for index, task in enumerate(tasks):
        formatted_tasks.append(f"{index + 1}. {task}")
    output_string += "".join(formatted_tasks)
    return output_string.rstrip('\n')


def remove_task(index):
    """Function: remove_task
    Input: index - the number of the task to remove from the list
    Return: Nothing
    """
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r", encoding="utf-8") as file:
            tasks = file.readlines()
        if 1 <= index <= len(tasks):
            with open(TASK_FILE, "w", encoding="utf-8") as file:
                for i, task in enumerate(tasks, start=1):
                    if i != index:
                        file.write(task)
            print(f"Task at index {index} removed.")
        else:
            print(f"Invalid task number: {index}. Please enter number between 1 and {len(tasks)}.")
    else:
        print("No tasks found.")

def main():
    """ Main function to execute the program logic."""
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
