log_data = "SCORE:Player_1:2500"
parsed_data = log_data.split(":")

print(parsed_data)
print(f"Name: {parsed_data[1]} | {parsed_data[0]}: {parsed_data[2]}")



