'''
Created on Oct 28, 2017

@author: Ale
'''
   
def checkType(p):
    """
    checks if the type is a valid one
    input: the string we want to check
    output: True if it's valid, False otherwise
    """
    predefTypes = ["water", "gas", "heating", "electricity", "other"]
    for type1 in predefTypes:
        if p == type1:
            return True
            break
    return False

def checkAndAddTransaction(transactionList, params):
    """
    checks if the 'add' command was entered properly
    input: list, parameters
    output: True if the parameters were valid and the adding was made
            False otherwise
    """
    if len(params) == 3:
        if params[0].isdigit() ==True and checkType(params[1]) == True and params[2].isdigit() == True:
            #we make sure the user can't add the apartment "0" or the amount "0"
            if int(params[0]) > 0 and int(params[2]) > 0:
                addTransaction(transactionList, params)
                return True
        return False
        #the parameters are not valid
    return False    

def addTransaction(transactionList, params):
    """
    adds a valid transaction
    input: list, parameters
    output: -
            (this function does not return anything, it is called in checkAndAddTransaction
            if the adding can be done)
    """
    transactionList.append((str(params[0]), str(params[1]), int(params[2])))    

def checkMultipleAdd(transactionList, params):
    """
    checks if the command entered is a multiple command
    if so, it splits the command and calls the adding function for each transaction
    if not, the adding is done in the normal way
    input: list, parameters
    output: True if the parameters were valid and the adding was done
            False otherwise
    """
    ok = 0
    if len(params) > 3:
        i = 0
        while i < len(params):
            if checkAndAddTransaction(transactionList, params[i:i+3]) == True:
                ok = 1
            i = i + 3
        if ok == 1:
        #found at least one transaction that was added
            return True
        return False
    else:
        #if not, the adding is done in the normal way
        if checkAndAddTransaction(transactionList, params) == True:
        #the transaction was added
            return True
    return False

def findApartment(transactionList, apart):
    """
    checks if there is any transaction for the apartment entered
    input: list, parameters
    output: the position of the transaction we were searching
            if we haven't found it, it returns -1
    """
    pos = -1
    for i in range(0, len(transactionList)):
        t = transactionList[i]
        if t[0] == apart:
            pos = i
            break
    return pos 
    
def removeExpensesStartEnd(transactionList, start, end):
    """
    removes the expenses between 2 given apartments
    input: list, the start apartment and the end apartment
    output: True if the removing was done successfully
            False otherwise
    """
    ok = 0
    i = 0
    while i < len(transactionList):
        t = transactionList[i][0]
        if int(t) >= int(start) and int(t) <= int(end):
            transactionList.pop(i)
            ok = 1
        else:
            i = i + 1
    
    if ok == 1:
        return True
    return False

def removeExpensesType(transactionList, type1):
    """
    removes all the expenses with a given type
    input: list, the given type
    output: True if the removing was done successfully
            False otherwise
    """
    ok = 0
    for t in transactionList:
        if t[1] == type1:
            transactionList.remove(t)
            ok = 1
    if ok == 1:
        return True
    return False

def removeExpensesApart(transactionList, apart):
    """
    removes all the expenses for a given apartment
    input: list, the given apartment
    output: True if the removing was done successfully
            False otherwise
    """
    ok = 0
    for t in transactionList:
        if t[0] == apart:
            transactionList.remove(t)
            ok = 1
    if ok == 1:
        return True
    return False

