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
        context['og_title'] = 'Aria Aramesh — Backend Developer'
        context['og_description'] = 'Backend developer focused on Python, Django, and PostgreSQL. Building real-world applications from idea to production.'
        context['og_image'] = f"{settings.SITE_URL}{settings.STATIC_URL}img/profile-4.webp"
        context['og_url'] = f"{settings.SITE_URL}/"
        context['og_type'] = 'profile'
        return context

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'portfolio/project-details.html'
    context_object_name = 'project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        overview_points = list(self.object.overview_points.order_by('id'))
        section_titles = [
            "مسئله",
            "راه‌حل",
            "تصمیم‌های فنی",
            "نتیجه",
        ]
        structured_overview = []
        for idx, title in enumerate(section_titles):
            text = overview_points[idx].text if idx < len(overview_points) else ""
            structured_overview.append({
                "title": title,
                "text": text,
            })
        context['structured_overview'] = structured_overview

        # OG metadata
        project = self.object
        context['og_title'] = project.title
        description_parts = [s['text'] for s in structured_overview if s['text']]
        context['og_description'] = ' '.join(description_parts)[:160]
        if project.og_image:
            context['og_image'] = f"{settings.SITE_URL}{settings.MEDIA_URL}{project.og_image}"
        else:
            context['og_image'] = f"{settings.SITE_URL}{settings.MEDIA_URL}{project.image}"
        context['og_url'] = f"{settings.SITE_URL}{self.request.path}"
        context['og_type'] = 'article'
        return context

class ServiceDetailView(TemplateView):
    template_name = 'portfolio/service-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['og_title'] = 'Services - Aria Aramesh'
        context['og_description'] = 'Backend development services including Python, Django, PostgreSQL, and more.'
        context['og_image'] = f"{settings.SITE_URL}{settings.STATIC_URL}img/og-image.webp"
        context['og_url'] = f"{settings.SITE_URL}{self.request.path}"
        context['og_type'] = 'website'
        return context

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
