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

    def test_navegacao_aninhada(self):
        self.cadastro.adicionar("www.exemplo.com/secao", "Seção")
        self.cadastro.adicionar("www.exemplo.com/secao/detalhes", "Detalhes")
        self.navegador.acessar("www.exemplo.com")
        self.navegador.acessar("/secao")
        self.assertEqual(
            self.navegador.acessar("/detalhes"),
            "www.exemplo.com/secao/detalhes"
        )

    def test_arquivo_da_pagina(self):
        self.cadastro.adicionar("www.exemplo.com/secao", "Texto de teste")
        caminho = self.cadastro.obter_arquivo("www.exemplo.com/secao")
        self.assertEqual(Path(caminho).read_text(encoding="utf-8").strip(), "Texto de teste")

    def test_links_disponiveis(self):
        self.cadastro.adicionar("www.exemplo.com/um", "Um")
        self.cadastro.adicionar("www.exemplo.com/dois", "Dois")
        self.assertEqual(
            self.cadastro.obter_links("www.exemplo.com"),
            ["/dois", "/um"]
        )

    def test_terceiro_link_e_rejeitado(self):
        self.cadastro.adicionar("www.exemplo.com/um", "Um")
        self.cadastro.adicionar("www.exemplo.com/dois", "Dois")
        with self.assertRaises(ValueError):
            self.cadastro.adicionar("www.exemplo.com/tres", "Três")

    def test_caminho_com_acento(self):
        pagina = self.cadastro.adicionar("www.exemplo.com/coordenação", "Coordenação")
        self.assertEqual(pagina, "www.exemplo.com/coordenação")
        self.assertTrue(self.cadastro.esta_cadastrada(pagina))

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
