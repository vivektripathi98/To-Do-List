#import sqlite3 as sql   
def main():
    tasks=[] # this task varible as ana array that will add array and remvoe it 

    def addTask(intask):
        tasks.append(intask)
        return tasks

    def removeTask(outTask):
        tasks.pop(outTask-1)
        return tasks

    def displayTask():
        x=1
        print("these are the task")
        if len(tasks)!=0:
            for task in tasks:
                print(str(x)+". "+ task)
                x+=1
        else:
            print("There is no task")


    while True:
        #displayTask()

        operation=input("Enter the Choice ")
        if(operation=='1'):
            adTask=input("Enter the Task need to addd ")
            addTask(adTask)
        elif(operation=='2'):
            remTask=int(input("Enter the Task number need to remvoe "))
            removeTask(remTask)
        elif(operation=='3'):
            disTask=input("Enter the Task need to Display ")
            displayTask()
            break
        else:
            print("You have entered the Wrong option")
       
if __name__ == "__main__":
    main()