def checkAndRemoveTransaction(transactionList, params):
    """
    checks if the 'remove' command was entered properly
    input: list, parameters
    output: True if the removing was done successfully
            False otherwise
    """
    if len(params) == 1: 
        if checkType(params[0]) == True: 
            #the parameter is a valid type    
            if removeExpensesType(transactionList, params[0]) == True:
                return True
            return False

        elif findApartment(transactionList, params[0]) == -1: 
    #the parameter is a given apartment but it doesn't have any transactions
            return False

        else:
    #the parameter is a valid given apartment
            if removeExpensesApart(transactionList, params[0]) == True:
                return True
            return False
        
    elif len(params) == 3:
        if params[1] == 'to' and findApartment(transactionList, params[0]) != -1 and findApartment(transactionList, params[2]) != -1:    
    #both of the given apartments exist
            if removeExpensesStartEnd(transactionList, params[0], params[2]) == True:
                return True
            return False

    #one or both of the given apartments does/do  not exist
        return False 
    #invalid number of parameters
    return False

def replaceTransaction(transactionList, apart, type1, value):
    """
    replaces the expense in a given transaction with a given value
    input: list, the apartment, the type of the transaction and the new amount
    output: True if the replacing was done successfully
            False otherwise
    """
    for t in transactionList:
        if t[0] == apart and t[1] == type1:
            transactionList.remove(t)
            transactionList.append((apart, type1, value))
            return True
    return False


def checkAndReplaceTransaction(transactionList, params):
    """
    checks if the 'replace' command was entered properly
    input: list, parameters
    output: True if the replacing was done successfully
            False otherwise
    """
    if len(params) == 4:
        if params[2] == 'with' and findApartment(transactionList, params[0]) != -1 and checkType(params[1]) == True and params[3].isdigit() == True and int(params[3]) > 0:
            if replaceTransaction(transactionList, params[0], params[1], int(params[3])) == True:
                return True
            return False
    return False

def checkMultipleReplace(transactionList, params):
    """
    checks if the command is a multiple one
    if so, it splits the command and calls the replacing function for each transaction
    if not, the replacing is done in the normal way
    input: list, parameters
    output: True if the replacing was done successfully
            False otherwise
    """
    ok = 0
    if len(params) > 4:
        i = 0
        while i < len(params):
            if checkAndReplaceTransaction(transactionList, params[i:i+4]) == True:
                ok = 1
            i = i + 4
        if ok == 1:
        #found at least one transaction that was replaced
            return True
        return False
    else:
        #if not, the replacing is done in the normal way
        if checkAndReplaceTransaction(transactionList, params) == True:
            #the replacing was done
            return True
        return False
    return False
        
def printList(transactionList): 
    """
    prints the list in a pretty way
    input: list
    output: A message if the list is empty
            prints the list otherwise      
    """
    if len(transactionList) > 0:
        for t in transactionList:
            print("Apartment: " + str(t[0]) + " Type: " + t[1] + " Expense: " + str(t[2]))
    else:
        print("Sorry. The list is empty")

def printListByApartment(transactionList, apart):
    """
    prints all the transactions for a given apartment
    input: list, the given apartment
    output: prints a list of transactions for an apartment
    """
    for i in range(0, len(transactionList)):
        t = transactionList[i]
        if t[0] == apart:
            print("Apartment: " + str(t[0]) + " Type: " + t[1] + " Expense: " + str(t[2]))

def checkOperand(operand):
    """
    checks if the operand is valid
    input: a string we want to check
    output: True if it is a valid one
            False otherwise
    """
    if operand == '<' or operand == '>' or operand == '=':
        return True
    return False

def sumOfExpenses(transactionList, apart):
    """
    returns the sum of expenses for an apartment
    input: list, the given apartment
    output: the sum
    """
    s = 0
    for i in range(0, len(transactionList)):
        t = transactionList[i]
        if t[0] == apart:
            s = s + t[2]
    return s

