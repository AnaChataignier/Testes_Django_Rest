from typing import Any
from django.test import TestCase
from aluraflix.models import Programa
from aluraflix.serializers import ProgramaSerializer


class ProgramaSerializerTestCase(TestCase):

    def setUp(self):
        self.programa = Programa(
            titulo="Procurando",
            data_lancamento="2020-07-04",
            tipo="S",
            likes=37898,
            dislikes=79,
        )

        self.serializer = ProgramaSerializer(instance=self.programa)

    def test_verifica_campos_serializados(self):
        """Teste que verifica os campos que estão sendo serializados"""
        data = self.serializer.data
        self.assertEqual(
            set(data.keys()),
            set(["titulo", "data_lancamento", "tipo", "likes", "dislikes"]),
        )

    def test_verifica_conteudos_serializados(self):
        """Teste que verifica conteudo dos campos Serializados"""
        data = self.serializer.data
        self.assertEqual(data["titulo"], self.programa.titulo)
        self.assertEqual(data["data_lancamento"], self.programa.data_lancamento)
        self.assertEqual(data["tipo"], self.programa.tipo)
        self.assertEqual(data["likes"], self.programa.likes)
