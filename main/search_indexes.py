from haystack import indexes
from main.models import Noticia

class NoticiaIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    autor=indexes.EdgeNgramField(model_attr='autor')
    
    titulo=indexes.EdgeNgramField(model_attr='titulo')
    link=indexes.EdgeNgramField(model_attr='link')
    categoria=indexes.EdgeNgramField(model_attr='categoria')
    
    def get_model(self):
        return Noticia
    
    def index_queryset(self, using=None):
        return self.get_model().objects.all()