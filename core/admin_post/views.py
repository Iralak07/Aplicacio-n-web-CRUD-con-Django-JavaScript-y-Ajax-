from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
# Importamos nuestro modelos para usarlos en las vistas
from core.admin_post.models import Category
# Reverse_lazy = Es útil cuando necesita usar una inversión de URL antes de que su proyecto URLConf está cargado. Algunos casos comunes donde esta función es necesaria son:
from django.urls import reverse_lazy
# Importaremos nuestro formulario
from .forms.categoria.forms import FormCategory

# jzonresponse para enviar datos en formato jzon al ajax
from django.http import JsonResponse


class DashBoardView(TemplateView):
    template_name = 'admin/dashboard.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Dashboard' 
        context['title_model'] = "Bienvenido al Tablero"
        return context
    
    
class ListCategoryView(ListView):
    template_name = "admin/lista_categorias.html"
    model = Category
    
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self,request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'search':
                data = list(Category.objects.all().values_list())
                return JsonResponse(data,safe=False)
            elif action == 'cargar':
                form = FormCategory(request.POST)
                if form.is_valid():
                    form.save()
                    return JsonResponse(data, safe=False)
                else:
                    data['error'] = "Esta categoria ya existe, vuelva a intentar"
                    return JsonResponse(data,safe=False)
            elif action == 'edit':
                pk = request.POST['id']
                objeto = Category.objects.get(pk=pk)
                form = FormCategory(request.POST, instance=objeto)
                if form.is_valid():
                    form.save()
                    return JsonResponse(data, safe=False)
                else:
                    data['error'] = "Esta categoria ya existe, vuelva a intentar"
                    return JsonResponse(data,safe=False)
            elif action == 'delete':
                try:
                    pk = request.POST['data']
                    objeto = Category.objects.get(pk=pk)
                    objeto.delete()
                    return JsonResponse(data, safe=False)
                except Exception as e:
                    data['error'] = f'Error de excepcion en el servidor: {str(e)}'
                    return JsonResponse(data,safe=False)
        except Exception as e:
            data['error'] = f'Error de excepcion en el servidor: {str(e)}'
            return JsonResponse(data,safe=False)
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Categorias"
        context["title_model"] = "Listado de categorias"
        context['title_modal'] = "Ingrese una categoria nueva"
        context['modal'] = FormCategory()
        return context
    

