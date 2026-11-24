import tempfile
import unittest
from pathlib import Path

from cadastro_urls import CadastroURLs
from navegador import Navegador


class TesteNavegador(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.base = Path(self.temp.name)
        self.urls = self.base / "urls.txt"
        self.paginas = self.base / "paginas"
        self.urls.write_text("www.exemplo.com\n", encoding="utf-8")
        self.cadastro = CadastroURLs(self.paginas, self.urls)
        self.cadastro.carregar_arquivo()
        self.navegador = Navegador(self.cadastro)

    def tearDown(self):
        self.temp.cleanup()

    def test_acesso_ao_dominio(self):
        self.assertEqual(self.navegador.acessar("www.exemplo.com"), "www.exemplo.com")

    def test_pagina_interna(self):
        self.cadastro.adicionar("www.exemplo.com/secao", "Conteúdo da seção")
        self.navegador.acessar("www.exemplo.com")
        self.assertEqual(self.navegador.acessar("/secao"), "www.exemplo.com/secao")

    def test_arquivo_da_pagina(self):
        self.cadastro.adicionar("www.exemplo.com/secao", "Texto de teste")
        self.assertEqual(
            Path(self.cadastro.obter_arquivo("www.exemplo.com/secao")).read_text(encoding="utf-8").strip(),
            "Texto de teste"
        )

    def test_erro_404_nao_altera_estado(self):
        self.navegador.acessar("www.exemplo.com")
        with self.assertRaises(ValueError):
            self.navegador.acessar("www.inexistente.com")
        self.assertEqual(self.navegador.pagina_atual, "www.exemplo.com")
        self.assertEqual(self.navegador.obter_historico_formatado(), "")

    def test_voltar(self):
        self.cadastro.adicionar("www.exemplo.com/outra", "Outra página")
        self.navegador.acessar("www.exemplo.com")
        self.navegador.acessar("/outra")
        self.assertEqual(self.navegador.voltar(), "www.exemplo.com")


if __name__ == "__main__":
    unittest.main()
