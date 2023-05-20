from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from . import models

curl=settings.CURRENT_URL


# Create your views here.

def myadminhome(request):
	return render(request,"adminhome.html",{'curl':curl})
		
def manageusers(request):
	query="select * from register where role!='admin' "
	models.cursor.execute(query)
	userDetails=models.cursor.fetchall()
	return render(request,"manageusers.html",{'curl':curl,'userDetails':userDetails})		
	

def manageusersstatus(request):
	s=request.GET.get('s')
	rid=request.GET.get('rid')
	if s=="block":
		query="update register set status=0 where regid=%s" %(rid)
	elif s=="unblock":	
		query="update register set status=1 where regid=%s" %(rid)
	else:
		query="delete from register where regid=%s" %(rid)	
	models.cursor.execute(query)
	models.db.commit()	
	return redirect(curl+'myadmin/manageusers/')	
	
def addcat(request):
	if request.method=="GET":
		return render(request,"addcat.html",{'curl':curl,'output':''})
	else:
		catnm=request.POST.get('catnm')
		caticon=request.FILES['caticon']
		fs = FileSystemStorage()
		filename = fs.save(caticon.name,caticon)
		query="insert into addcat values(NULL,'%s','%s')" %(catnm,filename)
		models.cursor.execute(query)
		models.db.commit()
		return render(request,"addcat.html",{'curl':curl,'output':'Category added successfully'})
		

def addsubcat(request):
	query="select * from addcat"
	models.cursor.execute(query)
	clist=models.cursor.fetchall()
	if request.method=="GET":
		return render(request,"addsubcat.html",{'curl':curl,'clist':clist,'output':''})
	else:
		catnm=request.POST.get('catnm')
		subcatnm=request.POST.get('subcatnm')
		caticon=request.FILES['caticon']
		fs = FileSystemStorage()
		filename = fs.save(caticon.name,caticon)
		query="insert into addsubcat values(NULL,'%s','%s','%s')" %(catnm,subcatnm,filename)
		models.cursor.execute(query)
		models.db.commit()
		return render(request,"addsubcat.html",{'curl':curl,'clist':clist,'output':'Sub Category added successfully'})		
					
	
	
	
	
	
	
	
	
	
	
	
	
