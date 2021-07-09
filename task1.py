import re
row=input("\nInput your string: ")
print("\nYour string is: ", row)
extract_letter=" ".join(re.split("[0-9]+", row))
extract_number="".join(re.split("[a-zA-Z]+", row))
extract_com_let=", ".join(extract_letter.split())
extract_com_num=", ".join(extract_number.split())
print("\nAll numbers: ", str(extract_com_num))
print("\nAll words between numbers: ", str(extract_com_let))
for let in extract_letter.split():
    print("\nCapital first letter and last of each word: ", let[0].upper() + let[1:-1].lower() + let[-1].upper(), end="\n")
new_num_max=list(map(int, extract_number.split()))
max_num=max(new_num_max)
print("\nMaximum element from numbers is: ", max_num)
for element in new_num_max:
    if element != max_num:
        element=element**new_num_max.index(element)
        print("\nnumbers power to its index: ", element)
    else:
        continue
