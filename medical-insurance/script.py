def analyze_smoker(smoker_status):
    if smoker_status == 1:
        print("To lower your cost, you should consider quitting smoking.")
    else:
        print("Smoking is not an issue for you.")


def calculate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
    estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
    print("The estimated insurance cost for " + name + " is " + str(estimated_cost) + " dollars.")
    return estimated_cost
    analyze_smoker(smoker)


# Estimate Maria's insurance cost
keanu_insurance_cost = calculate_insurance_cost(name = 'Keanu', age = 29, sex = 1, bmi=26.2, num_of_children = 3, smoker = 1)
