from django.shortcuts import redirect, render, redirect, get_list_or_404, get_object_or_404
from .models import GlosaForLessDocumentation, GlosaForErrorOFfactoring
from .forms import GlosaForLessDocumentationForm, GlosaForErrorOFfactoringForm


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

def update_glosa(request, glosa_id):
    # Verificar si la vista se está llamando
    print("Vista update_glosa llamada")

    # Inicializamos la glosa y form_type
    glosa = None
    form_type = None

    # Intentar obtener la glosa correspondiente (de ambos modelos)
    glosa_less_doc = None
    glosa_error_fact = None

    # Buscar primero GlosaForLessDocumentation
    try:
        glosa_less_doc = get_object_or_404(GlosaForLessDocumentation, pk=glosa_id)
    except:
        glosa_less_doc = None

    # Buscar luego GlosaForErrorOFfactoring si no se encontró una de tipo 'less_documentation'
    try:
        glosa_error_fact = get_object_or_404(GlosaForErrorOFfactoring, pk=glosa_id)
    except:
        glosa_error_fact = None

    # Si no encontramos ninguna glosa, mostramos un mensaje de error
    if not glosa_less_doc and not glosa_error_fact:
        return render(request, 'glosas/one_glosa.html', {
            'status': 404,
            'data': None,
            'message': 'Glosa no encontrada'
        })

    # Determinamos el tipo de glosa
    if glosa_less_doc:
        glosa = glosa_less_doc
        form_type = 'less_documentation'
    elif glosa_error_fact:
        glosa = glosa_error_fact
        form_type = 'error_factoring'

    # Si es un GET, mostramos el formulario con los datos de la glosa
    if request.method == 'GET':
        # Crear el formulario dependiendo del tipo de glosa
        if form_type == 'less_documentation':
            form = GlosaForLessDocumentationForm(instance=glosa)
        elif form_type == 'error_factoring':
            form = GlosaForErrorOFfactoringForm(instance=glosa)

        return render(request, 'glosas/update_glosa.html', {
            'glosa': glosa,
            'glosa_type': form_type,
            'form': form
        })

    # Si es un POST, procesamos el formulario
    if request.method == 'POST':
        form_type = request.POST.get('form_type')  # Aquí obtenemos el form_type del POST

        if form_type == 'less_documentation':
            form = GlosaForLessDocumentationForm(request.POST, instance=glosa)
            if form.is_valid():
                try:
                    form.save()
                    return redirect('GetAllGlosas')
                except Exception as e:
                    return render(request, 'glosas/update_glosa.html', {
                        'glosa': glosa,
                        'glosa_type': 'less_documentation',
                        'message': f'Error al actualizar (Documentos Faltantes): {str(e)}',
                        'form': form
                    })
        elif form_type == 'error_factoring':
            form = GlosaForErrorOFfactoringForm(request.POST, instance=glosa)
            if form.is_valid():
                try:
                    form.save()
                    return redirect('GetAllGlosas')
                except Exception as e:
                    return render(request, 'glosas/update_glosa.html', {
                        'glosa': glosa,
                        'glosa_type': 'error_factoring',
                        'message': f'Error al actualizar (Error Facturación): {str(e)}',
                        'form': form
                    })

    # Si algo sale mal, devolver el mensaje de error
    return render(request, 'glosas/update_glosa.html', {
        'glosa': glosa,
        'message': 'Error desconocido al intentar actualizar la glosa'
    })


from django.shortcuts import render, get_object_or_404, redirect
from .models import GlosaForLessDocumentation, GlosaForErrorOFfactoring

def delete_glosa(request, glosa_id):
    # Intentamos obtener la glosa de ambos tipos
    glosa = None
    try:
        glosa = get_object_or_404(GlosaForLessDocumentation, pk=glosa_id)
        glosa_type = 'less_documentation'
    except:
        try:
            glosa = get_object_or_404(GlosaForErrorOFfactoring, pk=glosa_id)
            glosa_type = 'error_factoring'
        except:
            glosa_type = None

    # Si no encontramos la glosa, mostramos un error
    if glosa is None:
        return render(request, 'glosas/one_glosa.html', {
            'status': 404,
            'data': None,
            'message': 'Glosa no encontrada'
        })

    # Intentar acceder a code_glosa, si no existe, se muestra un valor por defecto
    code_glosa = getattr(glosa, 'code_glosa', 'No disponible')

    # Si la solicitud es POST, intentamos eliminar la glosa
    if request.method == 'POST':
        try:
            glosa.delete()
            return redirect('GetAllGlosas')  # Redirige a la lista de glosas
        except Exception as e:
            return render(request, 'glosas/one_glosa.html', {
                'status': 500,
                'data': None,
                'message': f'Error al eliminar la glosa: {str(e)}'
            })

    # Si la solicitud es GET, mostramos la página de confirmación
    return render(request, 'glosas/delete_glosa.html', {
        'status': 200,
        'data': glosa,
        'glosa_type': glosa_type,
        'code_glosa': code_glosa,
        'message': f'¿Estás seguro que deseas eliminar la glosa con código {code_glosa}?'
    })
