#!/usr/bin/env python3
checklist = []
num_tasks = int(input("How many tasks do you want to add to your checklist today? "))

for i in range(num_tasks):
    task = input(f"Enter task {i+1}: ")
    checklist.append(task)

completed_tasks = []
incomplete_tasks = []

print("\nAt the end of the day, review your tasks.")
for task in checklist:
    status = input(f"Did you complete '{task}'? (y/n): ").strip().lower()
    if status == 'y':
        completed_tasks.append(task)
    else:
        incomplete_tasks.append(task)

with open("completed_tasks.txt", "w") as f:
    for task in completed_tasks:
        f.write(task + "\n")

with open("incomplete_tasks.txt", "w") as f:
    for task in incomplete_tasks:
        f.write(task + "\n")

print("\nCompleted tasks have been saved to completed_tasks.txt")
print("Incomplete tasks have been saved to incomplete_tasks.txt")