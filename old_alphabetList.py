# Name: Natalie Lim Kit Ee
# ID: 2201845
# Class: DAAA/2B/03

#parent class
class Node:
    def __init__(self, letter):
        self.letter = letter
        self.count = 0 #not private as securoty not compromised since it is hard to deduce message from letter count
        self.nextNode = None


#child class for every letter of the alphabet
class AlphabetList(Node):
    def __init__(self):
        self.letters = [Node(chr(i)) for i in range(ord('A'), ord('Z')+1)]

    #setter to count number of occurrences of a letter
    def setCount(self, text):
        for letter in text:
            if letter.isalpha():
                letter = letter.upper()
                for node in self.letters:
                    if node.letter == letter:
                        node.count += 1
    
    #getter to return count of letter
    def getLetterCount(self, letter):
        letter = letter.upper()
        for node in self.letters:
            if node.letter == letter:
                return node.count

    #getter to return total count of all letters
    def getTotalCount(self):
        return sum(node.count for node in self.letters)

    #getter to return each letter
    def getLetters(self):
        return [node.letter for node in self.letters]


class SortedList:
    def __init__(self):
        self.headNode = None
        self.currentNode = None
        self.length = 0

    #returns everything in sortedList (not needed in the code right now but if needed for future use)
    def __str__(self):
        alphacount = []
        node = self.resetForIteration()
        while node != None:
            node = self.nextNode()
            alphacount.append(node)
        return alphacount

    def __appendToHead(self, newNode):
        oldHeadNode = self.headNode
        self.headNode = newNode
        self.headNode.nextNode = oldHeadNode
        self.length += 1

    def insert(self, newNode):
        self.length += 1
        #if list is currently empty
        if self.headNode == None:
            self.headNode = newNode
            return

        #check if it is going to be new head based on count
        if newNode.count > self.headNode.count:
            self.__appendToHead(newNode)
            return
        elif newNode.count == self.headNode.count:
            #compare based on alphabetical order if count is same
            if newNode.letter < self.headNode.letter:
                sellf.__appendToHead(newNode)
                return 

        #check if going to be inserted between any pair of Nodes (left, right)
        leftNode = self.headNode
        rightNode = self.headNode.nextNode
        
        while rightNode != None:
            if newNode.count > rightNode.count:
                leftNode.nextNode = newNode
                newNode.nextNode = rightNode
                return
            elif newNode.count == rightNode.count:
                if newNode.letter < rightNode.letter:
                    leftNode.nextNode = newNode
                    newNode.nextNode = rightNode
                    return

            leftNode = rightNode
            rightNode = rightNode.nextNode
        #added at tail (less than all other nodes) 
        leftNode.nextNode = newNode

    #getter to return top 5 in sortedList
    def getTop5(self):
        top5 = []
        count = 0

        node = self.resetForIteration()
        while node != None and count < 5:
            node = self.nextNode()
            top5.append(node)
            count += 1
        return top5

    def resetForIteration(self):
        self.currentNode = self.headNode
        if self.currentNode != None:
            return self.currentNode
        else:
            return None

    def nextNode(self):
        if self.currentNode != None:
            data = self.currentNode
            self.currentNode = self.currentNode.nextNode
            return data
        return None