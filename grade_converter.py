# FILE NAME - grade_converter.py

# NAME: Matthew Brassie 
# DATE: October 1
# BRIEF DESCRIPTION:  



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



########## ENTER YER CODE BELOW THIS LINE ##########


print("===== Grade Converter =====")

num = float(input("Enter a numerical grade (1-100): "))

if num > 100:
    print("A+")

elif 100 >= num >= 90:
    print("A")

elif 90 > num >= 80:
    print("B")

elif 80 > num >= 70:
    print("C")

elif 70 > num >= 65:
    print("D")

elif num < 65:
    print("F")

########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################

'''
===== Grade Converter =====
Enter a numerical grade (1-100): 101
A+
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): -78
F
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): 64
F
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): 65
D
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): 66
D
'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What is something you would tell a future student to be careful about when
   doing this lab?







'''
