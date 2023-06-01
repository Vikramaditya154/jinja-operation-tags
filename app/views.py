from django.shortcuts import render

# Create your views here.
def condition(request):
    d={'a':20,'b':80,'c':100}
    return render(request,'if-condition.html',context=d)