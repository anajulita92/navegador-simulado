import unittest

from estrutura_web import EstruturaWeb


class TesteEstruturaWeb(unittest.TestCase):
    def setUp(self):
        self.estrutura = EstruturaWeb()

    def test_cadastro_e_busca_de_pagina(self):
        self.estrutura.cadastrar("www.exemplo.com", "home.txt")
        self.estrutura.cadastrar("www.exemplo.com/seção", "secao.txt")
        self.assertEqual(
            self.estrutura.obter_arquivo("www.exemplo.com/seção"),
            "secao.txt"
        )

    def test_pagina_inexistente(self):
        self.assertIsNone(self.estrutura.buscar("www.inexistente.com"))

    def test_limite_de_dois_links_por_pagina(self):
        self.estrutura.cadastrar("www.exemplo.com", "home.txt")
        self.estrutura.cadastrar("www.exemplo.com/a", "a.txt")
        self.estrutura.cadastrar("www.exemplo.com/b", "b.txt")
        with self.assertRaises(ValueError):
            self.estrutura.cadastrar("www.exemplo.com/c", "c.txt")

    def test_limite_independente_em_cada_pagina(self):
        self.estrutura.cadastrar("www.exemplo.com", "home.txt")
        self.estrutura.cadastrar("www.exemplo.com/a", "a.txt")
        self.estrutura.cadastrar("www.exemplo.com/b", "b.txt")
        self.estrutura.cadastrar("www.exemplo.com/a/um", "um.txt")
        self.estrutura.cadastrar("www.exemplo.com/a/dois", "dois.txt")
        self.assertEqual(
            self.estrutura.obter_links("www.exemplo.com/a"),
            ["/dois", "/um"]
        )


if __name__ == "__main__":
    unittest.main()
