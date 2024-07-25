def calculate_insurance_cost():
    print("The estimated insurance cost for this person is " + str(estimated_cost) + " dollars.")
    return estimated_cost

# Initial variables for Maria
age = 28
sex = 0
bmi = 26.2
num_of_children = 3
smoker = 0

# Estimate Maria's insurance cost
insurance_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500

print("The estimated insurance cost for Maria is " + str(insurance_cost) + " dollars.")
