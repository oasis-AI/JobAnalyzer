



import pandas as pd

file_path = '/Users/shiyu/Downloads/kong.xlsx'

ef = pd.ExcelFile(file_path)

print(ef.sheet_names)

for sheet in ef.sheet_names:
    # df = ef.parse(sheet)
    # print(df.head())

    sheet_df = pd.read_excel(file_path, sheet_name=sheet)

    print(sheet_df.head())


