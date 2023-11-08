F=float(input('Enter Frequency(Hz):'))
note= False
if -1<= F-440 <=1 :
    note='A4'
elif -1<=F-493.88<=1 :
    note='B4'
elif -1<=F-261.63<=1 :
    note='C4'        
elif -1<=F-293.66<=1 :
    note='D4'
elif -1<=F-329.63<=1 :
    note='E4'
elif -1<=F-349.23<=1 :
    note='F4'
elif -1<=F-392.00<=1 :
    note='G4'
else:
    print('No data on the entered frequency')
if note != False :
    print(f'The frequency {F}Hz belongs to the note {note}')    
            
                  