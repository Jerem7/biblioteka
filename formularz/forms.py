from django import forms


class SearchForm(forms.Form):
    search_phrase = forms.CharField(label='Fraza do wyszukania', max_length=255)
    search_by_choices = [
        ('id_ksiazki', 'ID Książki'),
        ('tytul', 'Tytuł'),
        ('id_autor__imie_autor', 'Imię autora'),
        ('id_autor__nazwisko_autor', 'Nazwisko autora'),
        ('id_wydawnictwa__nazwa', 'Wydawnictwo'),
        ('id_autor__kraj_pochodzenia', 'Kraj pochodzenia autora'),
    ]
    search_by = forms.ChoiceField(label='Szukaj według', choices=search_by_choices)
    additional_search = forms.BooleanField(label='Dodatkowy warunek wyszukiwania', required=False, initial=False)


class AdditionalSearchForm(forms.Form):
    additional_search_phrase = forms.CharField(label='Dodatkowa fraza do wyszukania', max_length=255, required=False)
    additional_search_by_choices = [
        ('id_ksiazki', 'ID Książki'),
        ('tytul', 'Tytuł'),
        ('id_autor__imie_autor', 'Imię autora'),
        ('id_autor__nazwisko_autor', 'Nazwisko autora'),
        ('id_wydawnictwa__nazwa', 'Wydawnictwo'),
        ('id_autor__kraj_pochodzenia', 'Kraj pochodzenia autora'),
    ]
    additional_search_by = forms.ChoiceField(label='Szukaj według', choices=additional_search_by_choices,
                                             required=False)
