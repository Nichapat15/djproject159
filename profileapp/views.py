from django.shortcuts import render

def home(request):
    return render(request,'home.html')
def personal(request):
    return render(request,'personal.html')
def sale(request):
    return render(request,'sale.html')
def interests(request):
    return render(request,'interests.html')
def educational(request):
    return render(request,'educational.html')

def rolemodel(request):
    return render(request,'rolemodel.html')

def showMyData(request):
    showID = '65342310159-1'
    showName = "ณิชาภัทร ไชยธงรัตน์"
    showAddress = "85 หมู่ 1 ต.ค้อเหนือ อ.เมือง จ.ยโสธร"
    showtel = "0940731977"
    showgender = "หญิง"
    showBirthday = "15 กุมภาพันธ์ 2545"
    showWeight = 79
    showHeight = 169
    showstatus = "นักศึกษา"
    showSchool = "มหาวิทยาลัยเทคโนโลยีราชมงคลอีสาน วิทยาเขตขอนแก่น"

    products = []

    product =['เลย์',20.00,'../../static/images/lays.png']
    products.append(product)
    product =['เบนโตะ', 20.00,'../../static/images/bento.png']
    products.append(product)
    product =['คอนเน่',20.00,'../../static/images/conne.png']
    products.append(product)
    product =['ทาโร่',20.00,'../../static/images/taro.png']
    products.append(product)
    product =['โปเต้',20.00,'../../static/images/pote.png']
    products.append(product)
    product = [ 'ตะวัน', 20.00,'../../static/images/tawan.png']
    products.append(product)
    product = ['ไดโนเสาร์',20.00,'../../static/images/daino.png']
    products.append(product)
    product = [ 'มาชิตะ',20.00,'../../static/images/mashi.png']
    products.append(product)
    product = [ 'ปาร์ตี้', 20.00,'../../static/images/party.png']
    products.append(product)
    product = [ 'สแน็คแจ็ค', 20.00,'../../static/images/sanak.png']
    products.append(product)

    context = {'showID':showID,'showName':showName,'showAddress':showAddress,'showtel':showtel,
               'showgender':showgender,'showBirthday':showBirthday,'showWeight':showWeight,'showHeight':showHeight,
               'showstatus':showstatus,'showSchool':showSchool, 'products':products}
    return render(request, 'showMyData.html', context)

