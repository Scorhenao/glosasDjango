from django.shortcuts import redirect, render, get_list_or_404
from .models import GlosaForLessDocumentation, GlosaForErrorOFfactoring
from .forms import GlosaForLessDocumentationForm, GlosaForErrorOFfactoringForm

# CRUD less documentation
from django.shortcuts import render, get_object_or_404

def get_one_glosa_less_doc(request, glosa_id):
    try:
        glosa = get_object_or_404(GlosaForLessDocumentation, pk=glosa_id)
    except Exception as e:
        return render(request, 'glosas/one_glosa.html', {
            'status': 500, 
            'data': None, 
            'message': f'Error: {str(e)}'
        })

    return render(request, 'glosas/one_glosa.html', {
        'status': 200, 
        'data': glosa, 
        'message': 'OK'
    })


from django.shortcuts import render, redirect
from .forms import GlosaForLessDocumentationForm, GlosaForErrorOFfactoringForm

def create_glosa(request):
    if request.method == 'POST':
        form_type = request.POST.get('form_type')

        if form_type == 'less_documentation':
            form = GlosaForLessDocumentationForm(request.POST)
            if form.is_valid():
                try:
                    form.save()
                    return redirect('GetAllGlosas')
                except Exception as e:
                    return render(request, 'glosas/create_glosa.html', {
                        'status': 500,
                        'message': f'Error al crear glosa (Documentos Faltantes): {str(e)}'
                    })
        elif form_type == 'error_factoring':
            form = GlosaForErrorOFfactoringForm(request.POST)
            if form.is_valid():
                try:
                    form.save()
                    return redirect('GetAllGlosas')
                except Exception as e:
                    return render(request, 'glosas/create_glosa.html', {
                        'status': 500,
                        'message': f'Error al crear glosa (Error Facturación): {str(e)}'
                    })
    
    return render(request, 'glosas/create_glosa.html', {
        'status': 400,
        'message': 'Solicitud inválida'
    })


def update_glosa_less_doc(request, glosa_id):
    glosa = get_object_or_404(GlosaForLessDocumentation, pk=glosa_id)

    if request.method == 'POST':
        form = GlosaForLessDocumentationForm(request.POST, instance=glosa)
        if form.is_valid():
            try:
                form.save()
                return redirect('get_one_glosa', glosa_id=glosa_id) 
            except Exception as e:
                return render(request, 'glosas/update_glosa.html', {'form': form, 'glosa': glosa, 'message': f'Error al actualizar: {str(e)}'})
    else:
        form = GlosaForLessDocumentationForm(instance=glosa)  
    
def delete_glosa_less_doc(request, glosa_id):
    glosa = get_object_or_404(GlosaForLessDocumentation, pk=glosa_id)
    
    if request.method == 'POST':
        try:
            glosa.delete()
            return redirect('GetAllGlosas')
        except Exception as e:
            print(str(e))
            return render(request, 'glosas/one_glosa.html', {
                'status': 500,
                'data': None,
                'message': 'Error deleting glosa'
            })

    return render(request, 'glosas/one_glosa.html', {
        'status': 200,
        'data': glosa,
        'message': '¿Estás seguro que deseas eliminar esta glosa?'
    })


# CRUD error factoring 
def get_all_glosas(request):
    try:
        glosas_less_doc = GlosaForLessDocumentation.objects.all()
        glosas_error_factoring = GlosaForErrorOFfactoring.objects.all()
    except Exception as e:
        return render(request, 'glosas/glosas.html', {
            'status': 500,
            'data_less_doc': [],
            'data_error_factoring': [],
            'message': f'Error al cargar las glosas: {str(e)}'
        })
    
    return render(request, 'glosas/glosas.html', {
        'status': 200,
        'data_less_doc': glosas_less_doc,
        'data_error_factoring': glosas_error_factoring,
        'message': 'OK'
    })

def get_one_glosa_error_factoring(request, glosa_id):
    try:
        glosa = get_object_or_404(GlosaForErrorOFfactoring, pk=glosa_id)
    except Exception as e:
        return render(request, 'glosas/one_glosa.html', {
            'status': 500, 
            'data': None, 
            'message': f'Error: {str(e)}'
        })

    return render(request, 'glosas/one_glosa.html', {
        'status': 200, 
        'data': glosa, 
        'message': 'OK'
    })

def update_glosa_error_factoring(request, glosa_id):
    glosa = get_object_or_404(GlosaForErrorOFfactoring, pk=glosa_id)

    if request.method == 'POST':
        form = GlosaForErrorOFfactoringForm(request.POST, instance=glosa)
        if form.is_valid():
            try:
                form.save()
                return redirect('get_one_glosa', glosa_id=glosa_id) 
            except Exception as e:
                return render(request, 'glosas/update_glosa.html', {'form': form, 'glosa': glosa, 'message': f'Error al actualizar: {str(e)}'})
    else:
        form = GlosaForErrorOFfactoringForm(instance=glosa)
    
    return render(request, 'glosas/update_glosa.html', {'form': form, 'glosa': glosa})

def delete_glosa_error_factoring(request, glosa_id):
    glosa = get_object_or_404(GlosaForErrorOFfactoring, pk=glosa_id)
    
    if request.method == 'POST':
        try:
            glosa.delete()
            return redirect('GetAllGlosas')
        except Exception as e:
            print(str(e))
            return render(request, 'glosas/one_glosa.html', {
                'status': 500,
                'data': None,
                'message': 'Error deleting glosa'
            })

    return render(request, 'glosas/one_glosa.html', {
        'status': 200,
        'data': glosa,
        'message': '¿Estás seguro que deseas eliminar esta glosa?'
    })

