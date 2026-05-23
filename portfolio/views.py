from django.shortcuts import render, redirect
from django.views.generic import TemplateView, DetailView, FormView
from django.urls import reverse_lazy
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Project
from .forms import ContactForm

class IndexView(TemplateView):
    template_name = 'portfolio/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.all()
        context['form'] = ContactForm()
        return context

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'portfolio/project-details.html'
    context_object_name = 'project'

class ServiceDetailView(TemplateView):
    template_name = 'portfolio/service-details.html'

class ContactProcessView(FormView):
    form_class = ContactForm
    template_name = 'portfolio/index.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']

        full_subject = f"[Portfolio Contact] {subject}"
        full_message = f"New message from portfolio contact form:\n\nName: {name}\nEmail: {email}\nSubject: {subject}\n\nMessage:\n{message}"
        
        try:
            send_mail(
                full_subject,
                full_message,
                settings.DEFAULT_FROM_EMAIL,
                [settings.CONTACT_RECEIVER_EMAIL],
                reply_to=[email],
                fail_silently=False,
            )
            messages.success(self.request, "Your message has been sent. Thank you!")
        except Exception as e:
            print("CONTACT_EMAIL_SEND_FAILED", repr(e))
            messages.error(self.request, "Sorry—your message could not be sent right now. Please try again later.")
        
        return redirect(self.get_success_url() + '#contact')

    def form_invalid(self, form):
        # If the form is invalid, we need to re-render the index page with errors.
        return render(self.request, self.template_name, {
            'projects': Project.objects.all(),
            'form': form,
            'anchor': 'contact'
        })
