from django.db import models


# Create your models here.

class Karta(models.Model):
    id_karty_bibl = models.AutoField(primary_key=True)
    imie = models.CharField(max_length=255)
    nazwisko = models.CharField(max_length=255)
    pesel = models.CharField(max_length=11)

    class Meta:
        db_table = 'dane_karty_i_posiadacza'


class Autor(models.Model):
    id_autor = models.AutoField(primary_key=True)
    imie_autor = models.CharField(max_length=255)
    nazwisko_autor = models.CharField(max_length=255)
    kraj_pochodzenia = models.CharField(max_length=255)

    class Meta:
        db_table = 'autorzy'


class DaneAdresowe(models.Model):
    id_karty_bibl = models.OneToOneField(Karta, primary_key=True, on_delete=models.CASCADE)
    ulica = models.CharField(max_length=255)
    numer_budynku = models.IntegerField()
    numer_lokalu = models.IntegerField()
    kod_pocztowy = models.CharField(max_length=9)
    miejscowosc = models.CharField(max_length=255)

    class Meta:
        db_table = 'dane_adresowe'


class Wydawnictwa(models.Model):
    id_wydawnictwa = models.AutoField(primary_key=True)
    nazwa = models.CharField(max_length=255)
    rok_zalozenia = models.IntegerField()
    kraj = models.CharField(max_length=255)

    class Meta:
        db_table = 'wydawnictwa'


class Kategorie(models.Model):
    id_kategorii = models.AutoField(primary_key=True)
    nazwa_kategorii = models.CharField(max_length=255)
    czy_mozna_wypozyczyc = models.BooleanField()

    class Meta:
        db_table = 'kategorie'


class Ksiazka(models.Model):
    id_ksiazki = models.AutoField(primary_key=True)
    tytul = models.CharField(max_length=255)
    nr_wydania = models.IntegerField()
    dostepnych = models.IntegerField()
    wypozyczonych = models.IntegerField()
    id_autor = models.ForeignKey(Autor, on_delete=models.SET_DEFAULT, default="brak autora")
    id_wydawnictwa = models.ForeignKey(Wydawnictwa, on_delete=models.SET_DEFAULT, default="brak wydawnictwa")
    id_kategorii = models.ForeignKey(Kategorie, on_delete=models.SET_DEFAULT, default="brak kategorii")

    class Meta:
        db_table = 'dane_ksiazek'


class Pracownicy(models.Model):
    id_pracownika = models.AutoField(primary_key=True)
    nazwisko = models.CharField(max_length=255)
    imie = models.CharField(max_length=255)
    data_zatrudnienia = models.DateField()
    stanowisko = models.CharField(max_length=255)

    class Meta:
        db_table = 'pracownicy'


class Wypozyczenia(models.Model):
    id_wypozyczenia = models.AutoField(primary_key=True)
    id_karty_bibl = models.ForeignKey(Karta, on_delete=models.SET_DEFAULT, default="brak numeru karty")
    id_ksiazki = models.ForeignKey(Ksiazka, on_delete=models.SET_DEFAULT, default="brak ksiazki")
    id_pracownika = models.ForeignKey(Pracownicy, on_delete=models.SET_DEFAULT, default="brak pracownika")
    data_wypozyczenia = models.DateField()
    data_zwrotu = models.DateField()
    czy_zwrocona = models.BooleanField()
    czy_po_terminie = models.BooleanField()

    class Meta:
        db_table = 'dane_wypozyczen'


class Rezerwacje(models.Model):
    id_rezerwacji = models.AutoField(primary_key=True)
    id_ksiazki = models.ForeignKey(Ksiazka, on_delete=models.SET_DEFAULT, default="brak ksiazki")
    id_karty_bibl = models.ForeignKey(Karta, on_delete=models.SET_DEFAULT, default="brak numeru karty")
    data_rezerwacji = models.DateField()
    czy_wypozyczono = models.BooleanField()
    data_wypozyczenia_lub_anulacji = models.DateField()

    class Meta:
        db_table = 'rezerwacje'

    class StatystykiWypozyczen(models.Model):
        id_karty_bibl = models.ForeignKey(Karta, on_delete=models.SET_DEFAULT, default="brak numeru karty")
        ilosc_wypozyczonych = models.IntegerField()
        ilosc_oddanych = models.IntegerField()
        ilosc_przetrzymanych = models.IntegerField()
        zaleglosc_za_przetrzymanie = models.IntegerField()

        class Meta:
            db_table = 'statystyki_wypozyczen'
