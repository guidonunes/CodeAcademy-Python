names = ["Mohamed", "Sara", "Xia", "Paul", "Valentina", "Jide", "Aaron", "Emily", "Nikita", "Paul"]
insurance_costs = [13262.0, 4816.0, 6839.0, 5054.0, 14724.0, 5360.0, 7640.0, 6072.0, 2750.0, 12064.0]


names.append("Priscilla")
print(names)
insurance_costs.append(8320.0)
print(insurance_costs)


medical_records = list(zip(insurance_costs, names))
