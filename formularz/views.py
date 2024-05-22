from django.shortcuts import render
from .forms import SearchForm, AdditionalSearchForm
from .models import Ksiazka


def search_books(request):
    if request.method == 'GET':
        search_form = SearchForm(request.GET)
        additional_search_form = AdditionalSearchForm(request.GET)

        if search_form.is_valid() and additional_search_form.is_valid():
            search_phrase = search_form.cleaned_data['search_phrase']
            search_by = search_form.cleaned_data['search_by']
            additional_search = search_form.cleaned_data['additional_search']

            additional_search_phrase = additional_search_form.cleaned_data['additional_search_phrase']
            additional_search_by = additional_search_form.cleaned_data['additional_search_by']

            # Logika do filtrowania
            filter_params = {f'{search_by}__icontains': search_phrase}

            if additional_search:
                if additional_search_phrase and additional_search_by:
                    filter_params[f'{additional_search_by}__icontains'] = additional_search_phrase

            results = Ksiazka.objects.filter(**filter_params)

            return render(request, 'search_results.html', {'results': results})

    else:
        search_form = SearchForm()
        additional_search_form = AdditionalSearchForm()

    return render(request, 'search.html',
                  {'search_form': search_form, 'additional_search_form': additional_search_form})
