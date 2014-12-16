import random
ph = [random.uniform(0, 14) for x in range(300000)]
temp = [random.uniform(55, 90) for x in range(300000)]
readings_file = open('/home/rob/aquarimeter-web/readings.csv', 'w+')
for x in range(len(temp)):
   readings_file.write("%.2f,%.2f\n" % (temp[x],ph[x]))
readings_file.close()   