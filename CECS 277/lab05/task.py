""" Task Class for the Task Manager

Written by: Omar Juarez, Yunjae Cho
Date: Fall 2024

"""

class Task:
    """Represents a task for a task manager.
    Attributes:
        description (str): description of the task
        date (str): due date of the task
        time (str): time the task is due
    """
    def __init__(self, description="", date="01/01/2000", time="00:00"):
        self.description = description
        self.date = date
        self.time = time
    def get_description(self):
        """Returns the task's description string.
        Args:
            self
        Returns:
            the description string
        """
        return self.description
    def __str__(self):
        """Returns a string used to display the task's information to the user.
        Args:
            self
        Returns:
            string with task, date, and time
        """
        return f"{self.description} -\nDue: {self.date} at {self.time}"
    def __repr__(self):
        """Returns a string used to write the task's information to the file.
        Args:
            self
        Returns:
            string with task, date, and time
        """
        return f"{self.description},{self.date},{self.time}"
    def __lt__(self, other):
        """Returns true if the self task is less than the other task.
        Args:
            self
            other
        Returns:
            bool whether the self task is less than the other task
        """
        less = False
        #202405011047
        self_num = (int(self.date[6:]) * 10**8) + (int(self.date[0:2]) * 10**6) + (int(self.date[3:5]) * 10**4) + (int(self.time[0:2]) * 10**2) + int(self.time[3:5])
        other_num = (int(other.date[6:]) * 10**8) + (int(other.date[0:2]) * 10**6) + (int(other.date[3:5]) * 10**4) + (int(other.time[0:2]) * 10**2) + int(other.time[3:5])
        #print(self_num)
        #print(int(self.date[6:]) * 10**8, int(self.date[0:2]) * 10**6, int(self.date[3:5]) * 10**4, int(self.time[0:2]) * 10**2, int(self.time[3:5]))
        
        if self_num < other_num:
            less = True
        elif self_num == other_num:
            less = self.description < other.description

        return less
        

'''def main_():
    t1 = Task("RSD", "05/01/2023", "10:47")
    t2 = Task("BASD", "05/01/2023", "10:47")
    print(t1)
    print(repr(t1))
    print(t2)
    print(repr(t2))
    print(t1 < t2)


main_()'''