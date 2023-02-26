from django.shortcuts import render
from testapp.models import Employee
from django.db.models import Q
from django.db.models.functions import Lower

# Create your views here.

def Employee_View(request):
    # emp_list = Employee.objects.all()
    # emp_list = Employee.objects.filter(esal__gt='12121')
    # emp_list = Employee.objects.filter(ename__icontains='sunny')
    # emp_list = Employee.objects.filter(id__in=[1,3,5])
    # emp_list = Employee.objects.filter(ename__startswith='D')
    # emp_list = Employee.objects.filter(ename__endswith='d')
    # emp_list = Employee.objects.filter(esal__range=[12000,15000])
    # emp_list = Employee.objects.filter(ename__startswith='D') | Employee.objects.filter(esal__lt=15000)
    # emp_list = Employee.objects.filter(Q(ename__startswith='D') | Q(esal__lt=15000))
    # emp_list = Employee.objects.filter(ename__startswith='D') & Employee.objects.filter(esal__lt=15000)
    # emp_list = Employee.objects.filter(Q(ename__startswith='D') & Q(esal__lt=15000))
    # emp_list = Employee.objects.filter(ename__startswith='D',esal__lt=15000)
    # emp_list = Employee.objects.exclude(ename__startswith='J')
    # emp_list = Employee.objects.filter(~Q(ename__startswith='J'))
    # emp_list = Employee.objects.all().values_list('ename','esal','eaddr')
    # emp_list = Employee.objects.all().values('ename','esal')
    # emp_list = Employee.objects.all().only('ename','esal','eaddr')
    # emp_list = Employee.objects.all().only('ename','esal','eaddr')
    # emp_list = Employee.objects.all().order_by('-esal')
    # emp_list = Employee.objects.all().order_by(Lower('ename'))


    q1 = Employee.objects.filter(esal__lt=15000)
    q2 = Employee.objects.filter(ename__startswith='J')
    q3 = q1.union(q2)
    emp_list = q3

    return render(request,'testapp/emp.html',{'emp_list':emp_list})


from django.db.models import Avg,Sum,Min,Max,Count

def aggregate_view(request):
    avg = Employee.objects.all().aggregate(Avg('esal'))
    max = Employee.objects.all().aggregate(Max('esal'))
    min = Employee.objects.all().aggregate(Min('esal'))
    avg = Employee.objects.all().aggregate(Avg('esal'))
    sum = Employee.objects.all().aggregate(Sum('esal'))
    count = Employee.objects.all().aggregate(Count('esal'))
    my_dict = {'avg':avg['esal__avg'],'max':max['esal__max'],'min':min['esal__min'],'sum':sum['esal__sum'],'count':count['esal__count']}
    return render(request,'testapp/aggregate.html',my_dict)