def printListOperands(transactionList, operand, value):
    """
    prints all the apartments which follow a certain criteria
    input: list, the given operand ( < | = | > ) and the given amount
    output: prints the given information if there was any
            returns -1 if not
    """
    ok = 0
    lst = []
    """
    we create a list in which we put each apartment as we find it
    if we already found an apartment once and we printed it, we make sure we don't print it again

    """
    for t in transactionList:
        if operand == '>' and sumOfExpenses(transactionList, t[0]) > value and t[0] not in lst:
            print("Apartment: " + str(t[0]) + " Expense: " + str(sumOfExpenses(transactionList, t[0])))
            ok = 1
            lst.append(t[0])
        elif operand == '<' and sumOfExpenses(transactionList, t[0]) < value and t[0] not in lst:
            print("Apartment: " + str(t[0]) +  " Expense: " + str(sumOfExpenses(transactionList, t[0])))
            ok = 1
            lst.append(t[0])
        elif operand == '=' and sumOfExpenses(transactionList, t[0])  == value and t[0] not in lst:
            print("Apartment: " + str(t[0]) +  " Expense: " + str(sumOfExpenses(transactionList, t[0])))
            ok = 1
            lst.append(t[0])
    if ok == 0:
        return -1

def checkAndListTransaction(transactionList, params):
    """
    checks if the 'list' command was entered properly
    input: list, parameters
    output: True if the listing was done successfully
            False otherwise
    """
    if len(params) == 0:
    #a simple print of the entire list
        printList(transactionList)
        return True

    elif len(params) == 1:
        if findApartment(transactionList, params[0]) != -1:
        #if the apartment exists, print all the expenses for it
            printListByApartment(transactionList, params[0])
            return True
        #no such apartment
        return False

    elif len(params) == 2:
        if checkOperand(params[0]) == True and params[1].isdigit() == True :
        #prints list according to the operand
            if printListOperands(transactionList, params[0], int(params[1])) != -1:
                return True
        #invalid parameters
        return False
    #invalid number of parameters
    return False

def sumType(transactionList, type1):
    """
    returns the sum of expenses for a given type, -1 otherwise
    input: list, the given type
    output: the sum
    """
    s = 0
    for t in transactionList:
        if t[1] == type1:
            s = s + t[2]
    return s
        
def checkSum(transactionList, params):
    """
    checks if the 'sum' command was entered properly
    input: list, parameters
    output: True if the command was valid
            False otherwise
    """
    if len(params) == 1:
        if checkType(params[0]) == True:
            #the type entered is valid
            sumType(transactionList, params[0])
            return True
        #invalid parameters
        return False
    #invalid number of parameters
    return False            

def sortApartments(transactionList):
    """
    sorts the list by apartment ascending by total amount of expenses
    """
    for i in range(0, len(transactionList) - 1):
        for j in range(i + 1, len(transactionList)):
            if sumOfExpenses(transactionList, transactionList[i][0]) > sumOfExpenses(transactionList, transactionList[j][0]):
                transactionList[i], transactionList[j] = transactionList[j], transactionList[i]

    printByApartment(transactionList)

def printByApartment(transactionList):
    """
    prints out the list of apartments sorted
    """
    print("Apartment: " + str(transactionList[0][0]) + " Expense: " + str(sumOfExpenses(transactionList, transactionList[0][0])))
    p = transactionList[0][0]
    for i in range(1, len(transactionList)):
        if transactionList[i][0] != p:
            print("Apartment: " + str(transactionList[i][0]) + " Expense: " + str(sumOfExpenses(transactionList, transactionList[i][0])))
        p = transactionList[i][0]
    
def sortType(transactionList):
    """
    sorts the list by type ascending by total amount of money
    """
    for i in range(0, len(transactionList) - 1):
                for j in range(i + 1, len(transactionList)):
                        if sumType(transactionList, transactionList[i][1]) > sumType(transactionList, transactionList[j][1]):
                                transactionList[i], transactionList[j] = transactionList[j], transactionList[i]
    printByType(transactionList)

def printByType(transactionList):
    """
    prints out the list of types sorted
    """
    print("Type: " + transactionList[0][1] + " Amount: " + str(sumType(transactionList, transactionList[0][1])))
    p = transactionList[0][1]
    for i in range(1, len(transactionList)):
        if transactionList[i][1] != p:
            print("Type: " + transactionList[i][1] + " Amount: " + str(sumType(transactionList, transactionList[i][1])))
        p = transactionList[i][1]

