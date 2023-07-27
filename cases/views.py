from django.views.generic import DetailView, ListView

from .models import Case


class CaselistView(ListView):
    template_name = 'case/case_list.html'
    queryset = Case.objects.all()


class CaseDetailView(DetailView):
    template_name = 'case/case_detail.html'
    queryset = Case.objects.all()

    def get_context_data(self, **kwargs):
        context = super(CaseDetailView, self).get_context_data(**kwargs)
        context['recent_works'] = Case.objects.all().exclude(id=self.object.id)
        return context
