from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import About, SkillGroup, Project, Certification, Contact

def home(request):
    about = About.objects.first()
    skill_groups = SkillGroup.objects.prefetch_related('skills')
    projects = Project.objects.all()
    certifications = Certification.objects.all()
    contact = Contact.objects.first()
    return render(request, 'index.html', {
        'about': about,
        'skill_groups': skill_groups,
        'projects': projects,
        'certifications': certifications,
        'contact': contact,
    })

