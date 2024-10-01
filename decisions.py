'''
Get two integers x and y from the user and write a program to relate 2 integers as equal to, less than or greater than.
Input format:
Input consist of 2 integers
The first input corresponds to  the first number.(a)
The second input corresponds to the second number.(b)
Output format:
If the first number is equal to the second number, print "x and y are equal". Otherwise, print "x greater than y" or "x less than y"
Sample Input:
6
8
Sample Output:
6 less than 8
'''
def main():
    # Input the two integers
    x = int(input())
    y = int(input())
    
    # Compare the integers and print the result
    if x == y:
        print(f"{x} and {y} are equal")
    elif x > y:
        print(f"{x} greater than {y}")
    else:
        print(f"{x} less than {y}")

if __name__ == "__main__":
    main()

'''
)Write a program to check whether the given character is vowel or consonant.
Input format:
The input consist of a character
Output format:
The output consists of a below-given string
“Vowel” / “Consonant” / “Not an alphabet”
Sample Input:
e

Sample Output:
Vowel
'''
Ans:
a=input()
if(a=='a' or a=='e' or a=='i' or a=='o' or a=='u'):
    print('Vowel')
elif(a>'a' and 'a'<a):
    print("Consonant")
else:
    print("Not an alphabet")


'''
The newly appointed Vice-Chancellor of Anna University wanted to create an automated grading system for the students to check their grade. When a student enters a mark, the grading system displays the corresponding grade.
Write a program to solve the given problem.
  Marks scored  
  Grade 
100
S
90 - 99
A
80 - 89
B
70 - 79
C
60 - 69
D
50 - 59
E
<50
F

Input format:
The input consists of one integer which corresponds to the marks scored by the student

Output format:
If a student marks greater than 100, print "Invalid Input". Otherwise, print the grade.
Sample Input:
78
Sample Output:C
'''
def main():
    # Input marks scored
    marks = int(input())
    
    # Check for invalid input
    if marks > 100:
        print("Invalid Input")
    else:
        # Determine the grade based on the marks
        if marks == 100:
            grade = "S"
        elif 90 <= marks < 100:
            grade = "A"
        elif 80 <= marks < 90:
            grade = "B"
        elif 70 <= marks < 80:
            grade = "C"
        elif 60 <= marks < 70:
            grade = "D"
        elif 50 <= marks < 60:
            grade = "E"
        else:
            grade = "F"
        
        # Output the grade
        print(grade)

if __name__ == "__main__":
    main()

'''
 A fruit seller buys a dozen of banana at Rs.X. He sells 1 banana at Rs.Y. Write a program to determine the profit or loss in Rs. for the fruitseller.
Input format:
Input consists of 2 floating point numbers
The first input corresponds to the total cost(X)
The second input corresponds to the sold cost(Y)
Output format:
Print "Profit or Loss" with Rupees.
Sample Input:
60
4
Sample Output:
Loss : Rs.12.00
'''
def main():
    # Input total cost for a dozen bananas
    total_cost = float(input())
    
    # Input selling price for one banana
    selling_price_per_banana = float(input())
    
    # Calculate the total selling price for a dozen bananas
    total_selling_price = selling_price_per_banana * 12
    
    # Determine profit or loss
    profit_or_loss = total_selling_price - total_cost
    
    # Output the result
    if profit_or_loss > 0:
        print(f"Profit : Rs.{profit_or_loss:.2f}")
    elif profit_or_loss < 0:
        print(f"Loss : Rs.{-profit_or_loss:.2f}")
    else:
        print("No Profit No Loss")

if __name__ == "__main__":
    main()

'''
Write a program to determine the fee amount to be collected from a student. 
Refer the table below for fee details.
  Student Type  
  Student Type denoted as  
  Fee Details  
Merit Seat Day Scholar
MSDS

Tuition fee + Bus fee



Merit Seat Hosteller
MSH
Tuition fee + Hostel fee

Management Seat Day Scholar



MGSDS

150% of Tuition fee + Bus fee



Management Seat Hosteller
MGSH

150% of Tuition fee + Hostel fee




Input format:
The first input corresponds to the student type
The second input corresponds to the tuition fee
The third input corresponds to the bus fee or hostel fees
Output format:
Print the total fee amount of the corresponding student with 2 decimal places.
Refer below sample output for formatting
Sample Input:
MSH
40000
50000
Sample Output:
90000.00
'''
def main():
    # Input student type
    student_type = input().strip()
    
    # Input tuition fee
    tuition_fee = float(input().strip())
    
    # Input bus or hostel fee
    additional_fee = float(input().strip())
    
    # Initialize total fee
    total_fee = 0.0

    # Determine total fee based on student type
    if student_type == "MSDS":
        total_fee = tuition_fee + additional_fee  # Tuition fee + Bus fee
    elif student_type == "MSH":
        total_fee = tuition_fee + additional_fee  # Tuition fee + Hostel fee
    elif student_type == "MGSDS":
        total_fee = (1.5 * tuition_fee) + additional_fee  # 150% of Tuition fee + Bus fee
    elif student_type == "MGSH":
        total_fee = (1.5 * tuition_fee) + additional_fee  # 150% of Tuition fee + Hostel fee
    else:
        print("Invalid student type")
        return
    
    # Output the total fee formatted to 2 decimal places
    print(f"{total_fee:.2f}")

