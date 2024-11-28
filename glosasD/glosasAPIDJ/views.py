from django.shortcuts import render, get_list_or_404
from .models import GlosaForLessDocumentation, GlosaForErrorOFfactoring
from .forms import GlosaForLessDocumentationForm

# CRUD less documentation
def get_all_glosas_less_doc(request):
    try:
        glosas = GlosaForLessDocumentation.objects.all()
    except:
        glosas = []
    return render(request, 'glosas/glosas.html', {'status': 200, 'data':glosas, 'message': 'OK'})

def get_one_glosa_less_doc(request, id):
    try:
        glosa = get_list_or_404(GlosaForLessDocumentation, pk=id)
    except:
        glosa = []
    return render(request, 'glosas/one_glosa.html', {'status': 200, 'data':glosa, 'message': 'OK'})

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

def update_glosa_less_doc(request, id):
    if request.method == 'PUT':
        form = GlosaForLessDocumentationForm(request.PUT)
        if form.is_valid():
            try:
                glosa = get_list_or_404(GlosaForLessDocumentation, pk=id)
                glosa.code_glosa = form.cleaned_data['code_glosa']
                glosa.description = form.cleaned_data['description']
                glosa.rejected_amount = form.cleaned_data['rejected_amount']
                glosa.save()
                return render(request, 'glosas/one_glosa.html', {'status': 200, 'data':glosa, 'message': 'Glosa updated successfully'})
            except:
                return render(request, 'glosas/one_glosa.html', {'status': 500, 'data':glosa, 'message': 'Error updating glosa'})
    else:
        return render(request, 'glosas/one_glosa.html', {'status': 400, 'data':glosa, 'message': 'Bad request'})
    
def delete_glosa_less_doc(request, id):
    try:
        glosa = get_list_or_404(GlosaForLessDocumentation, pk=id)
        glosa.delete()
        return render(request, 'glosas/one_glosa.html', {'status': 200, 'data':glosa, 'message': 'Glosa deleted successfully'})
    except:
        return render(request, 'glosas/one_glosa.html', {'status': 500, 'data':glosa, 'message': 'Error deleting glosa'})
    
# CRUD error factoring 
