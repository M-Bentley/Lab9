############################################
#                                          # 
#                   70pt                   #
#                                          #
############################################

# Create a celcius to fahrenheit calculator.
# Multiply by 9, then divide by 5, then add 32 to calculate your answer.

# TODO:
# Ask user for Celcius temperature to convert
# Accept user input 
# Calculate fahrenheit
# Output answer

print 'What temperature do you wish to convert to Fahrenheit?'
userInput = float(raw_input())

output = float(((userInput * 9)/5)+32)
print output,"F"
