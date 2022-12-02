"""Moduuli varastojen luomiseen ja muokkaamiseen."""
class Varasto:
    """Varaston alustaminen."""
    def __init__(self, tilavuus, alku_saldo = 0):
        self.tilavuus = 0.0
        if tilavuus > 0.0:
            self.tilavuus = tilavuus

        if alku_saldo < 0.0:
            # virheellinen, nollataan
            self.saldo = 0.0
        elif alku_saldo <= tilavuus:
            # mahtuu
            self.saldo = alku_saldo
        else:
            # täyteen ja ylimäärä hukkaan!
            self.saldo = tilavuus
        #print("moti")
        #print("moti")
        #print("moti")
        #print("moti")
        #print("moti")
        #print("moti")
        #print("moti")
        #print("moti")
        #print("moti")

    # huom: ominaisuus voidaan myös laskea.
    def paljonko_mahtuu(self):
        """Funktio, jolla tarkistetaan paljonko varastossa on vielä tilaa."""
        return self.tilavuus - self.saldo

    def lisaa_varastoon(self, maara):
        """Funktio, jolla lisätään tietty määrä varastoon."""
        if maara < 0:
            return
        if maara <= self.paljonko_mahtuu():
            self.saldo = self.saldo + maara
        else:
            self.saldo = self.tilavuus

    def ota_varastosta(self, maara):#, moti1 = 0, moti2 = 0, moti3 = 0):
        """Funktio, jolla otetaan tietty määrä varastosta"""
        if maara < 0:
            return 0.0
        if maara > self.saldo:
            kaikki_mita_voidaan = self.saldo
            self.saldo = 0.0

            return kaikki_mita_voidaan

        self.saldo = self.saldo - maara
        #if maara < 0:
        #    if self.saldo < 0:
        #        if self.tilavuus < 0:
        #            print("motivaatio")
        return maara

    def __str__(self):
        """Funktio, jolla tulostetaan varaston saldo ja jäljellä oleva tila."""
        return f"saldo = {self.saldo}, vielä tilaa {self.paljonko_mahtuu()}"
