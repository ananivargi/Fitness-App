def category(number):
    #Determine the category based on the range in the file 
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

vo2max = 58
age = 19
range = ''
f = open('vo2maxwomen.txt', 'r')
lines = f.readlines()
for line in lines:
    #Check if age range matches 
    if int(line.split(';')[0].split('-')[0]) <= age <= int(line.split(';')[0].split('-')[1]):
        #Check which vo2 max range matches and give a rating bsaed on position in file 
        for i in range(6):
            #print (int(line.split(';')[i+1].split('-')[1])) 
            if int(line.split(';')[i+1].split('-')[0]) <= vo2max <= int(line.split(';')[i+1].split('-')[1]):
                print ((line.split(';')[i+1].split('-')[0]))
                range = category()
            else:
                range = 'very poor'