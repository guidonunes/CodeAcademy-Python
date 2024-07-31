names = ["Mohamed", "Sara", "Xia", "Paul", "Valentina", "Jide", "Aaron", "Emily", "Nikita", "Paul"]
insurance_costs = [13262.0, 4816.0, 6839.0, 5054.0, 14724.0, 5360.0, 7640.0, 6072.0, 2750.0, 12064.0]


names.append("Priscilla")
print(names)
insurance_costs.append(8320.0)
print(insurance_costs)
print("-" * 50)

medical_records = list(zip(insurance_costs, names))
print(medical_records)
print("-" * 50)

num_medical_records = len(medical_records)
print(f"There are {num_medical_records} medical records")
print("-" * 50)

first_medical_record = medical_records[0]
print(first_medical_record)
print("-" * 50)

medical_records.sort()
print("Here are the medical records sorted by insurance cost: " + str(medical_records))
