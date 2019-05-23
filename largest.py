ahal=int(input())
kani=int(input())
kiru=int(input())
if((ahal>=kani)and (ahal>=kiru)):
  print(ahal)
elif((kani>=ahal)and (kani>=kiru)):
  print(kani)
else:
  print(kiru)    
