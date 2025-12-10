from django.shortcuts import render, get_object_or_404
from .models import Articel
from django.views.generic import DetailView
from hitcount.views import HitCountDetailView
from django.core.mail import send_mail
from django.http import HttpResponse

# Create your views here.

class ArticleDetailView(HitCountDetailView):
    model = Articel
    template_name = 'blogs.html'
    count_hit = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articelSuggestion'] = Articel.objects.exclude(
            slug=self.object.slug
        ).order_by('-pub_date')[:2]
        return context

def index(request):

    articelSuggestion = Articel.objects.all().order_by("-pub_date")[:2]

    if request.method == "POST":
        user_email = request.POST.get("email")
        message = request.POST.get("message")

        send_mail(
            subject="Poizraelsku kontakt",
            message=f"E-Mail: {user_email}\n\nNachricht:\n{message}",
            from_email=f"{user_email}",
            recipient_list=["robin.jerome.kaluzny@gmail.com"],
        )

        return HttpResponse("E-Mail wurde gesendet!")
    
    return render(request, 'index.html', {'articelSuggestion': articelSuggestion})


def blogOverview(request):
    articelSuggestion = Articel.objects.all().order_by("-pub_date")
    return render(request, 'blog_overview.html', {'articelSuggestion': articelSuggestion})

def blogOvervieIsrael(request):
    articelSuggestion = Articel.objects.filter(theme='israel').order_by("-pub_date")
    return render(request, 'israel.html', {'articelSuggestion': articelSuggestion})

def blogOvervieBible(request):
    articelSuggestion = Articel.objects.filter(theme='bible').order_by("-pub_date")
    return render(request, 'bible.html', {'articelSuggestion': articelSuggestion})

def blogOvervieTestimonies(request):
    articelSuggestion = Articel.objects.filter(theme='testimonies').order_by("-pub_date")
    return render(request, 'testimonies.html', {'articelSuggestion': articelSuggestion})

def blogs(request, slug):
    articel = get_object_or_404(Articel, slug=slug)
    articelSuggestion = Articel.objects.exclude(slug=slug).order_by("-pub_date")[:2]
    return render(request, 'blogs.html', {'articel': articel, 'articelSuggestion': articelSuggestion,})