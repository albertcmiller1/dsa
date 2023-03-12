dic1 = {
    'value': 11
}

dic2 = dic1 

print("before value is updated: ")
print(f"dic1 = {dic1} @ {id(dic1)}")
print(f"dic2 = {dic2} @ {id(dic2)}")
print("\n")

dic2['value'] = 22

print("after update")
print(f"dic1 = {dic1} @ {id(dic1)}")
print(f"dic2 = {dic2} @ {id(dic2)}")

'''
dic1 and dic2 point to the same place ! 
'''