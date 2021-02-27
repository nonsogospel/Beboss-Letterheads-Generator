from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),    # This is the url pattern for my website homepage
    path('base.html', views.base, name="base"),
    path("contactpage", views.contactpage, name="contactpage"),   # This is the url for the contact us of my website
    # This begins the urls for the letterhead 
    path("generate-letterhead-now", views.generate_letterhead, name="generate_letterhead"),
    path("letterhead_generator", views.letterhead_generator, name="letterhead_generator"),
    path("samples_generated", views.samples_generated, name="samples_generated"),
    path("send-downloaded-letterhead.html", views.attach_send, name="send-downloaded-letterhead"),
    path("samplific4lier.html", views.samplifico4, name="samplifico4"),
    path("generate-letterhead-now-s1", views.generate_letterhead_s1, name="generate_letterhead_s1"),
    path("samplific1lier.html", views.samplifico1, name="samplifico1"),
    path("letterhead_generator_s1", views.letterhead_generator_s1, name="letterhead_generator_s1"),
    path("samplific2lier.html", views.samplifico2, name="samplifico2"),
    path("generate-letterhead-now-s2", views.generate_letterhead_s2, name="generate_letterhead_s2"),
    path("letterhead_generator_s2", views.letterhead_generator_s2, name="letterhead_generator_s2"),
    path("samplific3lier.html", views.samplifico3, name="samplifico3"),
    path("generate-letterhead-now-s3", views.generate_letterhead_s3, name="generate_letterhead_s3"),
    path("letterhead_generator_s3", views.letterhead_generator_s3, name="letterhead_generator_s3"),
    path("samplific5lier.html", views.samplifico5, name="samplifico5"),
    path("generate-letterhead-now-s5.html", views.generate_letterhead_s5, name="generate_letterhead_s5"),
    path("letterhead_generator_s5", views.letterhead_generator_s5, name="letterhead_generator_s5"),
    path("samplific6lier.html", views.samplifico6, name="samplifico6"),
    path("generate-letterhead-now-s6", views.generate_letterhead_s6, name="generate_letterhead_s6"),
    path("letterhead_generator_s6", views.letterhead_generator_s6, name="letterhead_generator_s6"),
    path("samplific7lier.html", views.samplifico7, name="samplifico7"),
    path("generate-letterhead-now-s7", views.generate_letterhead_s7, name="generate_letterhead_s7"),
    path("letterhead_generator_s7", views.letterhead_generator_s7, name="letterhead_generator_s7"),
    path("samplific8lier.html", views.samplifico8, name="samplifico8"),
    path("generate-letterhead-now-s8", views.generate_letterhead_s8, name="generate_letterhead_s8"),
    path("letterhead_generator_s8", views.letterhead_generator_s8, name="letterhead_generator_s8"),
    path("samplific9lier.html", views.samplifico9, name="samplifico9"),
    path("generate-letterhead-now-s9", views.generate_letterhead_s9, name="generate_letterhead_s9"),
    path("letterhead_generator_s9", views.letterhead_generator_s9, name="letterhead_generator_s9"),
    path("samplific10lier.html", views.samplifico10, name="samplifico10"),
    path("generate-letterhead-now-s10", views.generate_letterhead_s10, name="generate_letterhead_s10"),
    path("letterhead_generator_s10", views.letterhead_generator_s10, name="letterhead_generator_s10"),
    path("samplific11lier.html", views.samplifico11, name="samplifico11"),
    path("generate-letterhead-now-s11", views.generate_letterhead_s11, name="generate_letterhead_s11"),
    path("letterhead_generator_s11", views.letterhead_generator_s11, name="letterhead_generator_s11"),
    path("samplific12lier.html", views.samplifico12, name="samplifico12"),
    path("generate-letterhead-now-s12", views.generate_letterhead_s12, name="generate_letterhead_s12"),
    path("letterhead_generator_s12", views.letterhead_generator_s12, name="letterhead_generator_s12"),
    path("samplific13lier.html", views.samplifico13, name="samplifico13"),
    path("generate-letterhead-now-s13", views.generate_letterhead_s13, name="generate_letterhead_s13"),
    path("letterhead_generator_s13", views.letterhead_generator_s13, name="letterhead_generator_s13"),
    path("samplific14lier.html", views.samplifico14, name="samplifico14"),
    path("generate-letterhead-now-s14", views.generate_letterhead_s14, name="generate_letterhead_s14"),
    path("letterhead_generator_s14", views.letterhead_generator_s14, name="letterhead_generator_s14"),
    path("samplific15lier.html", views.samplifico15, name="samplifico15"),
    path("generate-letterhead-now-s15", views.generate_letterhead_s15, name="generate_letterhead_s15"),
    path("letterhead_generator_s15", views.letterhead_generator_s15, name="letterhead_generator_s15"),
    path("samplific16lier.html", views.samplifico16, name="samplifico16"),
    path("generate-letterhead-now-s16", views.generate_letterhead_s16, name="generate_letterhead_s16"),
    path("letterhead_generator_s16", views.letterhead_generator_s16, name="letterhead_generator_s16"),
    # The Letterhead section ends here
    # The Resume / CV resume begins here
    # path("online-resume-cv-samples.html", views.online_resume_cv_generator, name="online_resume_cv_generator"),
    # path("generate-resume-now-cv1.html", views.generate_resume_now_cv1, name="generate_resume_now_cv1"),
    # path("generate-resume-now-cv2.html", views.generate_resume_now_cv2, name="generate_resume_now_cv2")

    # The about center is here
    path('aboutus', views.aboutus, name='aboutus'),
    # The privacypolicy is here
    path('privacypolicy', views.privacypolicy, name='privacypolicy'),
    

]