# code to convert a string(if possible) to a sequence of numbers where each number is an atomic number of an element represented by the string tokens extracted from the original string in order
from mendeleev import element

class EncodeTreeNode:
    def __init__(self, content, operand):
        self.content = content
        self.single = None
        self.double = None
        self.operand = operand

class EncodeTree:

    def __init__(self, number):
        self.head = EncodeTreeNode("", number) # empty node as head
        self.valid_outcomes = []

    def get_number(self, element_symbol):
        try:
            return str(element(element_symbol.capitalize()).atomic_number)+" "
        except:
            return ""
        return ""


    def routine(self, node):
        if node.operand == "": # empty operand, chain finished
            self.valid_outcomes.append(node.content) # add to the list of valid outcomes
            return
        # assign new nodes and call recursive routine on each routine

        if len(node.operand) >= 1: # assign single
            addend = self.get_number(node.operand[0])
            if addend != "": # invlaid element, try next
                node.single = EncodeTreeNode(node.content + addend, node.operand[1:])
                self.routine(node.single)

        if len(node.operand) >=2: #assign double
            addend = self.get_number(node.operand[0:2])
            if addend == "": # invlaid element, interrupt chain
                return
            node.double = EncodeTreeNode(node.content + addend, node.operand[2:])
            self.routine(node.double)

        return

    def populate(self):
        self.routine(self.head)


print("Enter string to encode:")
name = input()
tree = EncodeTree(name)
tree.populate()
print("Possible Encodings:")
print(tree.valid_outcomes)
