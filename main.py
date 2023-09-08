#Old code reused to check for float
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
    if num != ".":  #accounts for singular "." input which caused the code to crash
      try:
        float(num)
      except ValueError:
        return False
        
      if float(num) >= 0 and num[0] != ".":
        return True
      else:
        return False
    else:
      return False
  else:
    return False



check = 0
global GENDER  #Getting gender of user
while check == 0:
  GENDER = input("Please enter your gender (F or M): ")
  if GENDER == "F" or GENDER  == "M":
    check = 1
  else:
    print("\nPlease enter a valid response.\n")


#Initializing lists of parts for men and women in lists

Men = ["Chest Skinfold (mm)","Abdomen Skinfold (mm)","Thigh Skinfold (mm)","Age (Year)",
       "Waist Circumference (m)", "Forearm Circumference (m)"]

Women = ["Triceps Skinfold (mm)","Thigh Skinfold (mm)","Suprailiac Skinfold (mm)","Age (Year)",
         "Gluteal Circumference (cm)"]


#initializing empty list, for acquired measurements from user

measurements_got = []


#women_body_density = 1.1470292-0.0009376*skin_fold_sum+0.0000030 *(skin_fold_sum**2)-0.0001156 *age -0.0005839 *gluteal_circumference


#initialize new list to save which gender list we need.

measurements_needed = []

if GENDER == "M":  #Since we have not picked which gender list we need, this code uses the previous women and men lists and saves the corresponding one to the measurements_needed list
  measurements_needed = Men
else:
  measurements_needed = Women



for part in measurements_needed:    #This code stores the users inputted measurements to measurements_got
  checker = 0
  while checker == 0: 
    if part == "Age (Year)":
      measurement = input("\nPlease enter your age (Year): ")
    else:
      measurement = input("\nPlease enter the measurement for your " + part + ": ")
    
    if not isfloat(measurement):
        checker = 0
    else:
      checker = 1
      measurements_got.append(float(measurement))


if GENDER == "M": #calculation for MEN

  #initializing each necessary variable for equation
  sum_of_skinfolds = measurements_got[0] + measurements_got[1] + measurements_got[2]
  age = measurements_got[3]
  waist_circumference = measurements_got[4]  #We can simply index the location of the values in the list, since we had the user enter them in the same order as the corresponding gender list
  Forearm_circumference = measurements_got[5]

  skinfoldpt1 = (0.0008209 * sum_of_skinfolds) #The following lines were created to break up the orginal equation, because it was too large to fit on one line.
  skinfoldpt2 = (0.0000026 * (sum_of_skinfolds ** 2))
  agept = (0.0002017 * age)
  waistpt = (0.005675 * waist_circumference)
  forearmpt = (0.018586*Forearm_circumference)

  #actual calculation takes place
  
  body_density = 1.0990750 - skinfoldpt1 + skinfoldpt2 - agept - waistpt +forearmpt

  

else: #else statements refers to WOMEN
  skin_fold_sum = measurements_got[0] + measurements_got[1] + measurements_got[2]
  age = measurements_got[3] #indexing / summing values
  gluteal_circumference = measurements_got[4]

  skin_foldpt1 = (0.0009376 * skin_fold_sum)  #original equation did not fit on one line.
  skin_foldpt2 = (0.0000030 * (skin_fold_sum ** 2))
  agept = (0.0001156 * age)
  glutpt = (0.0005839 * gluteal_circumference)

  body_density = 1.1470292 - skin_foldpt1 + skin_foldpt2 - agept - glutpt




body_fat_percentage = (495 / body_density) - 450 #siri calculation takes place here
print(f"\nYour body fat percentage is {body_fat_percentage:.2f}%") #print out body fat %, rounded to 2 decimals.

#women_body_density = 1.1470292-(0.0009376*skin_fold_sum)+(0.0000030 *(skin_fold_sum**2))-(0.0001156 *age) - (0.0005839 *gluteal_circumference)


#male_body_density = 1.0990750 - (0.0008209 * sum_of_skinfolds) + (0.0000026 * (sum_of_skinfolds ** 2)) - (0.0002017 * age)-(0.005675*waist_circumference)+(0.018586*Forearm_circumference)


