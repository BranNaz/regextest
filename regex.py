### Regex project

# Use python to read the file regex_test.txt and print the last name on each line using 
# regular expressions and groups (return None for names with no first and last name, 
# or names that aren't properly capitalized)
##### Hint: use with open() and readlines()

import re

f = open('files2/regex_test.txt')
names = f.read()
names = re.compile('[A-Z][a-zA-Z]+)[A-Z][a-zA-Z]+')
found = names.findall('Madonna','programming is cool')
print(found)

f.close()


