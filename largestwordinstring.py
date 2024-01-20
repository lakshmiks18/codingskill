print("enter the string")
text=input()
text=text.split()
bigWordLen=0

for wrd in text:
    wrdLen=len(wrd)
    if wrdLen > bigWordLen:
        bigWordLen=wrdLen
print("\n Largest word:")
for wrd in text:
    wrdLen=len(wrd)
    if wrdLen==bigWordLen:
        print(wrd)
