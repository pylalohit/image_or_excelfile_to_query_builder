from django.shortcuts import render



def home(request):
    return render(request,"home.html")

def Create_Table(request):
    import xlrd
    if request.method == "POST" :
        file_obj = request.FILES['filename']
        #fs = FileSystemStorage()
        #fs.save(file_obj.name,file_obj)
        #loc = fs.path(file_obj.name)
        wb = xlrd.open_workbook(file_contents = file_obj.read())
        sheet = wb.sheet_by_index(0)
        tn = request.POST['tablename']
        nc = sheet.ncols
        nr = sheet.nrows
        ts = "CREATE TABLE" + " " + tn + " " + '('
        ins = "INSERT INTO "+ tn + " VALUES ( "
        intl = [] # list for integer index storage
        indl = [] # list for date index storage
        tr = sheet.row_values(nr-1)
        td = sheet.row_values(nr-1)
        Insert_Into_Table_list = []
        for i in range(nc):
            if i == nc-1:
                ts = ts + sheet.cell_value(0,i) + " " + sheet.cell_value(nr-1,i)+" "+");"
            else:
                ts = ts + sheet.cell_value(0,i) + " " + sheet.cell_value(nr-1,i)+" "+','+ " "
        ## find integer index start
        for i in tr :
            if i == "integer" or i == "INTEGER" or i == "Integer" or i == "int" or i == " INT" or i == "Int":
                ind = tr.index(i) # temp used for integer index storage
                intl.append(ind)
                tr[ind] = None
        ## find interger index end

        ## find date index start
        for i in td :
            if i == "date" or i == "DATE" or i == "Date":
                indt = td.index(i) # temp used for date index storage
                indl.append(indt)
                td[indt] = None
        
        ## find date index end
        for i in range(1,nr-1):
            temp = sheet.row_values(i)
            if len(intl) > 0:
                for i in intl:
                    temp[i] = int(temp[i])
            if len(indl) > 0:
                for i in indl:
                    temp[i] = xlrd.xldate.xldate_as_datetime(temp[i],wb.datemode) 
                    temp[i] = str(temp[i])
                    temp[i] = temp[i][:10]

            temp = str(temp)
            temp = temp.replace('[',"")
            temp = temp.replace(']',"")
            temp = ins + temp + ');'
            Insert_Into_Table_list.append(temp)

        return render(request,"result.html",{"result1":ts,"result2":Insert_Into_Table_list})









