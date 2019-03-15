'''
Created on Oct 30, 2017

@author: Ale
'''
from copy import deepcopy
from Tests import initList
from Functions import printList
from Functions import checkMultipleAdd
from Functions import checkAndRemoveTransaction
from Functions import checkMultipleReplace
from Functions import checkAndListTransaction
from Functions import checkSum
from Functions import sumType
from Functions import checkMax
from Functions import maxAmountPerType
from Functions import checkSort
from Functions import checkFilter
from Functions import checkUndo
from Functions import checkExit
from Functions import checkHelp


def helpCmd():
    print("Valid commands:")
    print("\t add <apartment> <type> <amount>") 
    print("\t remove <apartment>\t remove <start apartment> to <end apartment>\t remove <type>")
    print("\t replace <apartment> <type> with <amount>") 
    print("\t list\t list <apartment>\t list [ < | = | > ] <amount>")
    print("\t sum <type>\t max <apartment>")
    print("\t sort apartment\t sort type")
    print("\t filter <type>\t filter <value>")
    print("\t undo")
    print("\t help")
    print("\t exit")
    
def readCmd():
    
    """
    Read and parse user commands
    input - 
    output : the tuple (command, params)

    """
    cmd = raw_input("Enter a command: ")

    """
    Separate command and parameters

    """
    if cmd.find(" ") == -1:
        #No parameters (help/exit/list etc)
        command = cmd
        params = ""
    else:
        #Parameters found
        command = cmd[0:cmd.find(" ")]
        params = cmd[cmd.find(" ") + 1:]
        params = params.split(" ")
        for i in range(0, len(params)):
            params[i] = params[i].strip()
    return (command, params)
 
def start():
    
    transactionList = []
    undolist = []
    undoIndex = 0
    
    #Added a test list
    initList(transactionList)
    printList(transactionList)
    
    while True:
        cmd = readCmd()
        command = cmd[0]
        params = cmd[1]
                
        if command == 'add':
            # we add the current list to the undolist
            undolist.append(deepcopy(transactionList))
            undoIndex = undoIndex + 1
            if checkMultipleAdd(transactionList, params) == True:
                print("Valid transaction/s added")
            else:
                #if the adding wasn't done, we delete the last copy we made
                undolist.pop(undoIndex-1)
                undoIndex = undoIndex - 1
                print("Invalid parameters. No transaction added")
                
        elif command == 'remove':
            undolist.append(deepcopy(transactionList))
            undoIndex = undoIndex + 1
            if checkAndRemoveTransaction(transactionList, params) == True:
                print("Transaction/s removed")
            else:
                undolist.pop(undoIndex-1)
                undoIndex = undoIndex - 1
                print("Invalid parameters. No transaction removed")
                
        elif command == 'replace':
            undolist.append(deepcopy(transactionList))
            undoIndex = undoIndex + 1
            if checkMultipleReplace(transactionList, params) == True:
                print("Valid transaction/s replaced")
            else:
                undolist.pop(undoIndex-1)
                undoIndex = undoIndex - 1
                print("Invalid parameters. No transactions replaced")
                
        elif command == 'list':
            if checkAndListTransaction(transactionList, params) == False:
                print("Invalid parameters")
                
        elif command == 'sum':
            if checkSum(transactionList, params) == True:
                print(sumType(transactionList, params[0]))
            else:
                print("Invalid parameters")
                
        elif command == 'max':
            if checkMax(transactionList, params) == True:
                maxAmountPerType(transactionList, params[0])
            else:
                print("Invalid parameters")
                
        elif command == 'sort':
            if checkSort(transactionList, params) == False:
                print("Invalid parameters")
                
        elif command == 'filter':
            undolist.append(deepcopy(transactionList))
            undoIndex = undoIndex + 1
            if checkFilter(transactionList, params) == False:
                undolist.pop(undoIndex-1)
                undoIndex = undoIndex - 1
                print("Invalid parameters")
                
        elif command == 'undo':
            if checkUndo(params) == True:
                if len(undolist) > 0:
                    """
                    if there were some changes made to the list, we assign to our transactionList
                    her last form before the changes 
                    and then we delete the last list in undolist, which contained the last changes
                    """
                    transactionList = deepcopy(undolist[undoIndex-1])
                    undolist.pop(undoIndex-1)
                    undoIndex = undoIndex - 1
                    printList(transactionList)
                else:
                    #if not, we print out a message for the user
                    print("Already at oldest change")
            else:
                print("Invalid parameters")
              
        elif command  == 'help':
            if checkHelp(params) == True:
                helpCmd()
            else:
                print("Invalid parameters"
                      )
            
        elif command == 'exit':
            if checkExit(params) == True:
                print("Exited the program")
                break
            else:
                print("Invalid parameters")
        else:
            print("Not a valid command. Enter 'help' if you need some :)")
            
start()