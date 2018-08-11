import os
import sys
from collections import OrderedDict
import datetime
from datetime import date

from peewee import *

db = SqliteDatabase('work_log.db')


class Entry(Model):

    name = TextField()
    dateworked = DateTimeField()
    work_task = TextField()
    timeworked = CharField()
    task_notes = TextField()

    class Meta:
        database = db


def initialize():

    db.connect()
    db.create_tables([Entry], safe=True)


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def search_query_date(user):
    """Search by Date """
    try:
        work_time_search = datetime.datetime.strptime(
            user, '%m/%d/%Y').date()
        return view_by_date(work_time_search)
        print("\n")
    except ValueError:
        return "Wrong Format"


def search_query(user):
    """Search by Name"""
    if user == "":
        print("You have to enter something ")
    else:
        return view_by_name(user)


def search_by_duration(user_minutes, user_seconds):
    """Search by Time"""
    try:
        work_dur = datetime.time(
            minute=int(user_minutes), second=int(user_seconds)
            )
        return view_by_dur(work_dur)
        print("\n")
    except ValueError:
        return "Wrong Format"


def search_by_keyword(user):
    """Search by search term"""
    if user == "":
        return "Enter something to search "
    else:
        return view_by_keyword(user)


def search_by_task(user):
    """Search by search term"""
    if user == "":
        return "Enter something to search "
    else:
        return view_by_work_task(user)


def add_entry(user, time_usr, task_usr, notes_usr, user_min, user_sec):
    """Add entries to Log """
    while True:
        try:
            dur_task = datetime.time(minute=int(user_min),
                                     second=int(user_sec))

            time_date = datetime.datetime.strptime(
                        time_usr, '%m/%d/%Y').date()

            Entry.create(
                name=user, dateworked=time_date, work_task=task_usr,
                timeworked=dur_task, task_notes=notes_usr
                )

            return (user, time_date, task_usr,
                    notes_usr, user_min, user_sec)
            break

        except ValueError:
            clear()
            print("Wrong Format in Date or Time. Try Again :) \n")
            break


def view_by_name(search_query=None):
    """View All Entries"""
    clear()
    entries = Entry.select().order_by(Entry.dateworked.desc())
    if search_query:
        entries = entries.where(Entry.name.contains(search_query))

    for entry in entries:
        dateworked = entry.dateworked.strftime('%m/%d/%Y')
        clear()
        print(dateworked)
        print('='*len(dateworked))
        print("name: " + entry.name + "\nwork: " +
              entry.work_task + "\nTime Worked: " +
              entry.timeworked + "\nNotes:\n" +
              entry.task_notes
              )
        print("\n")
        print('n) next entry')
        print('q) return to main menu')

        user = input("> ").lower()
        if user == "q":
            clear()
            break
        else:
            clear()
    if not entries:
        clear()
        print("Sorry couldn't find that information")


def view_by_dur(search_query=None):
    """Search by Duration"""
    clear()
    entries = Entry.select().order_by()
    if search_query:
        entries = entries.where(Entry.timeworked.contains(search_query))

    for entry in entries:
        dateworked = entry.dateworked.strftime('%m/%d/%Y')
        clear()
        print(dateworked)
        print('='*len(dateworked))
        print("name: " + entry.name + "\nwork: " +
              entry.work_task + "\nTime Worked: " +
              entry.timeworked + "\nNotes:\n" +
              entry.task_notes
              )
        print("\n")
        print('n) next entry')
        print('q) return to main menu')

        user = input("> ").lower()
        if user == "q":
            clear()
            break
        else:
            clear()
    if not entries:
        clear()
        print("Sorry couldn't find that information")


