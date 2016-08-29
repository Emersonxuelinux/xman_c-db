from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect 
from portal.models import Host
from portal.models import Idc
from portal.models import Maintance
from django.http import JsonResponse

# Create your views here.
def login(request):
	return render(request,'portal/login.html')
def check_login(request):
	username = request.GET.get('username')
	#username = request.GET.get('u')
	passwd = request.GET.get('password')
	#passwd = request.GET.get('p')
	if username == "zetao2016@6rooms.com" and passwd == "123.com":
		return HttpResponseRedirect('/')
		#return render(request,'portal/index.html')
	else:
		#return HttpResponse('用户名或密码错误')
		#return HttpResponse('<p style="color:red;">用户名或密码错误</p>')
		return render(request,'portal/login.html')
def addHost(request):
	return render(request,'portal/addHost.html')
def addIdc(request):
	return render(request,'portal/addIdc.html')
def addMaintance(request):
	return render(request,'portal/addMaintance.html')
def saltCMD(request):
	return render(request,'portal/saltCMD.html')
def get_hosts(request):
	#id=request.GET['id']
	hosts=Host.objects.all()[:10]	
	return render(request,'portal/hosts.html',{'hosts':hosts})
def idc_lists(request):
	return HttpResponse('<p style="color:red;">测试IDC机房列表</p>')
	#return render(request,'portal/idcs.html')
#首页
def index(request):
	response = ""
	hosts_list=Host.objects.all()[:10]
	idcs_list=Idc.objects.all()[:10]
	maintances_list=Maintance.objects.all()[:10]
	unhosts_list=Host.objects.filter(status='0')[:10]
	return render(request,'index.html',{'hosts':hosts_list,'idcs':idcs_list,'maintances':maintances_list,'unhosts_list':unhosts_list})
#获取IP地址
def ip_address(request):
	return {'ip_address': request.META['REMOTE_ADDR']}
#搜索框搜索
def search(request):
	host = request.GET.get('host')
	idc = request.GET.get('idc')
	hosts_array=Host.objects.filter(name__icontains='%s' % host)[:10]
	idcs_array=Host.objects.filter(name__icontains='%s' % idc)[:10]
	hosts_info=""
	for i in hosts_array:
		hosts_info += "<tr><td>"+str(i.id)+"</td><td>"+i.name+"</td><td>"+i.ip+"</td><td>"+str(i.role)+"</td><td>"+str(i.rack)+"</td><td></td></tr>"
	return HttpResponse("<tr>"+hosts_info+"</tr>")
#检查提交是否正确,包括设备机房维护等所有的
def check_add(request):
	if request.method == 'GET':
		return HttpResponse(status=403)
	idc=request.POST["idc-name"].encode('utf8')
	isp=request.POST["isp-name"].encode('utf8')
	return HttpResponse('<p style="color:red;">提交成功</p>')
