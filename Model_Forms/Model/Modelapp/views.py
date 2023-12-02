from django.shortcuts import render
from Modelapp.models import User
from Modelapp.forms import NewUserForm
# Create your views here.

def index(request):
    return render(request,'Modelapp/index.html')


def users(request):
    '''
    user_list = User.objects.order_by('first_name')
    user_dict={'users': user_list}
    return render(request,'Modelapp/users.html',context=user_dict)
    '''
    
    form=NewUserForm()
    
    if request.method == "POST":
        form=NewUserForm(request.POST)
            
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        
        else:
            print('Error form is invalid')
            
    return render(request,'Modelapp/users.html',{'form':form})