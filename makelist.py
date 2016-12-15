# open file called list.txt in write mode

file = open('list.txt', 'w')

# Repeat this ten times:
    # Take user input
    # Write user input to a file
    
count = 1
while count < 11:
    usersay = input("Input " + str(count) + ": ")
    file.write(usersay + "\n")
    count += 1
    
# Close file

file.close()