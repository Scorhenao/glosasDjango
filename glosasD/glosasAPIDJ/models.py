from django.db import models

class Glosa(models.Model):
    _code_glosa = models.CharField(max_length=10)
    _description = models.TextField()
    _rejected_amount = models.DecimalField(max_digits=10, decimal_places=2)
    
    def show_info(self):
        return f"Código: {self._code_glosa}, Descripción: {self._description}, Monto rechazado: {self._rejected_amount}"

    @property
    def getCodigoGlosa(self):
        return self._code_glosa
    
    @property
    def getDescriptionGlosa(self):
        return self._description
    @property  
    def getRejectedAmount(self):
        return self._rejected_amount

class GlosaForLessDocumentation(Glosa):
    _missed_documents = models.TextField()
    
    def show_info(self):
        return super().show_info() + f", Documentos faltantes: {self._missed_documents}"

    @property
    def getMissedDocuments(self):
        return self._missed_documents
class GlosaForErrorOFfactoring(Glosa):
    _type_error = models.CharField(max_length=100)
    
    def show_info(self):
        return super().show_info() + f", Tipo de error: {self._type_error}"
    
    @property
    def getTypeError(self):
        return self._type_error