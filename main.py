#my old code
def isfloat(num):
  period = 0
  for a in num:
    if a == ".":
      period = period + 1
    elif a.isdigit():
      pass
    else: 
      return False
  if period <= 1:
    if float(num) >= 0:
      return True
    else:
      return False
  else:
    return False



check = 0
global GENDER
while check == 0:
  GENDER = input("Please enter your gender (F or M): ")
  if GENDER == "F" or GENDER  == "M":
    check = 1
  else:
    print("Please enter a valid response.")


Men = ["Chest Skinfold (mm)","Abdomen Skinfold (mm)","Thigh Skinfold (mm)","Age (Year)",
       "Waist Circumference (m)", "Forearm Circumference (m)"]

Women = ["Triceps Skinfold (mm)","Thigh Skinfold (mm)","Suprailiac Skinfold (mm)","Age (Year)",
         "Gluteal Circumference (cm)"]

measurements_got = []


#women_body_density = 1.1470292-0.0009376*skin_fold_sum+0.0000030 *(skin_fold_sum**2)-0.0001156 *age -0.0005839 *gluteal_circumference



measurements_needed = []

if GENDER == "M":
  measurements_needed = Men
else:
  measurements_needed = Women

measurements_got = []


for part in measurements_needed:    
  checker = 0
  while checker == 0: 
    if part == "Age":
      measurement = input("Please enter your age: ")
    else:
      measurement = input("Please enter the measurement for your " + part + ": ")
    
    if not isfloat(measurement):
        checker = 0
    else:
      checker = 1
      measurements_got.append(float(measurement))


if GENDER == "M":
  sum_of_skinfolds = measurements_got[0] + measurements_got[1] + measurements_got[2]
  age = measurements_got[3]
  waist_circumference = measurements_got[4]
  Forearm_circumference = measurements_got[5]

  skinfoldpt1 = (0.0008209 * sum_of_skinfolds)
  skinfoldpt2 = (0.0000026 * (sum_of_skinfolds ** 2))
  agept = (0.0002017 * age)
  waistpt = (0.005675 * waist_circumference)
  forearmpt = (0.018586*Forearm_circumference)

  body_density = 1.0990750 - skinfoldpt1 + skinfoldpt2 - agept - waistpt +forearmpt

  

else:
  skin_fold_sum = measurements_got[0] + measurements_got[1] + measurements_got[2]
  age = measurements_got[3]
  gluteal_circumference = measurements_got[4]

  skin_foldpt1 = (0.0009376 * skin_fold_sum)
  skin_foldpt2 = (0.0000030 * (skin_fold_sum ** 2))
  agept = (0.0001156 * age)
  glutpt = (0.0005839 * gluteal_circumference)

  body_density = 1.1470292 - skin_foldpt1 + skin_foldpt2 - agept - glutpt


body_fat_percentage = (495 / body_density) - 450
print(f"Your body fat percentage is {body_fat_percentage:.2f}%")

#women_body_density = 1.1470292-(0.0009376*skin_fold_sum)+(0.0000030 *(skin_fold_sum**2))-(0.0001156 *age) - (0.0005839 *gluteal_circumference)


#male_body_density = 1.0990750 - (0.0008209 * sum_of_skinfolds) + (0.0000026 * (sum_of_skinfolds ** 2)) - (0.0002017 * age)-(0.005675*waist_circumference)+(0.018586*Forearm_circumference)


