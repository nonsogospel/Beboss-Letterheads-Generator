from django.shortcuts import render, redirect
from django.core.mail import send_mail
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors
from reportlab.lib.colors import HexColor
from reportlab.lib.units import inch
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Pagecontact, Uploaded_Images


# Create your views here.
def index(request):
    return render(request, 'index.html', {})


def contactpage(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        user = Pagecontact(username=username, email=email, subject=subject, message=message)
        user.save();

        messages.info(request, 'Form Submitted Successfully')
        return render(request, 'index.html')


# The letterhead section begins here
# Page to fill the form begins here
def generate_letterhead(request):
    return render(request, 'generate-letterhead-now.html')

def generate_letterhead_s1(request):
    return render(request, 'generate-letterhead-now-s1.html')

def generate_letterhead_s2(request):
    return render(request, 'generate-letterhead-now-s2.html')

def generate_letterhead_s3(request):
    return render(request, 'generate-letterhead-now-s3.html')

def generate_letterhead_s5(request):
    return render(request, 'generate-letterhead-now-s5.html')

def generate_letterhead_s6(request):
    return render(request, 'generate-letterhead-now-s6.html')

def generate_letterhead_s7(request):
    return render(request, 'generate-letterhead-now-s7.html')

def generate_letterhead_s8(request):
    return render(request, 'generate-letterhead-now-s8.html')

def generate_letterhead_s9(request):
    return render(request, 'generate-letterhead-now-s9.html')

def generate_letterhead_s10(request):
    return render(request, 'generate-letterhead-now-s10.html')

def generate_letterhead_s11(request):
    return render(request, 'generate-letterhead-now-s11.html')

def generate_letterhead_s12(request):
    return render(request, 'generate-letterhead-now-s12.html')

def generate_letterhead_s13(request):
    return render(request, 'generate-letterhead-now-s13.html')

def generate_letterhead_s14(request):
    return render(request, 'generate-letterhead-now-s14.html')

def generate_letterhead_s15(request):
    return render(request, 'generate-letterhead-now-s15.html')

def generate_letterhead_s16(request):
    return render(request, 'generate-letterhead-now-s16.html')

# page to fill the form ends here
    


def base(request):
    return render(request, 'base.html')

# I commented this section of my page
# because i removed it from the database, pushing it was giving me issues

# Individual controller of the page begins here

def letterhead_generator(request):
    if request.method == 'POST':
        Uploaded_Images.objects.all()
        business = request.POST['business']
        tagline = request.POST['tagline']
        message1 = request.POST['message1']
        email = request.POST['email']
        website = request.POST['website']
        location = request.POST['location']
        tel = request.POST['tel']
        image_upload = request.FILES.get('image_upload', False)
        data = [business, tagline, message1, email, website, location, tel]
        user = Uploaded_Images(image_upload=image_upload)
        user.save();
 
        return render(request, "samplific4lier.html", {'data': data})
        
        # return redirect('samples_generated.html')

    else:
        return render(request, "generate-letterhead-now.html")

# I will come back to this line of code later, i promise myself


def letterhead_generator_s1(request):
    if request.method == 'POST':
        Uploaded_Images.objects.all()
        business = request.POST['business']
        tagline = request.POST['tagline']
        message1 = request.POST['message1']
        email = request.POST['email']
        website = request.POST['website']
        location = request.POST['location']
        tel = request.POST['tel']
        image_upload = request.FILES.get('image_upload', False)
        data = [business, tagline, message1, email, website, location, tel]
        user = Uploaded_Images(image_upload=image_upload)
        user.save();
    
        return render(request, "samplific1lier.html", {'data': data})
        
        # return redirect('samples_generated.html')

    else:
        return render(request, "generate-letterhead-now-s1.html")


def letterhead_generator_s2(request):
    if request.method == 'POST':
        Uploaded_Images.objects.all().delete()
        Uploaded_Images.objects.all()
        business = request.POST['business']
        tagline = request.POST['tagline']
        message1 = request.POST['message1']
        email = request.POST['email']
        website = request.POST['website']
        location = request.POST['location']
        tel = request.POST['tel']
        image_upload = request.FILES.get('image_upload', False)
        data = [business, tagline, message1, email, website, location, tel, image_upload]
        user = Uploaded_Images(image_upload=image_upload)
        user.save();
    
        return render(request, "samplific2lier.html", {'data': data})
        
        # return redirect('samples_generated.html')

    else:
        return render(request, "generate-letterhead-now-s2.html")

def letterhead_generator_s3(request):
    if request.method == 'POST':
        Uploaded_Images.objects.all().delete()
        Uploaded_Images.objects.all()
        business = request.POST['business']
        tagline = request.POST['tagline']
        message1 = request.POST['message1']
        email = request.POST['email']
        website = request.POST['website']
        location = request.POST['location']
        tel = request.POST['tel']
        image_upload = request.FILES.get('image_upload', False)
        data = [business, tagline, message1, email, website, location, tel, image_upload]
        user = Uploaded_Images(image_upload=image_upload)
        user.save();
    
        return render(request, "samplific3lier.html", {'data': data})
        
        # return redirect('samples_generated.html')

    else:
        return render(request, "generate-letterhead-now-s3.html")


def letterhead_generator_s5(request):
    if request.method == 'POST':
        business = request.POST['business']
        tagline = request.POST['tagline']
        message1 = request.POST['message1']
        email = request.POST['email']
        website = request.POST['website']
        location = request.POST['location']
        tel = request.POST['tel']
        image_upload = request.FILES.get('image_upload', False)
        data = [business, tagline, message1, email, website, location, tel]
    
        return render(request, "samplific5lier.html", {'data': data})
        
        # return redirect('samples_generated.html')

    else:
        return render(request, "generate-letterhead-now-s5.html")


def letterhead_generator_s6(request):
    if request.method == 'POST':
        Uploaded_Images.objects.all().delete()
        Uploaded_Images.objects.all()
        business = request.POST['business']
        tagline = request.POST['tagline']
        message1 = request.POST['message1']
        email = request.POST['email']
        website = request.POST['website']
        location = request.POST['location']
        tel = request.POST['tel']
        image_upload = request.FILES.get('image_upload', False)
        data = [business, tagline, message1, email, website, location, tel, image_upload]
        user = Uploaded_Images(image_upload=image_upload)
        user.save();
    
        return render(request, "samplific6lier.html", {'data': data})
        
        # return redirect('samples_generated.html')

    else:
        return render(request, "generate-letterhead-now-s6.html")

def letterhead_generator_s7(request):
    if request.method == 'POST':
        Uploaded_Images.objects.all().delete()
        Uploaded_Images.objects.all()
        business = request.POST['business']
        tagline = request.POST['tagline']
        message1 = request.POST['message1']
        email = request.POST['email']
        website = request.POST['website']
        location = request.POST['location']
        tel = request.POST['tel']
        image_upload = request.FILES.get('image_upload', False)
        data = [business, tagline, message1, email, website, location, tel, image_upload]
        user = Uploaded_Images(image_upload=image_upload)
        user.save();
    
        return render(request, "samplific7lier.html", {'data': data})
        
        # return redirect('samples_generated.html')

    else:
        return render(request, "generate-letterhead-now-s7.html")

def letterhead_generator_s8(request):
    if request.method == 'POST':
        Uploaded_Images.objects.all().delete()
        Uploaded_Images.objects.all()
        business = request.POST['business']
        tagline = request.POST['tagline']
        message1 = request.POST['message1']
        email = request.POST['email']
        website = request.POST['website']
        location = request.POST['location']
        tel = request.POST['tel']
        image_upload = request.FILES.get('image_upload', False)
        data = [business, tagline, message1, email, website, location, tel, image_upload]
        user = Uploaded_Images(image_upload=image_upload)
        user.save();
    
        return render(request, "samplific8lier.html", {'data': data})
        
        # return redirect('samples_generated.html')

    else:
        return render(request, "generate-letterhead-now-s8.html")

def letterhead_generator_s9(request):
    if request.method == 'POST':
        Uploaded_Images.objects.all().delete()
        Uploaded_Images.objects.all()
        business = request.POST['business']
        tagline = request.POST['tagline']
        message1 = request.POST['message1']
        email = request.POST['email']
        website = request.POST['website']
        location = request.POST['location']
        tel = request.POST['tel']
        image_upload = request.FILES.get('image_upload', False)
        data = [business, tagline, message1, email, website, location, tel, image_upload]
        user = Uploaded_Images(image_upload=image_upload)
        user.save();
    
        return render(request, "samplific9lier.html", {'data': data})
        
        # return redirect('samples_generated.html')

    else:
        return render(request, "generate-letterhead-now-s9.html")

def letterhead_generator_s10(request):
    if request.method == 'POST':
        business = request.POST['business']
        tagline = request.POST['tagline']
        message1 = request.POST['message1']
        email = request.POST['email']
        website = request.POST['website']
        location = request.POST['location']
        tel = request.POST['tel']
        image_upload = request.FILES.get('image_upload', False)
        data = [business, tagline, message1, email, website, location, tel]
    
        return render(request, "samplific10lier.html", {'data': data})
        
        # return redirect('samples_generated.html')

    else:
        return render(request, "generate-letterhead-now-s10.html")


def letterhead_generator_s11(request):
    if request.method == 'POST':
        Uploaded_Images.objects.all().delete()
        Uploaded_Images.objects.all()
        business = request.POST['business']
        tagline = request.POST['tagline']
        message1 = request.POST['message1']
        email = request.POST['email']
        website = request.POST['website']
        location = request.POST['location']
        tel = request.POST['tel']
        image_upload = request.FILES.get('image_upload', False)
        data = [business, tagline, message1, email, website, location, tel, image_upload]
        user = Uploaded_Images(image_upload=image_upload)
        user.save();
    
        return render(request, "samplific11lier.html", {'data': data})
        
        # return redirect('samples_generated.html')

    else:
        return render(request, "generate-letterhead-now-s11.html")

def letterhead_generator_s12(request):
    if request.method == 'POST':
        Uploaded_Images.objects.all().delete()
        Uploaded_Images.objects.all()
        business = request.POST['business']
        tagline = request.POST['tagline']
        message1 = request.POST['message1']
        email = request.POST['email']
        website = request.POST['website']
        location = request.POST['location']
        tel = request.POST['tel']
        image_upload = request.FILES.get('image_upload', False)
        data = [business, tagline, message1, email, website, location, tel, image_upload]
        user = Uploaded_Images(image_upload=image_upload)
        user.save();
    
        return render(request, "samplific12lier.html", {'data': data})
        
        # return redirect('samples_generated.html')

    else:
        return render(request, "generate-letterhead-now-s12.html")

def letterhead_generator_s13(request):
    if request.method == 'POST':
        Uploaded_Images.objects.all().delete()
        Uploaded_Images.objects.all()
        business = request.POST['business']
        tagline = request.POST['tagline']
        message1 = request.POST['message1']
        email = request.POST['email']
        website = request.POST['website']
        location = request.POST['location']
        tel = request.POST['tel']
        image_upload = request.FILES.get('image_upload', False)
        data = [business, tagline, message1, email, website, location, tel, image_upload]
        user = Uploaded_Images(image_upload=image_upload)
        user.save();
    
        return render(request, "samplific13lier.html", {'data': data})
        
        # return redirect('samples_generated.html')

    else:
        return render(request, "generate-letterhead-now-s13.html")


def letterhead_generator_s14(request):
    if request.method == 'POST':
        business = request.POST['business']
        tagline = request.POST['tagline']
        message1 = request.POST['message1']
        email = request.POST['email']
        website = request.POST['website']
        location = request.POST['location']
        tel = request.POST['tel']
        image_upload = request.FILES.get('image_upload', False)
        data = [business, tagline, message1, email, website, location, tel]
    
        return render(request, "samplific14lier.html", {'data': data})
        
        # return redirect('samples_generated.html')

    else:
        return render(request, "generate-letterhead-now-s14.html")

def letterhead_generator_s15(request):
    if request.method == 'POST':
        business = request.POST['business']
        tagline = request.POST['tagline']
        message1 = request.POST['message1']
        email = request.POST['email']
        website = request.POST['website']
        location = request.POST['location']
        tel = request.POST['tel']
        image_upload = request.FILES.get('image_upload', False)
        data = [business, tagline, message1, email, website, location, tel]
    
        return render(request, "samplific15lier.html", {'data': data})
        
        # return redirect('samples_generated.html')

    else:
        return render(request, "generate-letterhead-now-s15.html")


def letterhead_generator_s16(request):
    if request.method == 'POST':
        Uploaded_Images.objects.all().delete()
        Uploaded_Images.objects.all()
        business = request.POST['business']
        tagline = request.POST['tagline']
        message1 = request.POST['message1']
        email = request.POST['email']
        website = request.POST['website']
        location = request.POST['location']
        tel = request.POST['tel']
        image_upload = request.FILES.get('image_upload', False)
        data = [business, tagline, message1, email, website, location, tel, image_upload]
        user = Uploaded_Images(image_upload=image_upload)
        user.save();
  
        return render(request, "samplific16lier.html", {'data': data})
        
        # return redirect('samples_generated.html')

    else:
        return render(request, "generate-letterhead-now-s16.html")


def samples_generated(request):
    return render(request, "samples_generated.html")


def attach_send(request):
    return render(request, "send-downloaded-letterhead.html")

# Page that houses the pdf generated
def samplifico4(request):
    return render(request, "samplific4lier.html")
    
def samplifico1(request):
    return render(request, "samplific1lier.html")

def samplifico2(request):
    return render(request, "samplific2lier.html")

def samplifico3(request):
    return render(request, "samplific3lier.html")

def samplifico5(request):
    return render(request, "samplific5lier.html")

def samplifico6(request):
    return render(request, "samplific6lier.html")

def samplifico7(request):
    return render(request, "samplific7lier.html")

def samplifico8(request):
    return render(request, "samplific8lier.html")

def samplifico9(request):
    return render(request, "samplific9lier.html")

def samplifico10(request):
    return render(request, "samplific10lier.html")

def samplifico11(request):
    return render(request, "samplific11lier.html")

def samplifico12(request):
    return render(request, "samplific12lier.html")

def samplifico13(request):
    return render(request, "samplific13lier.html")

def samplifico14(request):
    return render(request, "samplific14lier.html")

def samplifico15(request):
    return render(request, "samplific15lier.html")

def samplifico16(request):
    return render(request, "samplific16lier.html")

# This ends the function for the letterhead

# The about function goes here
def aboutus(request):
    return render(request, "aboutus.html")

# The privacypolicy function goes here
def privacypolicy(request):
    return render(request, "privacypolicy.html")