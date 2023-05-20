from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.conf import settings
from . import models
import time

curl=settings.CURRENT_URL
media_url=settings.MEDIA_URL

def home(request):
	query="select * from addcat"
	models.cursor.execute(query)
	clist=models.cursor.fetchall()
	return render(request,'home.html',{'curl':curl,'clist':clist,'media_url':media_url})
	
def viewsubcat(request):	
	query1="select * from addcat"
	models.cursor.execute(query1)
	clist=models.cursor.fetchall()
	
	cnm=request.GET.get("cnm")
	query="select * from addsubcat where catnm='%s' " %(cnm)
	models.cursor.execute(query)
	sclist=models.cursor.fetchall()
	return render(request,'viewsubcat.html',{'curl':curl,'sclist':sclist,'clist':clist,'cnm':cnm,'media_url':media_url})
	
def viewproducts(request):
	query1="select * from addcat"
	models.cursor.execute(query1)
	clist=models.cursor.fetchall()
	
	scnm=request.GET.get('scnm')	
	query="select * from product where cnm='%s' and bstatus=0" %(scnm)
	models.cursor.execute(query)
	plist=models.cursor.fetchall()
	
	return render(request,'viewproducts.html',{'curl':curl,'plist':plist,'scnm':scnm,'total':len(plist),'media_url':media_url,'clist':clist})	


def buylogin(request):
	if request.method=="GET":
		pid=request.GET.get('pid')
		price=request.GET.get('price')
		return render(request,'buylogin.html',{'curl':curl,'output':'','pid':pid,'price':price})
	else:
		email=request.POST.get('email')
		password=request.POST.get('password')
		pid=request.POST.get('pid')
		price=request.POST.get('price')
		
		query="select * from register where email='%s' and password='%s' and status=1 " %(email,password)
		models.cursor.execute(query)
		userDetails=models.cursor.fetchall()
		
		if len(userDetails)>0:
			if userDetails[0][8]=="user":
				response=redirect(curl+'user/userbuy/')
		
			response.set_cookie('cunm',email)
			response.set_cookie('pid',pid)
			response.set_cookie('price',price)
			return response	
		else:
			return render(request,'login.html',{'curl':curl,'output':'Login failed invalid user or verify your account....'})

	
def payment(request):
	uid=request.GET.get('uid')
	pid=request.GET.get('pid')	
	price=request.GET.get('price')
	ptime=time.strftime("%d/%m/%Y,%H:%M:%S,%A")
	query="insert into payment values(NULL,'%s',%s,%s,'%s')" %(uid,pid,price,ptime)
	models.cursor.execute(query)
	models.db.commit()
	return redirect(curl+'success/')

def cancel(request):
	return render(request,'cancel.html',{'curl':curl})
	
def success(request):
	return render(request,'success.html',{'curl':curl})		
	
def about(request):
	return render(request,'about.html',{'curl':curl})
	
def contact(request):
	return render(request,'contact.html',{'curl':curl})
	
def service(request):
	return render(request,'service.html',{'curl':curl})
	
def register(request):
	if request.method=="GET":
		return render(request,'register.html',{'curl':curl,'output':''})
	else:
		name=request.POST.get('name')
		email=request.POST.get('email')
		password=request.POST.get('password')
		address=request.POST.get('address')
		mobile=request.POST.get('mobile')
		city=request.POST.get('city')
		gender=request.POST.get('gender')
		
		query="insert into register values(NULL,'%s','%s','%s','%s','%s','%s','%s','user',0,'%s')" %(name,email,password,address,mobile,city,gender,time.asctime(time.localtime(time.time())))
		models.cursor.execute(query)
		models.db.commit()
		
		import smtplib 
		from email.mime.multipart import MIMEMultipart
		from email.mime.text import MIMEText
	
		me = "phpbatch34@gmail.com"
		you = email

		msg = MIMEMultipart('alternative')
		msg['Subject'] = "Verification Mail Bidding Web Solution"
		msg['From'] = me
		msg['To'] = you

		html = """<html>
  					<head></head>
  					<body>
    					<h1>Welcome to Bidding Web Solution</h1>
    					<p>You have successfully registered , please click on the link below to verify your account</p>
    					<h2>Username : """+email+"""</h2>
    					<h2>Password : """+str(password)+"""</h2>
    					<br>
    					<a href='http://localhost:8000/verify?vemail="""+email+"""' >Click here to verify account</a>		
  					</body>
				</html>
				"""
	
		s = smtplib.SMTP('smtp.gmail.com', 587) 
		s.starttls() 
		s.login("phpbatch34@gmail.com", "123@@123") 
	
		part2 = MIMEText(html, 'html')

		msg.attach(part2)
	
		s.sendmail(me,you, str(msg)) 
		s.quit() 
		print("mail send successfully....")
		
		
		return render(request,'register.html',{'curl':curl,'output':'Register successfully'})
	

def verify(request):
	vemail=request.GET.get('vemail')
	query="update register set status=1 where email='%s' " %(vemail)
	models.cursor.execute(query)
	models.db.commit()
	return redirect(curl+'login/')

	
def login(request):
	if request.method=="GET":
		return render(request,'login.html',{'curl':curl,'output':''})
	else:
		email=request.POST.get('email')
		password=request.POST.get('password')
		
		query="select * from register where email='%s' and password='%s' and status=1 " %(email,password)
		models.cursor.execute(query)
		userDetails=models.cursor.fetchall()
		
		print(userDetails)
		if len(userDetails)>0:
			if userDetails[0][8]=="user":
				response=redirect(curl+'user/')
			else:
				response=redirect(curl+'myadmin/')	
			response.set_cookie('cunm',email)
			return response	
		else:
			return render(request,'login.html',{'curl':curl,'output':'Login failed invalid user or verify your account....'})	
							














