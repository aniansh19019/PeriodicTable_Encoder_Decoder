from mendeleev import element

class EncodeTreeNode:
    def __init__(self, content, operand):
        self.content=content
        self.single = None
        self.double = None
        self.operand = operand

class EncodeTree:

    def __init__(self, number):
        # assert type(number) == String, "Invalid type for number"

        self.head = EncodeTreeNode("", number) # empty node as head
        self.number=number
        self.valid_outcomes = []

    def get_number(self, element_symbol):
        try:
            return str(element(element_symbol.capitalize()).number)
        except:
            return ""

        return ""


    def routine(self, node):
        # print(node.content)
        if node.operand == "": # empty operand, chain finished
            self.valid_outcomes.append(node.content) # add to the list of valid outcomes
            return
        # assign new nodes and call recursive routine on each routine

        if len(node.operand) >= 1: # assign single
            addend = self.get_number(node.operand[0])
            if addend == "": # invlaid element, interrupt chain
                return
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
num = input()
tree = EncodeTree(num)
tree.populate()
print("Possible Encodings:")
print(tree.valid_outcomes)