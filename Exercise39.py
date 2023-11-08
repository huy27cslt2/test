Noise=int(input(f'Enter the noise level in decibels(dB):'))
a,b,c,d=("Jackhammer","Gas lawnmower","Alarm clock","Quiet room")
if Noise==130: 
    print(f'The noise of {a}')
elif Noise==106: 
    print(f'The noise of {b}')
elif Noise==70: 
    print(f'The noise of {c}')
elif Noise==40: 
    print(f'The noise of {d}')
elif Noise<40 :
    print(f'Sound is below quiet room level')  
elif Noise>130 : 
    print(f'Value larger than {a}')
elif 106<Noise<130: 
    print(f'Noise is between {a} and {b}')
elif 70<Noise<106: 
    print(f'Noise is between {b} and {c}')
elif 40<Noise<70: 
    print(f'Noise is between {c} and {d}')
       
    

    