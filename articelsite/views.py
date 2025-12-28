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

def contact(request):
    if request.method == "POST":
        if request.POST.get("email") == "" or request.POST.get("message") == "" or request.POST.get("name") == "":
            return render(request, 'contact.html')
        else:
            user_email = request.POST.get("email")
            message = request.POST.get("message")
            name = request.POST.get("name")

            send_mail(
                subject="Poizraelsku kontakt",
                message=f"Person's E-Mail: {user_email}\n\nHis name: {name}\n\nMessage:\n{message}",
                from_email=f"{user_email}",
                recipient_list=["robin.jerome.kaluzny@gmail.com", "jaquelinekaluzny.ch@gmail.com"],
                fail_silently=False,
            )
            htmlResponse = '<h1>E-Mail został wysłany do Po Izraelsku Team!</h1> <a href="../contact/">Spowrotem ←</a>'
        
            return HttpResponse(htmlResponse)
    return render(request, 'contact.html')

def aboutUs(request):
    return render(request, 'about-us.html')