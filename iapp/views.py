from django.shortcuts import render,redirect
from .models import UploadImage
from .forms import UserImage
def index(request):
    if request.method=='post':
        fm=UserImage(request.POST,request.FILES)
        if fm.is_valid():
            images=fm.cleaned_data['images']
            reg=UploadImage(images=images)
            reg.save()
            return redirect('index')
    else:
        fm=UserImage()
    im = UploadImage.objects.all()
    return render(request,'upload.html',{'forms':fm,'download':im})










