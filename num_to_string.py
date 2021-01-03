from mendeleev import element

class DecodeTreeNode:
    def __init__(self, content, operand):
        self.content=content
        self.single = None
        self.double = None
        self.triple = None
        self.operand = operand

class DecodeTree:

    def __init__(self, number):
        # assert type(number) == String, "Invalid type for number"

        self.head = DecodeTreeNode("", number) # empty node as head
        self.number=number
        self.valid_outcomes = []

    def get_symbol(self, element_number):
        if int(element_number)<=118 and element_number[0] != "0":
            return element(int(element_number)).symbol
        return ""


    def routine(self, node):
        # print(node.content)
        if node.operand == "": # empty operand, chain finished
            self.valid_outcomes.append(node.content) # add to the list of valid outcomes
            return
        # assign new nodes and call recursive routine on each routine

        if len(node.operand) >= 1: # assign single
            addend = self.get_symbol(node.operand[0])
            if addend == "": # invlaid element, interrupt chain
                return
            node.single = DecodeTreeNode(node.content + addend, node.operand[1:])
            self.routine(node.single)

        if len(node.operand) >=2: #assign double
            addend = self.get_symbol(node.operand[0:2])
            if addend == "": # invlaid element, interrupt chain
                return
            node.double = DecodeTreeNode(node.content + addend, node.operand[2:])
            self.routine(node.double)

        if len(node.operand) >=3: #assign triple
            addend = self.get_symbol(node.operand[0:3])
            if addend == "": # invlaid element, interrupt chain
                return
            node.triple = DecodeTreeNode(node.content + addend, node.operand[3:])
            self.routine(node.triple)

        return

    def populate(self):
        self.routine(self.head)


print("Enter number to decode/encode:")
num = input()
tree = DecodeTree(num)
tree.populate()
print("Possible Encodings:")
print(tree.valid_outcomes)