if __name__ == "__main__":
    main()


'''
Ask a user for their birth year encoded as two digits (like "62") and for the current year, also encoded as two digits (like "99"). Write a program to find the users current age in years.
Input format:
Input consists of 2 integers
The first integer corresponds to the last 2 digits of the birth year
The second integer corresponds to the last 2 digits of the current year
Output format:
Print the user's current age
Refer below sample output for formatting.
Sample Input:
62
00
Sample Output:
38
'''
def main():
    # Input last two digits of the birth year
    birth_year = int(input().strip())
    
    # Input last two digits of the current year
    current_year = int(input().strip())
    
    # Calculate the full years
    # Assuming birth year is in the 1900s or 2000s
    if current_year < birth_year:
        current_year += 100  # Assume the current year is in the next century
    
    age = current_year - birth_year
    
    # Output the user's current age
    print(age)

if __name__ == "__main__":
    main()


'''
There are 3 labs in the CSE department(L1, L2, and L3) with a seating capacity of x, y, and z respectively. Find the lab which has minimal seating capacity.  
Input format:
Input consists of 3 integers
The first input denotes the seating capacity of L1(a)
The second input denotes the seating capacity of L2(b)
The third input denotes the seating capacity of L3(c)
Output format:
Print the minimal seating lab capacity
Refer the Sample output for formatting
Sample Input:
30
40
20
Sample Output:
L3
'''
L1=int(input())
L2=int(input())
L3=int(input())
if((L1<L2) and (L1<L3)):
    print("L1")
elif(L2<L3 and L2<L1):
    print("L2")
else:
    print("L3")


'''
There are 3 labs in the CSE department are L1, L2, and L3 with a seating capacity of x, y, and z respectively. One of the 3 labs has been allocated for ACE training. Out of the available labs, find the lab which has minimal seating capacity.
Input format:
Input consists of 3 integers and a string
The first input denotes the seating capacity of L1(a)
The second input denotes the seating capacity of L2(b)
The third input denotes the seating capacity of L3(c)
The fourth input denotes the lab which is allocated for ACE training
Output format:
Print the minimal seating capacity lab amongst the available labs.
Refer the Sample output for formatting
Sample Input:
30
40
20
L3
Sample Output:
L1
'''
def main():
    # Input seating capacities for labs L1, L2, and L3
    a = int(input().strip())  # Capacity of L1
    b = int(input().strip())  # Capacity of L2
    c = int(input().strip())  # Capacity of L3
    allocated_lab = input().strip()  # Lab allocated for ACE training

    # Initialize a dictionary to hold lab names and their capacities
    labs = {
        "L1": a,
        "L2": b,
        "L3": c
    }

    # Remove the allocated lab from consideration
    if allocated_lab in labs:
        del labs[allocated_lab]

    # Find the lab with the minimal seating capacity
    min_lab = min(labs, key=labs.get)
    
    # Output the lab with the minimal seating capacity
    print(min_lab)

if __name__ == "__main__":
    main()


'''
There are 3 labs in the CSE department are L1, L2, and L3 with a seating capacity of x, y, and z. A single lab needs to be allocated to a class of 'n' students. How many of the 3 labs can accommodate 'n' students?
Input format:
Input consists of 4 integers
The first input denotes the seating capacity of L1(a)
The second input denotes the seating capacity of L2(b)
The third input denotes the seating capacity of L3(c)
The fourth input denotes the number of students(x)
Output format:
Print the number of labs which can accommodate the 'n' number of students
Refer the Sample output for formatting
Sample Input:
30
40
20
25
Sample Output:
2 
'''
def main():
    # Input seating capacities for labs L1, L2, and L3
    a = int(input().strip())  # Capacity of L1
    b = int(input().strip())  # Capacity of L2
    c = int(input().strip())  # Capacity of L3
    n = int(input().strip())   # Number of students

    # Initialize count of labs that can accommodate 'n' students
    count = 0

    # Check each lab's capacity against the number of students
    if a >= n:
        count += 1
    if b >= n:
        count += 1
    if c >= n:
        count += 1

    # Output the number of labs that can accommodate 'n' students
    print(count)

if __name__ == "__main__":
    main()

'''

 There are 3 labs in the CSE department. The labs are L1, L2, and L3 with a seating capacity of x, y, and z respectively. A single lab needs to be allocated to a class of 'n' students. The labs need to be utilized to the maximum i.e the number of systems used should not be minimal. Which lab needs to be allocated to this class?
Input format:
Input consists of 4 integers
The first input denotes 'x'
The second input denotes 'y'
The third input denotes 'z'
The fourth input denotes 'n'
Output format:
Print the lab which is suitable for  'n' number of students
Refer the Sample output for formatting
Sample Input:
30
40
20
25
Sample Output:
'''
def main():
    # Input seating capacities for labs L1, L2, and L3
    a = int(input().strip())  # Capacity of L1
    b = int(input().strip())  # Capacity of L2
    c = int(input().strip())  # Capacity of L3
    n = int(input().strip())   # Number of students

    # Initialize count of labs that can accommodate 'n' students
    count = 0

    # Check each lab's capacity against the number of students
    if a >= n:
        count += 1
    if b >= n:
        count += 1
    if c >= n:
        count += 1

    # Output the number of labs that can accommodate 'n' students
    print(count)

if __name__ == "__main__":
    main()
