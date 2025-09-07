import os
from docxtpl import DocxTemplate
from docx2pdf import convert
import pandas as pd

ans = pd.read_csv("data.csv")
n = len(ans)

output_folder = "output"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)


def generate_certificate(index, total_rows):
    tpl = DocxTemplate("Certificate_Template.docx")

    # Extracting relevant information for the current row
    # fName = ans["FName"][index - 1]
    # lName = ans["LName"][index - 1]
    certificate_name = ans["certificate_name"][index - 1]
    # registration_email = ans["registration_email"][index - 1]
    # user_id = ans["ID"][index - 1]
    # get user_id as the index
    user_id = index

    # Creating the context dictionary
    context = {
        j + 1: {
            # "FName": fName,
            # "LName": lName,
            "certificate_name": certificate_name,
            # "ID": user_id,
        }
        for j in range(index)
    }

    tpl.render(context[index])

    output_path_docx = os.path.join(
        output_folder,
        # Below are extras
        # f"{fName}{lName}.docx",
        # f"{certificate_name}.docx",
        f"{index} - {certificate_name}.docx",
    )
    tpl.save(output_path_docx)

    print(
        f"Processing file: {index}/{total_rows} | {user_id} - {certificate_name}")
    convert(output_path_docx)


# Loop through all records and generate certificates
for i in range(1, n + 1):
    generate_certificate(i, n)

print("All done!")
