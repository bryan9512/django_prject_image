from django.shortcuts import render
from .forms import UploadedImageForm
from django.core.files.storage import FileSystemStorage

# Create your views here.


def first_view(request):
    return render(request,'django_eyeapp/first_view.html',{})

def uimage(request):
    if request.method == 'POST':
        form = UploadedImageForm(request.POST, request.FILES)
        if form.is_valid():
            myfile = request.FILES['image']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name,myfile)
            uploaded_file_url = fs.url(filename)
            return render(request,'django_eyeapp/uimage.html',{'form': form, 'uploaded_file_url': uploaded_file_url})
        #글을 쓸 때에는 여기로

    else:
        form = UploadedImageForm()
        return render(request,'django_eyeapp/uimage.html',{'form':form})
        # 글을 쓰지 않고 보여줄 때에는 여기로