class ChangeStr:
    """This class is working with string type of variables.

    It has nice functions with gorgeous documentary. Have a great day!

    """

    @staticmethod  # This method adds different symbol in end of line.
    def set_dot(line):  # This is the name of method.
        symbol = '.'  # This is the initialization of symbol variable.
        return line+symbol  # Return the finish result.
        # That is all.


new_c = ChangeStr()
print(ChangeStr.set_dot('test'))