def view_by_date(search_query=None):
    """Search by Date"""
    clear()
    entries = Entry.select().order_by()
    if search_query:
        entries = entries.where(Entry.dateworked.contains(search_query))

    for entry in entries:
        dateworked = entry.dateworked.strftime('%m/%d/%Y')
        clear()
        print(dateworked)
        print('='*len(dateworked))
        print("name: " + entry.name + "\nwork: " +
              entry.work_task + "\nTime Worked: " +
              entry.timeworked + "\nNotes:\n" +
              entry.task_notes
              )
        print("\n")
        print('n) next entry')
        print('q) return to main menu')

        user = input("> ").lower()
        if user == "q":
            clear()
            break
        else:
            clear()
    if not entries:
        print("Sorry couldn't find that information")


def view_by_keyword(search_query=None):
    clear()
    entries = Entry.select().order_by()
    if search_query:
        entries = entries.where(
            Entry.name.contains(search_query) +
            Entry.task_notes.contains(search_query))

    for entry in entries:
        dateworked = entry.dateworked.strftime('%m/%d/%Y')
        clear()
        print(dateworked)
        print('='*len(dateworked))
        print("name: " + entry.name + "\nwork: " +
              entry.work_task + "\nTime Worked: " +
              entry.timeworked + "\nNotes:\n " +
              entry.task_notes
              )
        print("\n")
        print('n) next entry')
        print('q) return to main menu')

        user = input("> ").lower()
        if user == "q":
            clear()
            break
        else:
            clear()
    if not entries:
        clear()
        print("Sorry nothing was found")


def view_by_work_task(search_query=None):
    clear()
    entries = Entry.select().order_by()
    if search_query:
        entries = entries.where(
            Entry.work_task.contains(search_query))

    for entry in entries:
        dateworked = entry.dateworked.strftime('%m/%d/%Y')
        clear()
        print(dateworked)
        print('='*len(dateworked))
        print("name: " + entry.name + "\nwork: " +
              entry.work_task + "\nTime Worked: " +
              entry.timeworked + "\nNotes:\n" +
              entry.task_notes
              )
        print("\n")
        print('n) next entry')
        print('q) return to main menu')

        user = input("> ").lower()
        if user == "q":
            clear()
            break
        else:
            clear()
    if not entries:
        clear()
        print("Sorry nothing was found")


def menu():
    print("Enter q to Quit")
    print("\n")
    print("a) Add Entry")
    print("b) Search_Menu ")
    print("\n")


def search_menu():
    print("Enter r to Return q to Quit")
    print("\n")
    print("a) Search by Name")
    print("b) Search by Date")
    print("c) Search by Work")
    print("d) Search by Duration")
    print("e) Search by Keyword")
    print("\n")


# The Program
def run_program():
    while True:
        menu()
        user = input("Action: ").lower()
        clear()
        if user == 'a':
            user = input("Enter name: ")
            task_usr = input("Task: ")
            clear()
            time_usr = input("Enter Date 'MM/DD/YYY': ")
            user_min = input("Minutes MM: ")
            user_sec = input("Seconds SS: ")
            clear()
            print("Any notes: 'ctrl/d' to q ")
            notes_usr = sys.stdin.read().strip()
            add_entry(user, time_usr, task_usr, notes_usr, user_min, user_sec)
        if user == 'b':
            while True:
                search_menu()
                user = input("Action: ").lower()
                if user == 'a':
                    clear()
                    user = input("Search: ")
                    search_query(user)
                if user == 'b':
                    clear()
                    print("MM/DD/YYYY")
                    user = input("Search: ")
                    search_query_date(user)
                if user == 'd':
                    clear()
                    print("Enter how many minutes")
                    user_minutes = input("Search:  ")
                    print("\n")
                    print("Enter how many seconds")
                    user_seconds = input("Search:  ")
                    search_by_duration(user_minutes, user_seconds)
                if user == 'e':
                    clear()
                    user = input("Search: ")
                    search_by_keyword(user)
                if user == 'c':
                    clear()
                    user = input("Search: ")
                    view_by_work_task(user)
                if user == 'r':
                    clear()
                    break
                if user == 'q':
                    clear()
                    break
                else:
                    clear()
        if user == 'q':
            clear()
            print("Goodbye")
            break

if __name__ == '__main__':
    initialize()
    clear()
    run_program()
