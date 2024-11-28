from django.shortcuts import redirect, render, get_list_or_404
from .models import GlosaForLessDocumentation, GlosaForErrorOFfactoring
from .forms import GlosaForLessDocumentationForm

# CRUD less documentation
def get_all_glosas_less_doc(request):
    try:
        glosas = GlosaForLessDocumentation.objects.all()
    except:
        glosas = []
    return render(request, 'glosas/glosas.html', {'status': 200, 'data':glosas, 'message': 'OK'})

from django.shortcuts import render, get_object_or_404

def get_one_glosa_less_doc(request, glosa_id):
    try:
        # Intentamos obtener la glosa
        glosa = get_object_or_404(GlosaForLessDocumentation, pk=glosa_id)
    except Exception as e:
        # Si no se encuentra la glosa, se muestra un mensaje de error
        return render(request, 'glosas/one_glosa.html', {
            'status': 500, 
            'data': None, 
            'message': f'Error: {str(e)}'
        })

    # Si se encuentra la glosa, mostrarla
    return render(request, 'glosas/one_glosa.html', {
        'status': 200, 
        'data': glosa, 
        'message': 'OK'
    })


def create_glosa_less_doc(request):
    glosa = None
    if request.method == 'POST':
        form = GlosaForLessDocumentationForm(request.POST)
        if form.is_valid():
            try:
                glosa = form.save()  
                return render(request, 'glosas/glosas.html', {'status': 201, 'data': [glosa], 'message': 'Glosa created successfully'})
            except Exception as e:
                return render(request, 'glosas/glosas.html', {'status': 500, 'data': None, 'message': f'Error creating glosa: {str(e)}'})
    else:
        form = GlosaForLessDocumentationForm()
    return render(request, 'glosas/create_glosa.html', {'status': 400, 'form': form, 'message': 'Bad request'})


def update_glosa_less_doc(request, glosa_id):
    glosa = get_object_or_404(GlosaForLessDocumentation, pk=glosa_id)

    if request.method == 'POST':
        form = GlosaForLessDocumentationForm(request.POST, instance=glosa)
        if form.is_valid():
            try:
                form.save()  # Guarda los cambios del formulario
                return redirect('get_one_glosa', glosa_id=glosa_id) 
            except Exception as e:
                return render(request, 'glosas/update_glosa.html', {'form': form, 'glosa': glosa, 'message': f'Error al actualizar: {str(e)}'})
    else:
        form = GlosaForLessDocumentationForm(instance=glosa)  
    
def delete_glosa_less_doc(request, glosa_id):
    # Obtener la glosa utilizando get_object_or_404
    glosa = get_object_or_404(GlosaForLessDocumentation, pk=glosa_id)
    
    if request.method == 'POST':
        try:
            glosa.delete()  # Eliminar la glosa
            return redirect('GetAllGlosas')  # Redirigir a la vista que lista todas las glosas
        except Exception as e:
            print(str(e))
            return render(request, 'glosas/one_glosa.html', {
                'status': 500,
                'data': None,
                'message': 'Error deleting glosa'
            })

    # Si la solicitud es GET, mostrar la confirmación de eliminación
    return render(request, 'glosas/one_glosa.html', {
        'status': 200,
        'data': glosa,
        'message': '¿Estás seguro que deseas eliminar esta glosa?'
    })


# CRUD error factoring 
