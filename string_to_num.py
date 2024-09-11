# code to convert a string(if possible) to a sequence of numbers where each number is an atomic number of an element represented by the string tokens extracted from the original string in order
from mendeleev import element
import sys

class EncodeTreeNode:
    def __init__(self, content, operand):
        self.content = content
        self.single = None
        self.double = None
        self.triple = None
        self.operand = operand

class EncodeTree:

    def __init__(self, number):
        self.head = EncodeTreeNode("", number) # empty node as head
        self.valid_outcomes = []

    def get_number(self, element_symbol, check_case = False):
        if check_case:
            if not (element_symbol[0].isupper() and (element_symbol[1:].islower() or len(element_symbol) == 1)):
                return ""

        try:
            return str(element(element_symbol.capitalize()).atomic_number)+" "
        except:
            return ""
        return ""


    def routine(self, node, check_case=False):
        if node.operand == "": # empty operand, chain finished
            self.valid_outcomes.append(node.content) # add to the list of valid outcomes
            return
        # assign new nodes and call recursive routine on each routine

        if len(node.operand) >= 1: # assign single
            addend = self.get_number(node.operand[0], check_case)
            if addend != "": # valid element, continue
                node.single = EncodeTreeNode(node.content + addend, node.operand[1:])
                self.routine(node.single, check_case)

        if len(node.operand) >=2: #assign double
            addend = self.get_number(node.operand[0:2], check_case)
            if addend != "": # valid element, continue
                node.double = EncodeTreeNode(node.content + addend, node.operand[2:])
                self.routine(node.double, check_case)

        if len(node.operand) >=3: #assign triple
            addend = self.get_number(node.operand[0:3], check_case)
            if addend != "": # valid element, continue
                node.triple = EncodeTreeNode(node.content + addend, node.operand[3:])
                self.routine(node.triple, check_case)


    def populate(self, check_case=False):
        self.routine(self.head, check_case)


print("Enter string to encode:")
name = input()
print("case sensitive? y/n")
check_case = input()
if check_case == "y":
    check_case = True
elif check_case == "n":
    check_case = False
else:
    print("Invalid input! Please try again!")
    sys.exit(-1)

tree = EncodeTree(name)
tree.populate(check_case)
print("Possible Encodings:")
print(tree.valid_outcomes)
