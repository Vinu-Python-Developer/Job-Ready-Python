def get_daily_tasks():
    tasks = input("Enter three things you did today, separated by commas: ")
    return tasks

def show_tasks(tasks):
    print("\n📝 Here are your tasks for today:")
    for i, task in enumerate(tasks.split(','), start=1):
        print(f"Task {i}: {task.strip()}")

def give_encouragement(tasks):
    if tasks.strip():  # making sure it's not just empty or spaces
        print("\n🌟 Well done! You're making progress!")
    else:
        print("\n⛔ You haven’t entered any tasks yet.")

# Main program starts here
daily_tasks = get_daily_tasks()
show_tasks(daily_tasks)
give_encouragement(daily_tasks)
