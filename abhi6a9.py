str1="{} {} {}".format('Work','Is','Worship')
print("String in default order:")
print(str1)

str1="{1} {0} {2}".format('Work','Is','Worship')
print("\nString in Positional order: ")
print(str1)

str1="{l} {f} {g}".format(g = 'Work', f ='Is', l ='Worship')
print("\nString in order of keywords:")
print(str1)

str1="{0:b}".format(12)
print("\nBinary representation of 12 is ")
print(str1)

str1="{0:e}".format(154.6347)
print("\nExponent representation of 154.6347 is")
print(str1)

str1="{0:.2f}".format(1/4)
print("\nOne-fourth is :")
print(str1)

str1="|{:<10}|{:^10}|{:>10}|".format('Work','Is','Worship')
print("\nLeft, center and right alignment with Formatting:")
print(str1)
print
