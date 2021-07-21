from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from core.main.models import Category, Product, Client, Sale


class DashboardView(TemplateView):
    template_name = 'dashboard.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    # def get(self, request, *args, **kwargs):
    #     request.user.get_group_session()
    #     return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['panel'] = 'Panel de administrador'
        # context['graph_sale_years'] = self.get_graph_sales_years_month()
        context['entity_count'] = countEntity()
        return context


def countEntity():
    return {
        'cat': Category.objects.count(),
        'prod': Product.objects.count(),
        'cli': Client.objects.count(),
        'sale': Sale.objects.count(),
    }


class CountView(View):
    pass
