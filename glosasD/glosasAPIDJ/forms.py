from django import forms
from .models import GlosaForLessDocumentation, GlosaForErrorOFfactoring

class GlosaForLessDocumentationForm(forms.ModelForm):
    class Meta:
        model = GlosaForLessDocumentation
        fields = ['_code_glosa', '_description', '_rejected_amount', '_missed_documents']

class GlosaForErrorOFfactoringForm(forms.ModelForm):
    class Meta: 
        model = GlosaForErrorOFfactoring
        fields = ['_code_glosa', '_description', '_rejected_amount', '_type_error']