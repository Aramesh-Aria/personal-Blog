from django.shortcuts import render, redirect
from django.views.generic import TemplateView, DetailView, FormView
from django.urls import reverse_lazy
from django.contrib import messages
from django.conf import settings
from .models import Project, ContactMessage
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        overview_points = list(self.object.overview_points.order_by('id'))
        section_titles = [
            "مسئله / Problem",
            "راه‌حل / Solution",
            "تصمیم‌های فنی / Technical Decisions",
            "نتیجه / Outcome",
        ]
        structured_overview = []
        for idx, title in enumerate(section_titles):
            text = overview_points[idx].text if idx < len(overview_points) else ""
            structured_overview.append({
                "title": title,
                "text": text,
            })
        context['structured_overview'] = structured_overview
        return context

class ServiceDetailView(TemplateView):
    template_name = 'portfolio/service-details.html'

class ContactProcessView(FormView):
    form_class = ContactForm
    template_name = 'portfolio/index.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        # Save the message to the database
        ContactMessage.objects.create(
            name=form.cleaned_data['name'],
            email=form.cleaned_data['email'],
            subject=form.cleaned_data['subject'],
            message=form.cleaned_data['message']
        )
        
        messages.success(self.request, "Your message has been sent. Thank you!")
        return redirect(self.get_success_url() + '#contact')

    def form_invalid(self, form):
        # If the form is invalid, we need to re-render the index page with errors.
        return render(self.request, self.template_name, {
            'projects': Project.objects.all(),
            'form': form,
            'anchor': 'contact'
        })
