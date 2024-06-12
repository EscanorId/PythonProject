print('Welcome to BMI Calculator')
print()
tinggi = int(input('\nMasukkan tinggi badan : '))
berat = int(input('\nMasukkan berat badan : '))
print('--------------------------')

#Rumus BMI
calculate = berat / (tinggi**2)
BMI = (calculate * 100**2)

#kondisional
result = BMI
if BMI < 16:
  BMI = ('terlalu kurus')
elif 16 <= BMI <= 17:
  BMI = ('kurus')
elif 17 <= BMI <= 18.5:
  BMI = ('sedikit kurus')
elif 18.5 <= BMI <= 25:
  BMI = ('normal')
elif 25 <= BMI <= 30:
  BMI = ('kelebihan berat badan')
elif 30 <= BMI <= 35:
  BMI = ('obesitas kelas 1')
elif 35 <= BMI <= 40:
  BMI = ('obesitas kelas 2')
elif BMI > 40:
  BMI = ('obesitas kelas 3')
else:
  print('tidak diketahui')

#OUTPUT
print('Hasil BMI kamu adalah', result)
print('Kamu memiliki berat badan yang', BMI )
