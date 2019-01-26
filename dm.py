import math
const = (math.pi/180)
print("%70s"%'Delta Modulation of Sinusoidal Wave')
w = int(input('Enter the frequency of input signal(rad/s)\n'))  #frequncy
a = int(input('Enter the amplitude of sin wave\n'))     #amplitude
fi = int(input('Enter the phase angle(in degrees)\n'))  #phase
sf = int(input('Enter the sampling frequency\n'))      #sampling frequency
if sf < 1:
    print('Error')
    exit(1)
print('Input Signal -')
print('%dsin(%dt+rad(%d))'%(a, w, fi))
t = 0.0
theta = w*t+fi*const
val = []
add = 1/sf
for i in range(sf):
    val.append(a*math.ceil(math.sin(w*t+fi*const)*100)/100)
    t += add
print('Sampled values (for one time period)- ')
print(val)
print('Encoded binary message')
print(0, end=' ')
prev = 0
for i in range(1, sf):
    if val[i]-val[i-1] > 0:
        print(1, end=' ')
        prev = 1
    elif val[i]-val[i-1] < 0:
        print(0, end=' ')
        prev = 0
    else:
        print(prev, end=' ')
x = input('\nPress enter to exit\n')
