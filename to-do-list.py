# todo_list.py

class Task:
    def __init__(self, name, due_date=None):
        self.name = name
        self.due_date = due_date
        self.completed = False
        self.pending=True
        

    def mark_as_completed(self):
        self.completed = True

    def mark_as_non_completed(self):
        self.completed = False
        
    def mark_as_pending(self):
        self.pending = True

    def __str__(self):
        return f"{self.name} ({'Completed' if self.completed else 'Pending'})"

todo_list = []

def add_task(name, due_date=None):
    c=0
    if(len(todo_list)==0):
            todo_list.append(Task(name, due_date))
    else:
        for task in todo_list:
            if(task.name!=name):
                c+=1
            else:
                c=-1
        if(c!=-1):
            todo_list.append(Task(name, due_date))
        else:
            print("                              Please enter a different name,task with this name already exists! ")

def update_task(name,comp):
    length=len(todo_list)
    if(length!=0):
        for task in todo_list:
            if(task.name==name):
                if(comp=="yes"):
                    task.mark_as_completed()
                elif(comp=="no"):
                    task.mark_as_non_completed()
                    task.mark_as_pending()
    else:
        print("                              No list exists to be updated, please add first!")

def remove_cat(cat):
    if(len(todo_list)==0):
        print("                              No existing task to be removed, please save the task first!")
        return
    elif(cat.lower()=="completed"):
        todo_list[:] = [task for task in todo_list if not task.completed]
    elif cat.lower() == "pending":
        todo_list[:] = [task for task in todo_list if task.completed]
    elif(cat.lower()=="all"):
        todo_list.clear()
    else:
        print("                 Please enter valid operation!")

def remove_task(name):
    
    if(len(todo_list)==0):
        print("                              No existing task to be removed, please save the task first!")
    else:
        for task in todo_list[:]:  # Create a copy of the list using slicing
            if task.name == name:
                todo_list.remove(task)
        if name not in [task.name for task in todo_list]:
            print("                          No such task exists!")
        return todo_list
            
     

def display_tasks(cat):
    if(len(todo_list)==0):
        print("                              No existing tasks to be displayed, please save the task first!")
    elif(cat.lower()=="completed"):
        for task in todo_list:
            if(task.completed==True):
                print(task)
    elif(cat.lower()=="pending"):
        for task in todo_list:
            if(task.completed==False):
                print(task)
    elif(cat.lower()=="all"):
        for task in todo_list:
            print(task)
        

# main code:
while True:
    s=input("                    Enter the task which you want to perform(if nothing enter 0): ")
    r=s.lower()
    if(r=="0"):
        break
    elif(r=="add"):
        name=input("Enter the name of the task to be added: ")
        time=int(input("Enter the due date: "))
        add_task(name,time)
    elif(r=="update"):
        name=input("Enter the name of the task to be updated: ")
        upd=input("Enter Yes if completed else No: ")
        update=upd.lower()
        update_task(name,update)
    elif(r=="remove"):
        category=input("Choose the category of tasks that are to be removed(1(for specific task)/completed/pending/all(for all tasks)): ")
        if(category=="1"):
            name=input("Enter the name of the task to be removed: ")
            remove_task(name)
        else:
            remove_cat(category)
    elif(r=="display"):
        category=input("Choose the category of tasks that are to be printed(completed/pending/all(for all tasks)): ")
        display_tasks(category)
    else:
        print('                             No such action can be performed!')
    print("\n")