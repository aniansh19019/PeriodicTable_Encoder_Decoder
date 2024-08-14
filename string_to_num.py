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
    def get_numeber_case_sensitive(self,operand):
        num_str =""
        try:
            while operand != "":
                if operand[0].islower():
                    return None
                next_symbol = operand[0]
                tocut = 1
                if len(operand) >= 2 and operand[1].islower():
                    next_symbol = operand[0:2]
                    tocut = 2
                operand = operand[tocut:]
                next_num = self.get_number(next_symbol)
                if next_num == "":
                    return None
                num_str += next_num
        except:
            return None
        return num_str
    
    def populate(self):
        case_sensitive_value = self.get_numeber_case_sensitive(self.head.operand)
        if case_sensitive_value is not None:
            print("case senstive number: ",case_sensitive_value)
            self.valid_outcomes.append(case_sensitive_value)
        else:
            print("no case sensitive number found")
        self.routine(self.head)
        self.valid_outcomes = list(set(self.valid_outcomes))


print("Enter string to encode:")
name = input()
tree = EncodeTree(name)
tree.populate()
print("Possible Encodings:")
print(tree.valid_outcomes)
