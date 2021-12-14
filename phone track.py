photos={"camera":10,"whatsapp images":25,"Pinterest":1,"screenshots":100}
photos["B612"]=10
photos["WeChat"]=7
photos["snapseed"]=5       
photos["candycamera"]=9

print(photos)
if isinstance(photos,dict)==True:
    print("entry is correct")
else :
    raise TypeError("entered datatype is wrong")
for i in photos.items():
    print(i)

Snapchat={"Reels":10}
Snapchat["Filter"]=10
Snapchat["Chat"]=7
Snapchat["Roll"]=5       
Snapchat["camera"]=9
Snapchat["Photos"]=30    
print(Snapchat)
if isinstance(Snapchat,dict)==True:
    print("Entry is correct")
else:
    raise TypeError("The datatype is wrong")
for i in Snapchat.items():
    print(i)
