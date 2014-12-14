import random
ph = [random.uniform(0, 14) for x in range(30000)]
temp = [random.uniform(55, 90) for x in range(30000)]
temp_file = open('temp.csv', 'w+')
ph_file = open('ph.csv', 'w+')
for x in range(len(temp)):
    temp_file.write("%.2f," % temp[x])
    ph_file.write("%.2f," % ph[x])
temp_file.close()
ph_file.close()
