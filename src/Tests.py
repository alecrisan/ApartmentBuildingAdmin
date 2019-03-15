'''
Created on Oct 30, 2017

@author: Ale
'''

from Functions import checkMultipleAdd
from Functions import checkAndRemoveTransaction
from Functions import checkMultipleReplace
from Functions import checkSum
from Functions import sumType
from Functions import checkMax
from Functions import checkSort
from Functions import checkFilter
from Functions import checkType
from Functions import checkAndAddTransaction
from Functions import findApartment
from Functions import removeExpensesApart
from Functions import removeExpensesType
from Functions import removeExpensesStartEnd
from Functions import replaceTransaction
from Functions import checkAndReplaceTransaction
from Functions import maxExpense
from Functions import sumOfExpenses
from Functions import checkOperand
from Functions import filterByType
from Functions import filterByValue
from Functions import checkAndListTransaction
from Functions import checkUndo
from Functions import checkExit
from Functions import checkHelp

def initList(transactionList):
    transactionList.append(('1', 'gas', 200))
    transactionList.append(('2', 'water', 50))
    transactionList.append(('4', 'other', 145))
    transactionList.append(('6', 'gas', 193))
    transactionList.append(('10', 'electricity', 20))
    transactionList.append(('11', 'heating', 200))
    transactionList.append(('3', 'gas', 12))
    transactionList.append(('4', 'other', 99))
    transactionList.append(('2', 'water', 100))
    transactionList.append(('1', 'heating', 140))
    transactionList.append(('4', 'other', 300))



def testcheckType():
    
    assert checkType('gas')
    assert not checkType('ajksdn')
    assert checkType('other')
    assert not checkType('34')

def testcheckAndAddTransaction():
    testList = []
    initList(testList)

    assert checkAndAddTransaction(testList, ('7', 'water', '290'))
    assert not checkAndAddTransaction(testList, ('20', 'dasd', '100'))
    assert not checkAndAddTransaction(testList, ('2', 'gas'))

def testcheckMultipleAdd():
    testList = []
    initList(testList)

    assert checkMultipleAdd(testList, ('2', 'water', '67', '5', 'gas', '190'))
    assert not checkMultipleAdd(testList, ('2', 'ga', '45', '-5', 'wat', '56'))
    
def testfindApartment():    
    testList = []
    initList(testList)

    assert findApartment(testList, '2') == 1
    assert findApartment(testList, '25') == -1

def testcheckAndRemoveTransaction():
    testList = []
    initList(testList)

    assert checkAndRemoveTransaction(testList, ('2'))
    assert checkAndRemoveTransaction(testList, ('1', 'to', '4'))
    assert checkAndRemoveTransaction(testList, ('6'))
    assert not checkAndRemoveTransaction(testList, ('3', 'to', '7'))
    assert not checkAndRemoveTransaction(testList, ('waater'))

def testremoveExpensesApart():
    testList = []
    initList(testList)

    assert removeExpensesApart(testList, '10')
    assert not removeExpensesApart(testList, 'abc')
    assert not removeExpensesApart(testList, '25')
    assert not removeExpensesApart(testList, ('1', '3'))

def testremoveExpensesType():
    testList = []
    initList(testList)

    assert removeExpensesType(testList, 'gas')
    assert not removeExpensesType(testList, '34')    
    assert not removeExpensesType(testList, 'bcsjn')
    assert not removeExpensesType(testList, ('1', 'gas'))

def testremoveExpensesStartEnd():
    testList = []
    initList(testList)

    assert removeExpensesStartEnd(testList, '2', '4')
    assert not removeExpensesStartEnd(testList, '24', '2')

def testreplaceTransaction():
    testList = []
    initList(testList)

    assert replaceTransaction(testList, '10', 'electricity', '67')
    assert not replaceTransaction(testList, '3', 'water', '10')

def testcheckAndReplaceTransaction():
    testList = []
    initList(testList)
    
    assert checkAndReplaceTransaction(testList, ('1', 'gas', 'with', '150'))
    assert not checkAndReplaceTransaction(testList, ('1', 'gas', '150'))
    assert not checkAndReplaceTransaction(testList, ('3', 'gas', 'wit', '34'))

def testcheckMultipleReplace():
    testList = []
    initList(testList)

    assert checkMultipleReplace(testList, ('6', 'gas', 'with', '45', '1', 'heating', 'with', '23'))
    assert not checkMultipleReplace(testList, ('6', 'gaaas', 'with', '56', '4', 'heating', 'wit', '34'))

def testsumType():
    testList = []
    initList(testList)

    assert sumType(testList, 'gas') == 405
    assert sumType(testList, 'da') == 0

def testcheckSum():
    testList = []
    initList(testList)

    assert not checkSum(testList, '43')
    assert not checkSum(testList, 'gasss')

def testcheckAndListTransaction():
    testList = []
    initList(testList)
    
    assert not checkAndListTransaction(testList, '48 8')
    assert not checkAndListTransaction(testList, '====')
    
    
def testmaxExpense():
    testList = []
    initList(testList)

    assert maxExpense(testList, '2', 'water') == 100
    assert maxExpense(testList, '4', 'gas') == 0

def testcheckMax():
    testList = []
    initList(testList)

    assert checkMax(testList, '2')
    assert not checkMax(testList, '20')
    assert not checkMax(testList, 'a')

def testsumOfExpenses():
    testList = []
    initList(testList)

    assert sumOfExpenses(testList, '2') == 150
    assert sumOfExpenses(testList, '6') == 193
    assert sumOfExpenses(testList, '7') == 0

def testcheckOperand():
    assert checkOperand(">")
    assert not checkOperand("!")
    assert checkOperand("=")

def testcheckSort():
    testList = []
    initList(testList)

    assert not checkSort(testList, ('2', 'apartment'))
    assert not checkSort(testList, 'dada')

def testcheckFilter():
    testList = []
    initList(testList)

    assert not checkFilter(testList, ('3', 'gas'))
    assert not checkFilter(testList, 'pap')

def testfilterByType():
    testList = []
    initList(testList)
    
    assert filterByType(testList, 'other')
    assert not filterByType(testList, 'da')

def testfilterByValue():
    testList = []
    initList(testList)

    assert filterByValue(testList, '100')
    assert filterByValue(testList, '400')

def testcheckUndo():

    assert not checkUndo('gh')
    assert checkUndo('')
    assert not checkUndo('f 6 7')
    
def testcheckExit():
    
    assert not checkExit('fsd')
    assert checkExit('')
    assert not checkExit('g 45 3')
    
def testcheckHelp():
    
    assert not checkHelp('sadhjb')
    assert checkHelp('')
    assert not checkHelp('9 gas r3')
    
def runAllTests():
    testcheckType()
    testcheckAndAddTransaction()
    testcheckMultipleAdd()
    testfindApartment()
    testremoveExpensesStartEnd()
    testremoveExpensesType()
    testremoveExpensesApart()
    testcheckAndRemoveTransaction()
    testreplaceTransaction()
    testcheckAndReplaceTransaction()
    testcheckMultipleReplace()
    testcheckOperand()
    testsumOfExpenses()
    testsumType()
    testcheckSum()
    testcheckAndListTransaction()
    testcheckSort()
    testmaxExpense()
    testcheckMax()
    testcheckFilter()
    testfilterByType()
    testfilterByValue()
    testcheckUndo()
    testcheckExit()
    testcheckHelp()
    
runAllTests()