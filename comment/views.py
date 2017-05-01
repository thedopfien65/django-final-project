from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

class IndexView(generic.TemplateView):
    template_name = 'comment/index.html'
    context_object_name = 'comment_board'