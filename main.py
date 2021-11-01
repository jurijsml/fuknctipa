"""
Uzraksti funkciju, kura atgriež vērtību True, ja abi dotie vārdi sākas ar vienu burtu
"""
"""
sakas_vienadi("Liela Lama") -----> True
sakas_vienadi("Maza Lama") ------> False
"""

"""
Noderīgas metodes:

.split()
.lower()
"""

def sakas_vienadi(teksts):
  teksts = teksts.lower().split()

if teksts[0][0] == teksts [1][0]:
  return True
else:
  return False

print(sakas_vienadi("Liela Lama"))
print(sakas_vienadi("Maza Lama"))

def sakas_vienadi(teksts):
  teksts = teksts.lower().split()

  return teksts [0][0] == teksts[1][0]

print(sakas_vienadi("Liela Lama"))
print(sakas_vienadi("Maza Lama"))