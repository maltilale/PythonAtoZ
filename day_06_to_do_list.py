# You are building a command-line to-do list application that allows users to manage their tasks and persist them to a file. The application should support adding, viewing, completing, and deleting tasks through terminal commands.

# Your task is to implement a TodoList class that handles all task operations and file persistence.

# Requirements
# The TodoList class should support the following operations:
# add_task(description: str) - Add a new task with the given description
# view_tasks() - Display all tasks with their status (pending/completed)
# complete_task(task_id: int) - Mark a task as completed
# delete_task(task_id: int) - Remove a task from the list
# save_to_file(filename: str) - Save all tasks to a file
# load_from_file(filename: str) - Load tasks from a file

# Input Format
# Task descriptions are strings with length 1≤len≤200
# Task IDs are integers starting from 1
# Filename is a valid string representing a file path

# Output Format
# For view_tasks(), output should be formatted as:
# [ID] [Status] Description
# Where Status is either [ ] for pending or [X] for completed.

# Constraints
# 1≤number of tasks≤1000
# 1≤number of tasks≤1000
# Task descriptions contain only printable ASCII characters
# File operations should handle errors gracefully
# Task IDs should persist even after deletion (don't reuse IDs)

from pydantic import BaseModel


def valid_input():
    global task_description, task_id, file_name
    print("To create a to-do list, give below details: ")
    try:
        task_description = str(
            input("Give task description with lenght not more then 200 characters: ")
        )
        task_id = int(input("Give task ID: "))
        file_name = str(input("Give file name to be saved with: "))

    except ValueError as e:
        print(e)
        print("Invalid input! Please enter a valid input.")
    else:
        todo = TodoList()
        todo.add_task(task_description, task_id, file_name)
        todo.view_tasks()


class Task(BaseModel):
    task_description: str
    task_id: int
    status: str


class TodoList:

    def __init__(self):
        self.to_do_list = []

    def add_task(self, description: str, id: int, file_name: str):
        task = Task(task_description=description, task_id=id, status="pending")
        task.status = "pending"
        self.to_do_list.append(task)
        self.save_to_file(file_name, task)

    def view_tasks(self) -> list[Task]:
        return self.to_do_list

    def complete_task(self, task_id: int):
        for task in self.to_do_list:
            if task.task_id == task_id:
                task.status = "completed"
                break
        self.view_tasks()

    def delete_task(self, task_id: int):
        for index in range(len(self.to_do_list)):
            if self.to_do_list[index].task_id == task_id:
                self.to_do_list.pop(index)
                break
        self.view_tasks()

    def save_to_file(self, filename: str, task: Task):
        try:
            with open(filename, "w") as f:
                f.write(task.task_description)
            print(f"file saved successfully at: {filename}")
            self.load_from_file(filename)
        except IOError as e:
            print(f"An error occurred while saving the file: {e}")

    def load_from_file(self, filename: str):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                return f.read()

        except FileNotFoundError:
            print("The file was not found.")
        except IOError as e:
            print(f"An error occurred while opening the file: {e}")


if __name__ == "__main__":
    valid_input()
    print
