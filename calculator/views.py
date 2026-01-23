from django.shortcuts import render

# Create your views here.
def index(request):
    result=None
    if request.method=='POST':
        try:
            num1=float(request.POST.get('num1'))
            num2=float(request.POST.get('num2'))
            op=request.POST.get('op')

            if op=='+':
                  result=num1 + num2
            elif op=='-' :
                 result= num1 - num2
            elif op=='*':
                 result= num1 * num2
            elif op=='/':
                 if num2 !=0:
                    result=num1/num2
                 else: result="error try again not try 0"   
            
        except (ValueError,TypeError):
               result="please enter integer number"
    return render(request,'calculator/index.html',{'result':result})