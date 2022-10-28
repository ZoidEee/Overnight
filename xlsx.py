import xlsxwriter


def xlsxWriter(date,time,amount,apy, filename):
    workbook = xlsxwriter.Workbook(f'/home/nvll/Desktop/{filename}.xlsx')
    worksheet = workbook.add_worksheet()

    colTitle = ['Date', 'Time', 'Amount', 'APY']
    row = 0
    col = 0

    alignCenter = workbook.add_format()
    alignCenter.set_align('center')
    alignCenter.set_align('vcenter')

    worksheet.set_column(first_col=0, last_col=4, width=10)


    for title in colTitle:
        worksheet.write(row, col, title,alignCenter)
        col += 1

    row = 1
    col = 0

    for d in date:
        worksheet.write(row, col, d, alignCenter)
        row += 1
    row = 1
    col = 1
    for t in time:
        worksheet.write(row, col, t, alignCenter)
        row += 1
    row = 1
    col = 2
    for a in amount:
        worksheet.write(row, col, a, alignCenter)
        row += 1
    row = 1
    col = 3
    for p in apy:
        worksheet.write(row, col, p, alignCenter)
        row += 1

    workbook.close()



