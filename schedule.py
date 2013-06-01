"""
file: schedule.py
language: python3
author: zkf5289@rit.edu Zachary K Friss 
description: cs1 lab6 Creates a schedule based off revenue per unit and project length for a given
interval of time. 
"""

class ProjectInfo():
    """
    Creates the class ProjectInfo
    """
    __slots__ = ('pid','plength','revenue','runit')

def mkProjectInfo(pid,plength,revenue,runit):
    """
    Creates the Project Info structure based on the class ProjectInfo

    pid (str) : name of the project
    plength (str) : length of the project
    revenue (str) : Revenue the project will make
    runit (float) : Revenue per week

    Returns the full project info structure. 
    """

    struct = ProjectInfo()
    struct.pid = pid
    struct.plength = plength
    struct.revenue = revenue
    struct.runit = runit
    return struct

def insertion_sort(data,sort):
    """
    insert_sort : ListofOrderables -> None
    Perform an in-place insertion sort on a list of sortable data.
    
    Parameters:
    data - the list of data to sort
    sort - what to sort.
    
    post - conditions
    the data list has been sorted.
    """
    if sort == 'runit':
        marker = 1
        while marker < len(data):
            marker_val = data[marker]
            i = marker
            while i > 0 and data[i-1].runit > marker_val.runit:
                data[i] = data[i-1]
                i -= 1
            data[i] = marker_val
            marker = marker + 1
    elif sort == 'plength':
        marker = 1
        while marker < len(data):
            marker_val = data[marker]
            i = marker
            while i > 0 and data[i-1].runit == marker_val.runit and data[i-1].plength > marker_val.plength:
                data[i] = data[i-1]
                i -= 1
            data[i] = marker_val
            marker = marker + 1

def make_schedule(weeks,schedule):
    """
    Creates a list of projects to schedule based off a greedy algorithm of taking
    the projects with the highest runit value that fit the given weeks.

    weeks (int) : Number of weeks to schedule
    schedule (list) list of projects to schedule

    Returns the list of projects to schedule. 
    """
    schedule_list = schedule[:]
    insertion_sort(schedule_list,'runit')
    insertion_sort(schedule_list,'plength')
    your_list = []
    while weeks > 0 and len(schedule_list) > 0:
        project = schedule_list.pop()
        time = int(project.plength)
        weeks = weeks - time

        if weeks >= 0:
            your_list.append(mkProjectInfo(project.pid,project.plength,project.revenue,project.runit))
        if weeks < 0:

            weeks = weeks + time

    return your_list

def scheduleLst(fileName):
    """
    Takes projects from file and adds them to a list after calling the mkProjectInfo function.

    fileName (str): Location of the file to read.

    Returns the projects in a list. 
    """
    projects = []
    for line in open(fileName):
        elements = line.split()
        pid = elements[0]
        plength = elements[1]
        revenue = elements[2]
        runit = float((int(elements[2]) / int(elements[1])))
        projects.append(mkProjectInfo(pid,plength,revenue,runit))
    return projects
       
def displaySchedule(schedule,weeks):
    """
    Displays the list of projects to schedule, calculates the revenue that it will
    generate and finds how many weeks have been left unscheduled.

    schedule (list) : List of projects to be scheduled
    weeks (int) : length of weeks to be scheduled.

    Prints schedule, revenue and weeks left. 
    """
    revenue = 0
    leftover = 0
    if schedule == None:
        print("Couldn't find a schedule that fits the given weeks.")
    else:
        print("Projects to schedule:")
        for entry in schedule:
            print(entry.pid)
            revenue += int(entry.revenue)
            leftover += int(entry.plength)
        print("Total Revenue: ",revenue)
        print("Unscheduled weeks in schedule: ",(weeks - leftover))
            
def main():
    """
    Main function that prompts user for filename and number of weeks to schedule.
    Calls other functions to create schedule. 
    """
    fileName = input("Enter Filename for projects: ")
    projects = scheduleLst(fileName)
    weeks = int(input("Amount of weeks to schedule: "))
    displaySchedule(make_schedule(weeks,projects),weeks)

main()
