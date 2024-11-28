from django import forms
from .models import GlosaForLessDocumentation

class GlosaForLessDocumentationForm(forms.ModelForm):
    class Meta:
        model = GlosaForLessDocumentation
        fields = ['_code_glosa', '_description', '_rejected_amount', '_missed_documents']
