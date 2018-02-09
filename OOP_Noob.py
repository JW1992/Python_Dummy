#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Employee:
    '''All employee kinds'''
    # A variable declared inside the class definition but outside of a method is static variable.
    empCount = 0

    #Same as constructor
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print "Total Employee %d" % Employee.empCount

    def displayEmployee(self):
        print "Name : ", self.name, ", Salary: ", self.salary

if __name__ == '__main__':
    emp1 = Employee("Zara", 2000)
    emp2 = Employee("Eric", 3000)
    emp1.displayEmployee()
    emp2.displayEmployee()
    print "Total Employee %d" % Employee.empCount
