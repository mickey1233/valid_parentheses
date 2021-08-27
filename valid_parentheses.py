def Valid_Parentheses(s):
    blanket_list = []
       for blanket in s:
            if blanket == "(" or blanket == "{" or blanket == "[":
                blanket_list.append(blanket)
            else:
                # print(blanket_list)
                if blanket_list:
                    # print(blanket_list)
                    blanket1 = blanket_list.pop()
                    if ord(blanket1) == ord(blanket) - 1 or ord(blanket1) == ord(blanket) - 2:
                        # print(ord(blanket1) == ord(blanket) + 1)
                        continue
                    else:
                        # print(blanket_list)
                        return False
                else:
                    return False
        if blanket_list:
            return False
        else:
            return True


def main():
    Valid_Parentheses("()")
    Valid_Parentheses("()[]{}")
    Valid_Parentheses("(]")
    Valid_Parentheses("([)]")
    Valid_Parentheses("{[]}")


if __name__ == 'main':
    main()
