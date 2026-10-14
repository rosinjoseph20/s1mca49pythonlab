s=input("enter a string:")
if s.endswith('ing'):
    ns=s+'ly'
else:
    ns=s+'ing'
print("Modified string:",ns)
