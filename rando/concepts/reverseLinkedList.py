from unicodedata import digit
import re, os
class Node:

    #Node constructor
    def __init__(self, data):
        #contain only the piece of data
        self.data = data
        #and that next
        self.next = None

class LinkedList:
    #Initialize
    def __init__(self):
        #on initialization, head is empty
        self.head = None

    #TODO: Insert node at head
    def push(self, new_data):
        
        #create temp node
        new_node = Node(new_data)
        
        #assign the 'next' position of the temp as the current head
        new_node.next = self.head

        #merge nodes
        self.head = new_node

    #Print the linked list
    def printList(self):
        #Create temporary list
        temp = self.head
        #Empty string to be printed
        listStr = ""
        #While there is a next node
        while(temp):
            #Add the head to the fron of the print list
            listStr+="->{0}".format(temp.data)
            #Take next node
            temp = temp.next
        #Pretty printing
        print(listStr[2:len(listStr)+1])

    #Reverses the list
    def reverse(self):
        #Previous is none
        prev = None

        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

if __name__ == '__main__':
    llist = LinkedList()
    os.system('cls' if os.name=='nt' else 'clear')
    num = input("Enter a value to add to the LinkedList, or enter 'r' to reverse the list:\n")

    while(num != 'r'):

        while(not num):
            os.system('cls' if os.name=='nt' else 'clear')
            num = input("Try again and enter a proper value.\n")
            x = re.findall('\D', num.lower())
        if(num == 'r'): break
        x = re.findall('\D', num.lower())
        
        while x:
            os.system('cls' if os.name=='nt' else 'clear')
            if(num =='r'): break
            num = input("Try again and enter a proper value.\n")
            while(not num):
                os.system('cls' if os.name=='nt' else 'clear')
                num = input("Try again and enter a proper value.\n")
                if(num == 'r'): break
                x = re.findall('\D', num.lower())
                
            x = re.findall('\D', num.lower())
        if(num == 'r'): break
        llist.push(int(num))
        os.system('cls' if os.name=='nt' else 'clear')
        num = input("Enter another value (to the head of the list) or 'r'\n")
    
    os.system('cls' if os.name=='nt' else 'clear')
    print("Given list:")
    llist.printList()
    llist.reverse()
    print("Reversed List")
    llist.printList()
    print('\n\n')