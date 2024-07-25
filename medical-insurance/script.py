def calculate_insurance_cost(age, sex, bmi, num_of_children, smoker):
    estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
    print("The estimated insurance cost for this person is " + str(estimated_cost) + " dollars.")
    return estimated_cost


# Estimate Maria's insurance cost
maria_insurance_cost = calculate_insurance_cost(28, 0, 26.2, 3, 0)

print("The estimated insurance cost for Maria is " + str(calculate_insurance_cost) + " dollars.")


# Estimate Omar's insurance cost
omar_insurance_cost = calculate_insurance_cost(35, 1, 22.2, 0, 1)

print("The estimated insurance cost for Omar is " + str(calculate_insurance_cost) + " dollars.")
