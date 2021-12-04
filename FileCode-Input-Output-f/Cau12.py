SoTuNhien = ['không', 'một', 'hai', 'ba', 'bốn', 'năm', 'sáu', 'bảy', 'tám', 'chín']
DonVi = ['mươi', 'mốt','hai', 'ba', 'bốn', 'lăm', 'sáu', 'bảy', 'tám', 'chín']
Chuc = ['linh', 'mười','hai', 'ba', 'bốn', 'lăm', 'sáu', 'bảy', 'tám', 'chín']
Lop = ['tỷ', 'triệu', 'nghìn']
Cum = ['trăm', 'chục', 'đơn vị']

def nhomCum3So(so):
    chieudai_so = len(so)
    sodu, songuyen = chieudai_so % len(Cum), chieudai_so//len(Cum)
    list_CumLe = so[:sodu]
    list_CumChan = so[sodu:]
    
    list_Cum3So = []
    if list_CumLe != "":
        list_Cum3So = [list_CumLe]
    begin = 0
    end = begin +3
    for _ in range(songuyen):                          
        list_Cum3So.append(list_CumChan[begin:end])
        begin = end 
        end = begin +3
    return list_Cum3So

def themTienTo_Lop(list_Cum3So):   
    so_label = len(list_Cum3So)
    soLop = len(Lop)
    list_TienTo = []
    if so_label==1: 
        return list_TienTo, list_Cum3So
    elif so_label>1 and so_label <= soLop:
        list_TienTo = [*Lop[-so_label+1:]]
    else: 
        sochu_ty = 0
        for i_label in range(so_label):
            if id_Lop < (-soLop): 
                id_Lop =-1
                list_TienTo.insert(0, Lop[id_Lop])
                id_Lop -= 1

            elif i_label !=0:
                list_TienTo.insert(0, Lop[id_Lop])
                id_Lop -= 1
                if list_TienTo[0] == Lop[0]:
                    list_TienTo[0] += (" "+Lop[0])*sochu_ty                     
                    sochu_ty += 1 
    return list_TienTo, list_Cum3So

def phanCum_themTienTo (so):
    list_Cum3So = nhomCum3So(so)
    list_TienTo, list_Cum3So = themTienTo_Lop(list_Cum3So)
    return list_TienTo, list_Cum3So
    
# Đọc số có 2 chữ số
def docSoChuc(so2ChuSo):
    
    if so2ChuSo[0] == "0":
        return "linh" +" "+ SoTuNhien[int(so2ChuSo[1])]    
        # Xét các số hàng đơn vị
        if so2ChuSo[1] == "0":
            return Chuc[1] # Số 10
        elif so2ChuSo[1] == "1":
            return Chuc[1] + " "+ SoTuNhien[1]
        else:
            return Chuc[1] + " " +DonVi[int(so2ChuSo[1])]   

    else:
        if DonVi[0] == DonVi[int(so2ChuSo[1])]:
            return SoTuNhien[int(so2ChuSo[0])] +" " + DonVi[int(so2ChuSo[1])]                 
        else:
            return SoTuNhien[int(so2ChuSo[0])] +" " + DonVi[0] +" "+ DonVi[int(so2ChuSo[1])]

def docSoTram(so):
    
    if so[1:] == "00":
        return SoTuNhien[int(so[0])]+" " +Cum[0]
    else:
        return SoTuNhien[int(so[0])]+" " +Cum[0]+" "+docSoChuc(so[1:])

def docso_TungCum(so):
    chieudai_so = len(so)
    if chieudai_so == 1:
        return SoTuNhien[int(so)]
    elif chieudai_so == 2:
        return docSoChuc(so)
    else:        
        return docSoTram(so)

def doc_Cum3so(list_cum3So):
    kq_DocSo =[]
    # Đọc các số theo từng lớp
    for lop in list_cum3So:
        if lop != "":
            kq_DocSo.append(docso_TungCum(lop))
    return kq_DocSo        

def ghepCacLop(list_TienTo, ketqua_DocCum):
    ketQuaDocSo = ''  
    if list_TienTo == []:
        ketQuaDocSo = ketqua_DocCum[0]
    elif list_TienTo != []:
        for i_cum in range(len(ketqua_DocCum)):
            if i_cum < len(list_TienTo):
                ketQuaDocSo += (ketqua_DocCum[i_cum] + " " +list_TienTo[i_cum] + " ")                
            else: ketQuaDocSo +=  ketqua_DocCum[i_cum]
    else:
        ketQuaDocSo += ketqua_DocCum[0]
       
    ketQuaDocSo = ketQuaDocSo.capitalize()
    return ketQuaDocSo

# Đọc số
def docso(so):    
    list_TienTo, list_Cum3So = phanCum_themTienTo(so)
    ketqua_DocCum = doc_Cum3so(list_Cum3So)
    ketQuaDocSo = ghepCacLop(list_TienTo, ketqua_DocCum)   
    return ketQuaDocSo
    

path_w = 'output.txt'
s = ''




mylist = []

f = open('input.txt', 'r', encoding='UTF-8')
data = f.read()
mylist = data.split("\n")
for i in mylist:
    print(docso(i))
    s += docso(i) + '\n'

with open(path_w, mode='w') as f:
    f.write(s)