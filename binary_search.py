#Binary search algorithm — returns index of a number in a list. Can be imported and used in other programs/websites etc. 
#Function parameters are numberList (list of numbers for finding target) and targetValue (number whose index is to be found)
#doSearch function returns index of targetValue

def doSearch(numberList,targetValue):
  min_index = 0
  max_index = len(numberList)-1
  guess = 0
  while max_index >= min_index:
    guess = round((max_index+min_index)/2)
    print("Index Searched: ", guess)
    if numberList[guess] == targetValue:
      return guess
    elif numberList[guess] < targetValue:
      min_index = guess+1
    else:
      max_index = guess-1
  return -1
