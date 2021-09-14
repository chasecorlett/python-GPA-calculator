"""Chase Corlett
CSCI 101 - Section C
Create Project - GPA Calculator"""
import csv
#prompt for file input and give user status message
print('Please enter the name of your CSV file containing your grades and credit hours\nfor each class (row 1 should contain the grade percentages and row 2 the\ncorresponding credit hours, each value separated by only a single comma)')
file = input('FILE> ')
print('Thank you, now calculating your current GPA')

#define all functions
def read(file):
    with open(file, 'r') as csvfile:
        read = csv.reader(csvfile)
        contents = list(read)
        csvfile.close()
    return contents

def split(lst, index):
    out_lst = []
    for i in lst[index]:
        out_lst.append(i)
    return out_lst

def calc_gpa(grade_lst, point_lst):
    weight_lst = []
    point_total = 0
    earned_total = 0
    count = 0
    for i in grade_lst:
        if float(i) < 60:
            earned_total = earned_total
        elif 60 <= float(i) <= 69.99:
            earned_total += float(point_lst[count])
        elif 70 <= float(i) <= 79.99:
            earned_total += 2 * float(point_lst[count])
        elif 80 <= float(i) <= 89.99:
            earned_total += 3 * float(point_lst[count])
        elif 90 <= float(i):
            earned_total += 4 * float(point_lst[count])
        count += 1
    for i in point_lst:
        point_total += float(i)
    gpa = round(earned_total / point_total, 2)
    return gpa

#use functions to pull/ format necessary info to calclulate GPA
gpa = calc_gpa(split(read(file), 0), split(read(file), 1))

#write the output file containing a short message and the calculated GPA and close it
GPA_file = open('Your_GPA.txt', 'w')
GPA_file.write('Your GPA is %s' %gpa)
GPA_file.close()

#write output in Python and give user message informing them of the new file
print('Your GPA is %s' %gpa)
if 0 < gpa < 2:
    print('Maybe consider seeking some academic advising and/or tutoring')
elif 2 <= gpa < 3:
    print("You're doing good, keep plugging along!")
elif 3 <= gpa < 3.8:
    print("You're doing great, nice work!")
elif 3.8 < gpa:
    print('Wow! Great job, got any pro tips for me?')
elif gpa == 0:
    print('Ouch. How??')
print("You can now find your gpa saved as 'Your_GPA.txt'")
