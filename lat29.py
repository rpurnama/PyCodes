# lat29.py

negara = set(['brazil', 'rusia', 'indonesia'])

print("indonesia" in negara)
print("amerika" in negara)

negara2 = negara.copy()
negara2.add('korea')

print(negara2.issuperset(negara))

negara.remove('rusia')

print(negara2 & negara)
print(negara2.intersection(negara))