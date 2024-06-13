def find_category(number):
    #Determine the category based on the category in the file 
    if number == 0:
        return 'excellent'
    elif number == 1:
        return 'good'
    elif number == 2:
        return 'above average'
    elif number ==3:
        return 'average'
    elif number == 4:
        return 'below average'
    else:
        return 'poor'

vo2max = 48
age = 19
category = ''
f = open('vo2maxwomen.txt', 'r')
lines = f.readlines()
for line in lines:
    found = 0
    #Check if age category matches 
    if int(line.split(';')[0].split('-')[0]) <= age <= int(line.split(';')[0].split('-')[1]):
        #Check which vo2 max category matches and give a rating bsaed on position in file 
        found = 1
        for i in range(6):
            if int(line.split(';')[i+1].split('-')[0]) <= vo2max <= int(line.split(';')[i+1].split('-')[1]):
                category = find_category(i)
                break
            else:
                category = 'very poor'
                break

print (category)