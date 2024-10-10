import check_input
from task import Task
"""
Written by: Omar Juarez, Yunjae Cho
Date: Fall 2024

"""

def main_menu():
    """Displays the main menu and returns the user's valid input
    Args:
        none
    Returns:
        user input
    """
    print("-Tasklist-")
    print(
        "1. Display current task\n2. Mark current task complete\n3. Postpone current task\n4. Add new task\n5. Save and quit")
    user_choice = check_input.get_int_range(
        "Enter choice: ", 1, 5)
    return user_choice
    


def read_file():
    """Opens the file "tasklist.txt" and read in each of the tasks
    Args:
        none
    Returns:
        filled task list
    """
    tasklist = []
    with open("tasklist.txt", 'r') as file: # stores each line in a list
        lines = file.readlines()
        for line in lines:
            # Split the line into description, date, and time
            description, date, time = line.strip().split(',')
            task = Task(description, date, time)
            tasklist.append(task)
    return tasklist


def write_file(tasklist):
    """Passes in the list of tasks that will be written to the file "tasklist.txt"
    Iterates through the list of tasks and write each one to the file using the Task's
    repr() method
    Args:
        tasklist
    Returns:
        none
    """
    with open('tasklist.txt', 'w') as file:
        for task in tasklist:
            file.write(repr(task) + '\n')


def get_date():
    """Prompts the user to enter the month, day, and year
    Args:
        none
    Returns:
        formatted date
    """
    month = check_input.get_int_range("Enter month: ", 1, 12)
    day = check_input.get_int_range("Enter day: ", 1, 31)
    year = check_input.get_int_range("Enter year: ", 2000, 2100)
    formatted_date = f"{month:02}/{day:02}/{year}"

    return formatted_date


def get_time():
    """Prompts the user to enter the hour (military time) and minute
    Args:
        none
    Returns:
        formatted time
    """
    hour = check_input.get_int_range("Enter hour: ", 0, 23)
    minute = check_input.get_int_range("Enter minute: ", 0, 59)
    formatted_time = f"{hour:02}:{minute:02}"

    return formatted_time


def main():
    tasklist = read_file()
    tasklist.sort()
    print(f"You have {len(tasklist)} tasks.")
    replay = True
    while replay is True:
        user_input = main_menu()
        if user_input == 1:
            # displays current task
            if tasklist:
                # If there are tasks, display the first one
                print(f"Current task: {tasklist[0]}")
            else:
                # If no tasks, display completion message
                print("All your tasks are complete.")
        elif user_input == 2: # displays the current task, remove it and then display the new task.
            if tasklist:
                # If there are tasks, display the first one
                print(f"Marking current task as complete: {tasklist[0]}")
                tasklist.pop(0)
                if tasklist:
                    # If there are tasks, display the first one
                    print(f"New current task is: {tasklist[0]}")
                else:
                    print("All your tasks are complete.")
            else:
                # If no tasks, display completion message
                print("All your tasks are complete.")
        elif user_input == 3: # displays the current task and then prompt the user to enter a new date and time
            if tasklist:
                current_task = tasklist[0]
                print(f"Postponing task: {tasklist[0]}")
                print("Enter new due date:")
                new_date = get_date()
                print("Enter new time:")
                new_time = get_time()

                tasklist.pop(0)

                updatted_task = Task(current_task.description, new_date, new_time)
                tasklist.append(updatted_task)

                tasklist.sort()
            else:
                print("All your tasks are complete.")
        elif user_input == 4: # prompt the user to enter a new task description, due date, and time.
            new_description = input("Enter a task: ") 
            print("Enter due date:")
            new_date = get_date()
            print("Enter time:")
            new_time = get_time()

            new_task = Task(new_description, new_date, new_time)

            tasklist.append(new_task)
            tasklist.sort()
        else: # writes the contents of the task back to the file (overwrite the old contents, do not append) and then end the program.
            write_file(tasklist)
            replay = False


main()