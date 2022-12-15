# Will be implementing some new way to create an excel for our project.
import random
import xlsxwriter
# https://github.com/gibz104/xlsb-converter
# https://pypi.org/project/aspose-cells/#description

from datetime import datetime

# datetime object containing current date and time
now = datetime.now()
 

dt_string = now.strftime("%m/%d/%Y %H:%M:%S")

# Time of Shift
# Whole Tomatoes
# Sliced Tomatoes
# Crushed Tomatoes
# Total Tomatoes


def main():
    
    workbook = xlsxwriter.Workbook("Tomatoes.xlsx")
    
    bold_format = workbook.add_format({'bold': True})
    
    cell_format = workbook.add_format()
    cell_format.set_text_wrap()
    cell_format.set_align('top')
    cell_format.set_align('left=')
    
    worksheet = workbook.add_worksheet('Tomatoes')
    
    
    worksheet.write('A1', 'Shifts', bold_format)
    worksheet.write('B1', 'Whole Tomatoes', bold_format)
    worksheet.write('C1', 'Total Tomatoes', bold_format)
    # worksheet.write('C1', 'Sliced Tomatoes', bold_format)
    # worksheet.write('D1', 'Crushed Tomatoes', bold_format)
    # worksheet.write('E1', 'Total Tomatoes', bold_format)
    
    rowIndex = 2
    
    for row in range(25):
        tomatoshift = dt_string
        wholeTomatoes = 20 + random.randint(50, 100)
        # slicedTomatoes = 20 + random.randint(50, 100)
        # crushedTomatoes = 20 + random.randint(50, 100)
        totalOfTomatoes = wholeTomatoes #+ slicedTomatoes + crushedTomatoes
        #tomatoProfit = random.random() * 500
        
        worksheet.write('A' + str(rowIndex), tomatoshift, cell_format)
        worksheet.write('B' + str(rowIndex), wholeTomatoes, cell_format)
        worksheet.write('C' + str(rowIndex), totalOfTomatoes, cell_format)
        # worksheet.write('C' + str(rowIndex), slicedTomatoes, cell_format)
        # worksheet.write('D' + str(rowIndex), crushedTomatoes, cell_format)
        # worksheet.write('E' + str(rowIndex), totalOfTomatoes, cell_format)
        
        rowIndex += 1

    workbook.close()

    
if __name__ == "__main__":
    main()