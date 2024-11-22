from django.urls import path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)
from .views import (
    HomeView,
    LivroList, LivroDetail,
    CategoriaList, CategoriaDetail,
    AutorList, AutorDetail,
    ColecaoListCreate, ColecaoDetail
)

urlpatterns = [

    path('', HomeView.as_view(), name='home'),
    
    path('livros/', LivroList.as_view(), name='livro-list'),
    path('livros/<int:pk>/', LivroDetail.as_view(), name='livro-detail'),
    
    path('categorias/', CategoriaList.as_view(), name='categoria-list'),
    path('categorias/<int:pk>/', CategoriaDetail.as_view(), name='categoria-detail'),
    
    path('autores/', AutorList.as_view(), name='autor-list'),
    path('autores/<int:pk>/', AutorDetail.as_view(), name='autor-detail'),
    
    path('colecoes/', ColecaoListCreate.as_view(), name='colecao-list-create'),  # Corrigido nome da view
    path('colecoes/<int:pk>/', ColecaoDetail.as_view(), name='colecao-detail'),  # Corrigido nome da view
    
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('docs/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
