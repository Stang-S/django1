from .models import Member
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def about(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))