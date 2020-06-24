import matplotlib.pyplot as plt
import numpy
x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78]
y = [472,698,785,1781,1477,1755,2010,2127,2603,2838,3239,3915,3721,3173,3437,2676,3001,2546,2035,14153,5151,2662,2097,2132,2003,1852,516,977,996,978,554,862,741,992,1292,1503,1989,1981,1858,2573,2298,3111,3625,4049,3892,4390,4567,7266,8295,10907,11059,13036,12920,15730,20682,26145,30692,29452,32480,41493,43835,48557,60994,64553,66761,60415,61786,73792,77053,80097,101736,84821,71502,74044,85116,84447,85638,94629]
plt.scatter(x, y)
plt.show()

sum_until_now=0
for i in y:
    sum_until_now=sum_until_now+i

print("No.of confirmed cases until now i.e (DAY 1-78): ",sum_until_now)
mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))
myline = numpy.linspace(1, 78, 100)
plt.scatter(x, y)
plt.plot(myline, mymodel(myline),color='r',marker='o')
plt.show()

from sklearn.metrics import r2_score
mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))
print(r2_score(y, mymodel(x)))
mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

# confirmed = mymodel(100)
# print(confirmed)

confirmed=0
for i in range(79,99,1):
    confirmed=confirmed+mymodel(i)
    print("Estimated Confirmed cases on day ",i," :   ",mymodel(i))
print("Total Estimated confirmed cases at the end of april from 11/04/20 : ",confirmed)    
print("Total Estimated confirmed cases at the end of april : ",confirmed+sum_until_now)    

