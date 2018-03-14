from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.http import Http404

from .models import Fanfic

# My first view~

def index(request):
	# now rewritten a bunch~
	latest_fanfic_list = Fanfic.objects.order_by('-pub_date')[:5]
	context = {'latest_fanfic_list': latest_fanfic_list}
	return render(request, 'fic/index.html', context)

# new view added in tutorial part 3

def detail(request, fanfic_id):
	# now modifiying this to return 404 if fanfic
	# does not exist
	fanfic = get_object_or_404(Fanfic, pk=fanfic_id)
	return render(request, 'fic/detail.html', {'fanfic':fanfic})
