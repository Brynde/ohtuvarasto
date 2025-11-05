import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_lisaa_liikaa(self):
        self.varasto.lisaa_varastoon(11)

        # varastossa pitäisi olla tilaa 10-11 ja ylimääräiset heitetään pois eli 0
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 0)

    def test_lisaa_liian_vahan(self):
        self.varasto.lisaa_varastoon(-1)

        # varastossa pitäisi olla tilaa 10 sillä negatiiviset hylätään
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 10)

    def test_ota_pois_liikaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(9)

        # varastossa pitäisi olla tilaa 10 sillä liikaa ottaminen ottaa kaikki
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 10)

    def test_ota_pois_liian_vahan(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(-1)

        # varastossa pitäisi olla tilaa 2 sillä negatiiviset hylätään
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_varaston_tilavuus_liian_pieni(self):
        varasto = Varasto(-1)

        self.assertAlmostEqual(varasto.tilavuus, 0)
    
    def test_alku_saldo_liikaa(self):
        varasto = Varasto(10, -1)
    
        self.assertAlmostEqual(varasto.saldo, 1)

    def test_str_palauttaa_oikean_muodon(self):
        teksti = str(self.varasto)

        # varastossa pitäisi olla saldo = 0 ja tilaa 10
        self.assertEqual(teksti, "saldo = 0, vielä tilaa 10")
