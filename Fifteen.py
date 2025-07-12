import re
pattern = r'^([A-Z][a-z]*)\s+([A-Z][a-z]*)'
# Pattern captures Firstname Lastname at the beginning of a sentence.

A = "Jane Doe is eating breakfast."
B = "L Zhang is a great Broadway actor."
C = "Ling-Ling practices violin 40 hours a day."
D = "Today is John Doe's birthday."

fname_lname = re.findall(pattern, A) + re.findall(pattern, B) + re.findall(pattern, C) + re.findall(pattern, D)
# Finds all occurrences of the pattern in the sentences A, B, C, and D.
print(fname_lname)