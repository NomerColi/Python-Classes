"""

Inheritance
you create a new class that is derived from an existing class
subclasses are easy to write
no need to write similar functions for each of the different types of classes
easy to modify

superclass <|--- subclass (solid line and hollow arrow)

Overriding
any methods in a subclass that have the same name as in the superclass

Super
The super() method returns the object as the superclass’s type so you can call methods from the superclass

"""

class Person:
    """Represents a person.
    Attributes:
        name (str): name of the person.
        address (str): address of the person.
        birth_year (int): year person was born.
    """
    def __init__(self, name, address, b_year):
        """Initializes the name, address, and birth year of the person."""
        self.name = name
        self.address = address
        self.birth_year = b_year

    def age(self, curr_year):
        """Returns the age of the person given the current year."""
        return curr_year - self.birth_year

    def __str__(self):
        """String representation of a person."""
        return "My name is " + self.name + " and I am " + str(self.age(2023)) + " years old.\nI live at " + self.address + "."


class Employee(Person):
        """Represents an employee.
        Attributes:
            job_desc (str): job description of employee.
            salary (int): salary of employee.
        """
        __doc__ = Person.__doc__ + __doc__

        def __init__(self, name, addr, b_year, job, sal):
            """Initializes the name, address, birth year, job description, and salary of the employee."""
            super().__init__(name, addr, b_year)
            self.job_desc = job
            self.salary = sal

        def do_job(self):
            """Returns a string representation of the employee doing their job."""
            return "I’m working, doing " + self.job_desc

        def __str__(self):
            """String representation of an employee."""
            return super().__str__()+ "\nMy job is " + self.job_desc + " and I get paid " + str(self.salary) + ".\n" + self.do_job()


#import person
#import employee

def main():
    p1 = Person("John", "123 Fake St.", 1999)
    p2 = Employee("George", "456 Main St.", 1995, "System Admin.", 80000)
    print(p1)
    print(p2)

main()