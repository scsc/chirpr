# from django.http import HttpResponse
from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic.base import RedirectView
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'chirpr/index.html')
    # return HttpResponse("Hello!")


class RedirectToIndex(RedirectView):
    url = reverse_lazy('index')


@login_required
def chirp(request):
    pass