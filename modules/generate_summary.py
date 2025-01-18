import xlsxwriter

def create_workbook():
    workbook = xlsxwriter.Workbook('output/FSOAR_PARSER.xlsx')
    worksheet = workbook.add_worksheet('Known Issues')

    cell_format = workbook.add_format({
        'font_size': 8,
        'bold': True,
        'color': 'blue',
        'align': 'center',
        'text_wrap': True
    })

    table_header_format  = workbook.add_format({
        'font_size': 12,
        'bold': True,
        'color': 'blue',
        'align': 'center'
    })

    worksheet.insert_image('A1', 'input/Fortinet-logo-rgb-black-red.png', {'x_scale': 0.5, 'y_scale': 0.5})
    worksheet.insert_image('E1', 'input/2025-01-17 18_06_19-FortiSOAR.png', {'x_scale': 0.7, 'y_scale': 0.7})

    row = 5
    worksheet.set_column('A:A', 5)
    worksheet.set_column('B:B', 20)
    worksheet.set_column('C:C', 50)
    worksheet.set_column('D:D', 130)
    worksheet.write("D1", "FortiSOAR Automated Troubleshooter", table_header_format)

    worksheet.write("A5", "S.No", table_header_format)
    worksheet.write("B5", "Log File Name", table_header_format)
    worksheet.write("C5", "Solution", table_header_format)
    worksheet.write("D5", "Log Line", table_header_format)


    with open('findings/output.txt', 'r') as findingsfh:
        for outline in findingsfh.readlines():
            outline = outline.strip().split('~')
            col = 0
            worksheet.write(row, col, row-4, cell_format)
            worksheet.write(row, col+1, outline[0], cell_format)
            worksheet.write(row, col+2, outline[2], cell_format)
            worksheet.write(row, col+3, outline[1], cell_format)
            row = row + 1

    unknown = workbook.add_worksheet('Unknown Issues')

    unknown.insert_image('A1', 'input/Fortinet-logo-rgb-black-red.png', {'x_scale': 0.5, 'y_scale': 0.5})
    unknown.insert_image('D1', 'input/2025-01-17 18_06_19-FortiSOAR.png', {'x_scale': 0.7, 'y_scale': 0.7})
    row = 5
    unknown.set_column('A:A', 5)
    unknown.set_column('B:B', 20)
    unknown.set_column('C:C', 180)
    unknown.write("C1", "FortiSOAR Automated Troubleshooter", table_header_format)

    unknown.write("A5", "S.No", table_header_format)
    unknown.write("B5", "Log File Name", table_header_format)
    unknown.write("C5", "Log Line", table_header_format)

    workbook.close()