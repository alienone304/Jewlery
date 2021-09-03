from django.urls import include, path
from company.views import (ContactUsView, AboutUsView, ContactUsListView,
                            ContactUsDeleteView, FAQsView, TermandConditionsView)

app_name ='company'
urlpatterns = [
    path('about-us/',AboutUsView, name = 'aboutus'),
    path('faqs/', FAQsView, name = 'faqs'),
    path('terms-and-conditions/',TermandConditionsView, name = 'termsandconditions'),
    path('contact-us/',ContactUsView, name = 'contactus'),
    path('contact-us-list/',ContactUsListView, name = 'contactuslist'),
    path('contact-us-delete/<int:pk>',ContactUsDeleteView, name = 'contact-us-delete'),

]
