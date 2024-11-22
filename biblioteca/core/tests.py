from django.test import TestCase
from django.contrib.auth.models import User
from .models import Categoria, Autor, Livro, Colecao
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

class ColecaoTests(TestCase):
    def setUp(self):
        # Configurar APIClient para incluir autenticação JWT
        self.client = APIClient()

        # Criar usuários
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.outro_user = User.objects.create_user(username='outro_usuario', password='senha456')

        # Gerar token JWT para o usuário principal
        self.user_token = str(RefreshToken.for_user(self.user).access_token)
        self.outro_user_token = str(RefreshToken.for_user(self.outro_user).access_token)

        # Criar dados necessários para testes
        self.autor = Autor.objects.create(nome="Autor Exemplo")
        self.categoria = Categoria.objects.create(nome="Categoria Exemplo")
        self.livro = Livro.objects.create(
            titulo="Livro Exemplo",
            autor=self.autor,
            categoria=self.categoria,
            publicado_em="2023-01-01"
        )
        self.colecao = Colecao.objects.create(
            nome="Coleção Exemplo",
            colecionador=self.user
        )
        self.colecao.livros.add(self.livro)

    def test_criar_colecao(self):
        # Autenticar com o token do usuário
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.user_token}')

        # Testa a criação de uma nova coleção
        response = self.client.post(reverse('colecao-list-create'), {
            'nome': "Nova Coleção",
            'livros': [self.livro.id]
        })
        self.assertEqual(response.status_code, 201)  # Verifica se a resposta é 201 (Criado)
        nova_colecao = Colecao.objects.get(nome="Nova Coleção")
        self.assertEqual(nova_colecao.colecionador, self.user)

    def test_permissoes_acesso_gerenciamento(self):
        # Autenticar com o token do usuário
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.user_token}')

        # Usuário autenticado tenta editar a coleção
        response = self.client.patch(reverse('colecao-detail', kwargs={'pk': self.colecao.id}), {
            'nome': "Coleção Editada"
        })
        self.assertEqual(response.status_code, 200)
        self.colecao.refresh_from_db()
        self.assertEqual(self.colecao.nome, "Coleção Editada")

        # Outro usuário tenta editar
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.outro_user_token}')
        response = self.client.patch(reverse('colecao-detail', kwargs={'pk': self.colecao.id}), {
            'nome': "Tentativa de Edição"
        })
        self.assertEqual(response.status_code, 403)

        # Usuário autenticado tenta excluir
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.user_token}')
        response = self.client.delete(reverse('colecao-detail', kwargs={'pk': self.colecao.id}))
        self.assertEqual(response.status_code, 204)

    def test_usuarios_nao_autenticados_nao_podem_criar_ou_editar(self):
        # Remover autenticação
        self.client.credentials()

        # Teste para criação de coleção (usuário não autenticado)
        response = self.client.post(reverse('colecao-list-create'), {
            'nome': "Nova Coleção",
            'livros': [self.livro.id]
        })
        self.assertEqual(response.status_code, 401)

        # Teste para edição de coleção (usuário não autenticado)
        response = self.client.patch(reverse('colecao-detail', kwargs={'pk': self.colecao.id}), {
            'nome': "Tentativa de Edição"
        })
        self.assertEqual(response.status_code, 401)

    def test_listagem_de_colecao_para_usuario_autenticado(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.user_token}')

        response = self.client.get(reverse('colecao-list-create'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.colecao.nome)

    def test_listagem_de_colecao_para_usuario_nao_autenticado(self):
        self.client.credentials()
        response = self.client.get(reverse('colecao-list-create'))
        self.assertEqual(response.status_code, 401)
