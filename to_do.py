#To do list
def to_do():


        while True:
            print("\nMY TO DO LIST!!")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Complete Task")
            print("4. Delete Task")
            print("5. Exit")
            
            i=input("enter a number")

            if i=="1":
                a=input("Enter the task: ")
                with open ("To_do.txt","a") as f1:
                    f1.write(a + "\n")
                print("TASK ADDED!!")

            elif i=="2":
                with open ("To_do.txt","r") as f1:
                    n=f1.readlines()
                if not n:
                    print("No task found")
                else:
                    print("\nYour Tasks:")
                    for index, task in enumerate(n, start=1):
                        print(f"{index}. {task.strip()}")


            elif i=="3":
                with open ("To_do.txt","r") as f1:
                    k=f1.readlines()
                if not k:
                    print("No task found")
                else:
                    for index in range(len(k)):
                        print(f"{index + 1}. {k[index].strip()}")
                    try:
                        j = int(input("Enter task number to mark as complete: ")) - 1
                        if 0 <= j < len(k):
                                if "[Completed]" not in k[j]:
                                        k[j] = k[j].strip() + "[Completed]\n"
                                        with open("To_do.txt", "w") as f1:
                                                f1.writelines(k)
                                        print("Task marked as completed ")
                                else:
                                        print("Invalid task number ")
                    except ValueError:
                        print("Please enter a valid number ")


            elif i=="4":
                with open ("To_do.txt","r") as f1:
                    g=f1.readlines()
                if not g:
                    print("No task found")
                else:
                    for index in range(len(g)):
                        print(f"{index + 1}. {g[index].strip()}")
                    try:
                        j = int(input("Enter task number to delete: ")) - 1
                        if 0 <= j < len(g):
                            del g[j] 
                            with open("To_do.txt", "w") as f1:
                                f1.writelines(g)
                            print("Task deleted ")
                        else:
                            print("Invalid task number ")
                    except ValueError:
                        print("Please enter a valid number ")

            

                
            elif i=="5":
                print("Thank you!")
                break
to_do()
