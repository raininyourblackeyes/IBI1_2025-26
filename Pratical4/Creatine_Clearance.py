# Step 1: Validate Age (positive integer, 1 ≤ age ≤ 99)
# LOOP indefinitely:
while True:
    # PROMPT user to enter age (as integer)
    age = int(input("What's your age?"))
    # IF age is greater than 0 AND less than 100:
    if 0 < age < 100:
        # EXIT the age validation loop
        break
    # ELSE:
    else:
        # PRINT error message: "The age is wrong. Please enter a number between 1 and 99."
        print("The age is wrong. Please enter a number between 1 and 99.")

# Step 2: Validate Weight (numeric value, 20 < weight < 80 kg)
# LOOP indefinitely:
while True:
    # PROMPT user to enter weight (as floating-point number)
    weight = float(input("What's your weight(kg)?"))
    # IF weight is greater than 20 AND less than 80:
    if 20 < weight < 80:
        # EXIT the weight validation loop
        break
    # ELSE:
    else:
        # PRINT error message: "The weight is wrong. Please enter a number between 20 and 80."
        print("The weight is wrong. Please enter a number between 20 and 80.")

# Step 3: Validate Gender (only Male/Female, ignore leading/trailing whitespace)
# LOOP indefinitely:
while True:
    # PROMPT user to enter gender (as string)
    sex = input("What's your gender?(Male/Female)")
    # CONVERT input to string type and remove all leading/trailing whitespace
    sex = str(sex).strip()
    # IF processed gender is "Male" OR "Female":
    if sex in ["Male", "Female"]:
        # EXIT the gender validation loop
        break
    # ELSE:
    else:
        # PRINT error message: "The gender is wrong. Please enter Male or Female."
        print("The gender is wrong. Please enter Male or Female.")

# Step 4: Validate Creatine Concentration (numeric value, 0 < concentration < 100 μmol/L)
# LOOP indefinitely:
while True:
    # PROMPT user to enter creatine concentration (as floating-point number)
    creatine_conc = float(input("What's your creating concentration(μmol/L)?"))
    # IF concentration is greater than 0 AND less than 100:
    if 0 < creatine_conc < 100:
        # EXIT the concentration validation loop
        break
    # ELSE:
    else:
        # PRINT error message: "The creatine concentration is wrong. Please enter a number between 0 and 100."
        print("The creatine concentration is wrong. Please enter a number between 0 and 100.")

# Step 5: Calculate Creatine Clearance (CrCl) with gender-specific formula
# IF validated gender is "Male":
if sex == "Male":
    # CrCl = [(140 - age) * weight] / (72 * creatine_concentration)
    CrCl = ((140 - age)*weight)/(72*creatine_conc)
# ELSE (gender is Female):
else:
    # CrCl = [(140 - age) * weight * 0.85] / (72 * creatine_concentration)
    CrCl = ((140 - age)*weight)*0.85/(72*creatine_conc)

# Step 6: Output the calculated Creatine Clearance result
# CONVERT CrCl value to string type
# PRINT the result with message: "The creatine clearance is [CrCl value]"
print("The creatine clearance is", str(CrCl))