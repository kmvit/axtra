from django.shortcuts import render
from django.views import generic
from .models import Work


class WorklistView(generic.ListView):
    template_name = 'portfolio/work_list.html'
    queryset = Work.objects.all()


class WorkDetailView(generic.DetailView):
    template_name = 'portfolio/work_detail.html'
    queryset = Work.objects.all()

    def get_context_data(self, **kwargs):
        context = super(WorkDetailView, self).get_context_data(**kwargs)
        context['recent_works'] = Work.objects.all().exclude(id=self.object.id)
        return context
