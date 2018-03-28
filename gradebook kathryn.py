Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> math_grade =int(input("What is your math grade?"))
science_grade = int(input("What is your science grade?"))
history_grade = int(input("What is your history grade?"))
english_grade = int(input("What is your english grade?"))
french_grade = int(input("What is your french grade?"))

grade_list = [math_grade,science_grade,history_grade,english_grade,french_grade]

average = (sum)(grade_list)/5
print average

grade_list.append(average)
grade_list.append("average")
print grade_list
print average

if average < 60:
    print "Below average, keep working."
elif average >= 60 and average <70:
    print "Almost there! keep working."
elif average >=70 and average <80:
    print "You're doing great!"
elif average >=80 and average <90:
    print "You're working hard! Keep going."
elif average >=90 and average <100:
    print "Nice job! You're excedding way above average."
