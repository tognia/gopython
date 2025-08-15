import pandas as pd

data = [
    {"Name": "F Martin", "Amount": "1000 F"},
    {"Name": "F Henri", "Amount": "1000 F"},
    {"Name": "MAGLOIRE", "Amount": "1000 F"},
    {"Name": "Pa Leo", "Amount": "1000 F"},
    {"Name": "Ma Dora", "Amount": "1000 F"},
    {"Name": "Timothée", "Amount": "1000"},
    {"Name": "F Jean Marie", "Amount": "1000"},
    {"Name": "F SALOMON", "Amount": "1000"},
    {"Name": "Ruth", "Amount": "1000"},
    {"Name": "Wes", "Amount": "1000"},
    {"Name": "Magellan", "Amount": "1000"},
    {"Name": "MASSOCK", "Amount": "1000"},
    {"Name": "Ma Marie", "Amount": "1000"},
    {"Name": "Emmanuel Mbalanda", "Amount": "1000"},
    {"Name": "Justin", "Amount": "1000"},
    {"Name": "Suzanne", "Amount": "1000"},
    {"Name": "Bonheur", "Amount": "1000"},
    {"Name": "Onana", "Amount": "1000"},
    {"Name": "Unknown", "Amount": "1000 F"}, # Assuming "1000F" without a name means "Unknown"
    {"Name": "Unknown", "Amount": "1000 F"}, # Assuming "1000 F" without a name means "Unknown"
    {"Name": "Unknown", "Amount": "1000 F"}, # Assuming "1000 F" without a name means "Unknown"
    {"Name": "S Trésor", "Amount": "1000"},
    {"Name": "S Alice", "Amount": "1000"},
    {"Name": "S Madeleine", "Amount": "1000"},
    {"Name": "S Pauline de Timothée", "Amount": "1000"},
    {"Name": "S Aboya Rose", "Amount": "1000"},
    {"Name": "S Marina", "Amount": "1000"},
    {"Name": "F Josue", "Amount": "1000"}
]

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Save the DataFrame to an Excel file
excel_file_name = "names_and_amounts.xlsx"
df.to_excel(excel_file_name, index=False)

print(f"Excel file '{excel_file_name}' created successfully!")