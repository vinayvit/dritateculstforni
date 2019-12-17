from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .models import Result
from .models import Answer
from .models import Admit
from .models import Admission
from .models import Important
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404

class IndexView(ListView):
    context_object_name = 'home_list'   
    template_name = 'scrp/post_list.html'
    queryset = Post.objects.all()

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.order_by('published_date')[:10]
        context['admit'] = Admit.objects.order_by('published_date')[:10]
        context['answer'] = Answer.objects.order_by('published_date')[:10]
        context['admission'] = Admission.objects.order_by('published_date')[:10]
        context['result'] = Result.objects.order_by('published_date')[:10]		
        context['important'] = Important.objects.order_by('published_date')[:10]    
        return context
		
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'scrp/jobs.html', {'posts': posts})
	
def post_detail(request, pk):
    posts = get_object_or_404(Post, pk=pk)
    return render(request, 'scrp/post_detail.html', {'posts': posts})	
	
def admit(request):
    admit = Admit.objects.all()
    return render(request, 'scrp/admit.html', {'admit': admit})	
	
def admit_detail(request, pk):
    admit = get_object_or_404(Admit, pk=pk)
    return render(request, 'scrp/admit_detail.html', {'admit': admit})	

def answer(request):
    answer = Answer.objects.all()
    return render(request, 'scrp/answer.html', {'answer': answer})
	
def answer_detail(request, pk):
    posts = get_object_or_404(Answer, pk=pk)
    return render(request, 'scrp/answer_detail.html', {'posts': posts})	
	
def admission(request):
    admission = Admission.objects.all()
    return render(request, 'scrp/admission.html', {'admission': admission})
	
def admission_detail(request, pk):
    posts = get_object_or_404(Admission, pk=pk)
    return render(request, 'scrp/admission_detail.html', {'posts': posts})	
	
def result(request):
    result = Result.objects.all()
    return render(request, 'scrp/result.html', {'result': result})
	
def result_detail(request, pk):
    posts = get_object_or_404(Result, pk=pk)
    return render(request, 'scrp/result_detail.html', {'posts': posts})		
	
def important(request):
    important = Important.objects.all()
    return render(request, 'scrp/important.html', {'important': important})
	
def important_detail(request, pk):
    posts = get_object_or_404(Important, pk=pk)
    return render(request, 'scrp/important_detail.html', {'posts': posts})		
	

	
