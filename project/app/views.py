from django.shortcuts import render
from re import findall 
import smtplib,ssl,os
from re import findall
from email.message import EmailMessage

def index(request):
    return render(request,'index.html')

def conferm(request):
    EID=request.POST['EID']
    Name=request.POST['NAME']
    Order=request.POST['ORDER']
    with open('OrdersList.txt','a') as file :
        file.write(f"{EID},{Name},{Order}\n")
    return render(request, 'conferm.html')

def orderlist(request):
    orders={
      "order":[]
    }
    if 'done' in request.POST:

        email=(request.POST)['done']

        From='sachin.hs@sigmoidanalytics.com'
        To=email
        password='vdxplxkzugyaktak'
        #

        em=EmailMessage()
        em['From']='sachin.hs@sigmoidanalytics.com'
        em['To']=email
        em['Subject']="Order Status"
        em.set_content('your order has been done \n Please collect it from the counter \n')
         
        context=ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
           smtp.login(From,password)
           smtp.sendmail(From,To,em.as_string())


        with open('OrdersList.txt','r') as file :
                data = file.read().splitlines(True)
        with open('OrdersList.txt', 'w') as fout:
                fout.writelines(data[1:])
        
    with open('OrdersList.txt','r') as file:
        for line in file:
            data=findall(r"[^,]+",line)
            orders['order'].append({"eid":data[0],"name":data[1],"order":data[2]})
    
    return render(request, 'orderlist.html', {"result":orders})



