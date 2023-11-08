note=input('Enter the musical note :')
if note[0] in ('A','B','C','D','E','F','G') :
    if 0<=int(note[1])<=8 :
        if note[0]=='A' :
            f=440.00
        elif note[0]=='B' :
            f=493.88
        elif note[0]=='C' :
            f=261.63
        elif note[0]=='D' :
            f=293.66  
        elif note[0]=='E' :
            f=329.63
        elif note[0]=='F' :
            f=349.23
        elif note[0]=='G' :
            f=392.00    
        F=f*(2**(4-int(note[1])))
        print(f'The frequency of {note} is {F}Hz')   
    else :
        print('That is the invalid parameter')     
else:
    print('That is the invalid parameter')