def checkSort(transactionList, params):
    """
    checks if the 'sort' command was entered properly
    input: list, parameters
    output: True if the sorting was done successfully
            False otherwise
    """
    if len(params) == 1:
        if params[0] == 'apartment':
            sortApartments(transactionList)
            return True
        elif params[0] == 'type':
            sortType(transactionList)
            return True
        #invalid parameters
        return False
    #invalid number of parameters
    return False

def maxExpense(transactionList, apart, type1):
    """
    returns the maximum amount for a certain type and apartment
    input: list, the given apartment and the given type
    output: the maximum amount
    """
    maxi = 0
    for t in transactionList:
        if t[0] == apart and t[1] == type1:
            if t[2] > maxi:
                maxi = t[2]
    return maxi

def maxAmountPerType(transactionList, apart):
    """
    writes the maximum amount per each type for an apartment given
    
     we create a list in which we put each type as we find it
         if we already found a type once and we printed it, we make sure we don't print it again 
    
    """
    typeList = list()
    for i in range(0, len(transactionList)):
        t = transactionList[i]
        if i == 0:
            if t[0] == apart:
                print("Type: " + t[1] + " Maximum: " + str(maxExpense(transactionList, t[0], t[1])))                
                typeList.append(t[1])
        
        elif t[0] == apart and t[1] not in typeList:
            print("Type: " + t[1] + " Maximum: " + str(maxExpense(transactionList, t[0], t[1])))
            typeList.append(t[1])
            
            
            
def checkMax(transactionList, params):
    """
    checks if the 'max' command was entered properly
    input: list, parameters
    output: True if the command was valid
            False otherwise
    """
    if len(params) == 1:
        if params[0].isdigit() == True and findApartment(transactionList, params[0]) != -1:
            return True
        #invalid parameters
        return False
    #invalid number of parameters
    return False

def filterByType(transactionList, type1):
    """
    keeps only the transactions for a given type
    input: list, the given type
    output: True if the list was modified
    """
    i = 0
    while i < len(transactionList):
        if transactionList[i][1] != type1 :
            transactionList.pop(i)
        else:
            i = i + 1
    if i != 0:
        #we did find something to filter
        return True

def filterByValue(transactionList, value):
    """
    keeps only the transactions smaller than a given value
    input: list, the given value
    output: True if the list was modified
    """
    i = 0
    while i < len(transactionList):
        if transactionList[i][2] >= value :
            transactionList.pop(i)
        else:
            i = i + 1
    if i != 0:
        #we did find something to filter
        return True
    
def checkFilter(transactionList, params):
    """
    checks if the 'filter' command was entered properly
    input: list, parameters
    output: True if the list was filtered
            False otherwise
    """
    if len(params) == 1:
        if checkType(params[0]) == True:
            #we have to filter by a given type
            if filterByType(transactionList, params[0]) == True:
                return True
        elif params[0].isdigit() == True:
            #we have to filter by a given value
            if filterByValue(transactionList, int(params[0])) == True:
                return True
        #invalid parameters 
        return False
    #invalid number of parameters  
    return False

def checkUndo(params):
    """
    checks if the 'undo' command was entered properly
    input: parameters
    output: True if the command is valid
            False otherwise
    """
    if len(params) == 0:
        return True
    return False
    
def checkExit(params):
    """
    checks if the 'exit' command was entered properly
    input: parameters
    output: True if the command is valid
            False otherwise
    """
    
    if len(params) == 0:
        return True
    return False

def checkHelp(params):
    """
    checks if the 'help' command was entered properly
    input: parameters
    output: True if the command is valid
            False otherwise
    """
    if len(params) == 0:
        return True
    return False
    