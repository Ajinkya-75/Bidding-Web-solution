from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import time
from . import models

curl=settings.CURRENT_URL
media_url=settings.MEDIA_URL

# Create your views here.

def userhome(request):
	return render(request,"userhome.html",{'curl':curl})
	
def addproduct(request):
	query1="select * from addsubcat"
	models.cursor.execute(query1)
	sclist=models.cursor.fetchall()
		
	if request.method=="GET":
		return render(request,"addproduct.html",{'curl':curl,'sclist':sclist,'cunm':request.COOKIES.get('cunm'),'output':''})
	else:
		title=request.POST.get('title')
		cnm=request.POST.get('cnm')
		price=request.POST.get('price')
		description=request.POST.get('description')
		mobile=request.POST.get('mobile')
		uid=request.POST.get('uid')
		bstatus=request.POST.get('bstatus')
		
		picon=request.FILES['picon']
		fs = FileSystemStorage()
		filename = fs.save(picon.name,picon)
		
		
		if bstatus!=None:
			bstatus=1
		else:
			bstatus=0	
		
		query="insert into product values(NULL,'%s','%s',%s,'%s','%s','%s','%s',%s,'%s')" %(title,cnm,price,description,mobile,filename,uid,bstatus,time.time())
		models.cursor.execute(query)
		models.db.commit()
		
		return render(request,"addproduct.html",{'curl':curl,'sclist':sclist,'cunm':request.COOKIES.get('cunm'),'output':'Product added successfully....'})
			
		
def userbuy(request):
	paypalURL = 'https://www.sandbox.paypal.com/cgi-bin/webscr'; 
	paypalID = 'jainishir-myseller@gmail.com';
	return render(request,"userbuy.html",{'paypalURL':paypalURL,'paypalID':paypalID,'curl':curl,'cunm':request.COOKIES.get('cunm'),'pid':request.COOKIES.get('pid'),'price':request.COOKIES.get('price')})		
		
	
def biddingproduct(request):
	uid=request.COOKIES.get('cunm')
	query="select * from product where bstatus=1 and uid!='%s' " %(uid)
	models.cursor.execute(query)
	plist=models.cursor.fetchall()
	dtime=172800
	ctime=time.time()
	
	for pdetails in plist:
		if ctime-float(pdetails[9])>dtime:
			query1="update product set status=1 where pid=%s" %(pdetails[0])
			models.cursor.execute(query1)
			models.db.commit()
	
	query2="select * from product where bstatus=1 and uid!='%s' and status=0" %(uid)
	models.cursor.execute(query2)
	new_plist=models.cursor.fetchall()
	
	
	return render(request,"biddingproduct.html",{'curl':curl,'plist':new_plist,'uid':uid,'media_url':media_url})	
	
def biddingoption(request):
	pid=request.GET.get('pid')
	query="select * from product where pid=%s " %(pid)
	models.cursor.execute(query)
	pdetails=models.cursor.fetchall()
	
	query1="select * from bidding where pid=%s " %(pid)
	models.cursor.execute(query1)
	bdetails=models.cursor.fetchall()
	
	if len(bdetails)>0:
		cprice=bdetails[0][3]
		for b in bdetails:
			if cprice<b[3]:
				cprice=b[3]
	else:
		cprice=pdetails[0][3]
	
	return render(request,'biddingoption.html',{'curl':curl,'media_url':media_url,'pdetails':pdetails[0],'cprice':cprice,'bid_uid':request.COOKIES.get('cunm')})	
	
	
def mybid(request):
	pid=request.POST.get('pid')
	bprice=request.POST.get('bprice')
	bid_uid=request.POST.get('bid_uid')
	
	query="insert into bidding values(NULL,%s,'%s',%s,'%s')" %(pid,bid_uid,bprice,time.asctime(time.localtime(time.time())))
	models.cursor.execute(query)
	models.db.commit()	
	pid=str(pid)
	return redirect(curl+'user/biddingoption/?pid='+pid)
	
def viewbiddingproduct(request):
	uid=request.COOKIES.get('cunm')
	query="select * from product where bstatus=1 and uid='%s' " %(uid)
	models.cursor.execute(query)
	plist=models.cursor.fetchall()
	return render(request,'viewbiddingproduct.html',{'curl':curl,'plist':plist,'media_url':media_url})	

def bidhistory(request):
	pid=request.GET.get('pid')
	query="select * from bidding where pid=%s order by bprice desc" %(pid)
	models.cursor.execute(query)
	blist=models.cursor.fetchall()
	return render(request,'bidhistory.html',{'curl':curl,'blist':blist,'media_url':media_url})		
	
	
	
	
	
	
	
	
	
	
		
		
		
		
				
	
