from django.shortcuts import render,get_object_or_404
from .models import Tweet
from django.views.generic import (DetailView,
                                  ListView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)
from django.urls import reverse_lazy,reverse
from .forms import TweetModelForm
from .mixins import FormUserNeededMixin,UserOwnerMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q


class TweetCreateView(FormUserNeededMixin,CreateView):
    form_class =TweetModelForm
    template_name = "tweets/create_view.html"
    # success_url = "/tweet/create/"
    # success_url = reverse_lazy("tweet:detail")


class TweetUpdateView(LoginRequiredMixin, UserOwnerMixin, UpdateView):
    queryset = Tweet.objects.all()
    form_class= TweetModelForm
    template_name = "tweets/update_view.html"


class TweetDeleteView(LoginRequiredMixin, DeleteView):
    model = Tweet
    template_name = "tweets/delete_confirm.html"
    success_url = reverse_lazy("tweet:list")



class TweetDetailView(DetailView):
    queryset = Tweet.objects.all()

    # template_name = "tweets/detail_view.html"

    # def get_object(self):
    #     print(self.kwargs)
    #     pk=self.kwargs.get('pk')
    #     print(pk)
    #     obj = get_object_or_404(Tweet,pk=pk)
    #     return obj


class TweetListView(ListView):
    # template_name = "tweets/list_view.html"
    def get_queryset(self,*args,**kwargs):
        qs = Tweet.objects.all()
        print(self.request.GET)
        query= self.request.GET.get("q",None)
        if query is not None:
            qs = qs.filter(
                            Q(content__icontains=query)|
                            Q(user__username__icontains=query)
                           )
        return qs


    def get_context_data(self, *args,**kwargs):
        context =super(TweetListView,self).get_context_data(*args,**kwargs)
        return context













'''
def tweet_create_view(request):
    form = TweetModelForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
    context={
        "form":form
    }

    return render(request,"tweets/create_view.html",context)



def tweet_detail_view(request,pk=None):
    # obj = Tweet.objects.get(pk=pk)
    obj = get_object_or_404(Tweet,pk=pk)
    print(obj)
    context ={
        "object": obj
    }
    return render(request, "tweets/detail_view.html",context)


def tweet_list_view(request):
    queryset = Tweet.objects.all()
    for obj in queryset:
        print(obj.content)
    context={
        "object_list": queryset
    }
    return render(request, "tweets/list_view.html", context)



'''



