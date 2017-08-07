from django.shortcuts import render, get_object_or_404
from .models import Tweet
from django.views.generic import DetailView, ListView

# Create your views here.


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
    queryset = Tweet.objects.all()

    def get_context_data(self, *args,**kwargs):
        context =super(TweetListView,self).get_context_data(*args,**kwargs)
        # context['another tweet']=Tweet.objects.all()
        # print(context)
        return context








'''


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



