from rest_framework import generics, permissions
from django_filters import rest_framework as filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Livro, Categoria, Autor, Colecao
from .serializers import LivroSerializer, CategoriaSerializer, AutorSerializer, ColecaoSerializer
from .custom_permissions import IsColecionador
from rest_framework.permissions import IsAuthenticated

# Paginação para Colecao
class ColecaoPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

# Filtro para Colecao
class ColecaoFilter(filters.FilterSet):
    nome = filters.CharFilter(lookup_expr='icontains')
    colecionador = filters.CharFilter(field_name='colecionador__username', lookup_expr='icontains')
    class Meta:
        model = Colecao
        fields = ['nome', 'colecionador']

class ColecaoListCreate(generics.ListCreateAPIView):
    queryset = Colecao.objects.all()
    serializer_class = ColecaoSerializer
    permission_classes = [IsAuthenticated]  # Garantir que só usuários autenticados possam acessar
    pagination_class = ColecaoPagination
    filterset_class = ColecaoFilter
    ordering_fields = ['nome', 'colecionador']
    ordering = ['nome']

    def perform_create(self, serializer):
        # A Coleção será associada ao usuário autenticado
        serializer.save(colecionador=self.request.user)

class ColecaoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Colecao.objects.all()
    serializer_class = ColecaoSerializer
    permission_classes = [IsColecionador, IsAuthenticated]  # Permissões para o colecionador e usuário autenticado

    def perform_update(self, serializer):
        # Certificar-se de que o colecionador está atualizado
        serializer.save(colecionador=self.request.user)


class LivroPagination(PageNumberPagination):
    page_size = 10  
    page_size_query_param = 'page_size'  
    max_page_size = 100  

class LivroFilter(filters.FilterSet):
    titulo = filters.CharFilter(lookup_expr='icontains') 
    autor = filters.CharFilter(field_name='autor__nome', lookup_expr='icontains')  
    categoria = filters.AllValuesFilter(field_name='categoria__nome')  

    class Meta:
        model = Livro
        fields = ['titulo', 'autor', 'categoria']

class LivroList(generics.ListCreateAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    pagination_class = LivroPagination  
    permission_classes = [permissions.AllowAny]
    filterset_class = LivroFilter  
    ordering_fields = ['titulo', 'autor', 'categoria', 'publicado_em']  
    ordering = ['titulo']  

    def perform_create(self, serializer):
        serializer.save()  

class LivroDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    name = "livro-detail"
    permission_classes = [permissions.AllowAny]

class CategoriaPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class CategoriaFilter(filters.FilterSet):
    nome = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Categoria
        fields = ['nome']

class CategoriaList(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    pagination_class = CategoriaPagination
    permission_classes = [permissions.AllowAny]
    filterset_class = CategoriaFilter
    ordering_fields = ['nome']
    ordering = ['nome']

    def perform_create(self, serializer):
        serializer.save()

class CategoriaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    name = "categoria-detail"
    permission_classes = [permissions.AllowAny]

class AutorPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class AutorFilter(filters.FilterSet):
    nome = filters.CharFilter(lookup_expr='icontains')  

    class Meta:
        model = Autor
        fields = ['nome']
    
class AutorList(generics.ListCreateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    pagination_class = AutorPagination
    permission_classes = [permissions.AllowAny]
    filterset_class = AutorFilter 
    ordering_fields = ['nome']  
    ordering = ['nome']  

    def perform_create(self, serializer):
        serializer.save() 

class AutorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    name = "autor-detail"
    permission_classes = [permissions.AllowAny]

class HomeView(APIView):
    def get(self, request):
        livros = Livro.objects.all()
        categorias = Categoria.objects.all()
        autores = Autor.objects.all()

        livros_serializados = LivroSerializer(livros, many=True).data
        categorias_serializadas = CategoriaSerializer(categorias, many=True).data
        autores_serializados = AutorSerializer(autores, many=True).data

        return Response({
            "livros": livros_serializados,
            "categorias": categorias_serializadas,
            "autores": autores_serializados
        })