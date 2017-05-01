from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from models import Comment

class IndexView(generic.ListView):
    template_name = 'comment/index.html'
    context_object_name = 'comment_board'
    def get_queryset(self):
        return Comment.objects.order_by('-comment_rating')