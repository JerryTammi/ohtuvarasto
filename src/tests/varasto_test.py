import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)
        self.virhevarasto = Varasto(-5, alku_saldo=-10)
        self.motivarasto = Varasto(5, alku_saldo=10)

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

    def test_yritetaan_laittaa_liikaa(self):
        self.varasto.lisaa_varastoon(1000)

        # varasto saldo pitäisi olla 10 (maksimi)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_yritetaan_ottaa_liikaa(self):
        self.varasto.ota_varastosta(1000)

        # varaston saldo pitäisi olla 0
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_lisataan_negatiivinen_maara(self):
        self.varasto.lisaa_varastoon(-1000)

        #varaston saldo pitäisi olla sama kuin ennen
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_otetaan_negatiivinen_maara(self):
        self.varasto.ota_varastosta(-1000)

        #varaston saldo pitäisi olla sama kuin ennen
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_saldon_tulostus(self):
        self.varasto.lisaa_varastoon(8)

        # tulostaminen toimii oikein
        self.assertAlmostEqual(self.varasto.__str__(), "saldo = 8, vielä tilaa 2")

    def test_virheellinen_tilavuus_alussa(self):
        self.assertAlmostEqual(self.virhevarasto.tilavuus, 0)

    def test_virheellinen_alku_saldo(self):
        self.assertAlmostEqual(self.virhevarasto.saldo, 0)

    def test_alku_saldo_pienempi_kuin_tilavuus(self):
        self.assertAlmostEqual(self.virhevarasto.saldo, self.virhevarasto.tilavuus)
    
    def test_alku_saldo_suurempi_kuin_tilavuus(self):
        self.assertAlmostEqual(self.motivarasto.saldo, self.motivarasto.tilavuus)