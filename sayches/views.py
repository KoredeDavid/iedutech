from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from sayches.forms import PopForm

# Create your views here.


@login_required
def pop(request):
    if request.method == 'POST':
        form = PopForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            form_obj = form.save(commit=False)
            form_obj.user = request.user
            form_obj.save()
            messages.success(request, 'Pop saved', )
            return redirect('pop')
    else:
        form = PopForm()
    return render(request, 'sayches.html', {'form':form})


