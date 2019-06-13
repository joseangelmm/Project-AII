from haystack.forms import SearchForm
class NoticiasSearchForm(SearchForm):

    def no_query_found(self):
        return self.searchqueryset.all()