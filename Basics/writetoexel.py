"""
    :summary This is python 3.7 supported selenium 3.141.0

    :since January 2020

    :author Sathya Sai M

    :keyword Python, selenium to write to EXEL file
"""
import openpyxl


class Exel:
    def exel(self):
        path = "/home/admin1/Downloads/Untitled 1.xlsx"

        workbook = openpyxl.load_workbook(path)
        sheet = workbook.active

        for r in range(1, 6):
            for c in range(1, 6):
                sheet.cell(row=r, column=c).value = "welcome"
        workbook.save(path)


if __name__ == '__main__':
    e = Exel()
    e.exel()
