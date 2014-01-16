from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, RequestContext, Http404, HttpResponseRedirect# Create your views here.
from django.core.mail import send_mail

from .models import Contact
from .forms import ContactForm


def contact_us(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        this_form = form.save(commit=False)
        this_form.save
        sent = send_mail('Mesage from Fitwirr fitness website', str(this_form.message), str(this_form.email), ['djohnyal@gmail.com'])
        if sent:
            send_mail('Mail sent', 'Fitwirr', 'contactus@fitwirr.com',['contactus@fitwirr.com'])
            return HttpResponseRedirect('/thankyou/')
    return render_to_response('contact/contact_us.html', locals(), context_instance=RequestContext(request))




def thankyou(request):
    return render_to_response('contact/thankyou.html', locals(), context_instance=RequestContext(request))





def team(request):
    return render_to_response('contact/team.html', locals(), context_instance=RequestContext(request))


def terms(request):
    return render_to_response('contact/terms.html', locals(), context_instance=RequestContext(request))


def privacy(request):
    return render_to_response('contact/privacy.html', locals(), context_instance=RequestContext(request))

