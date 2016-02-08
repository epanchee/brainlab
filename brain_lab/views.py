from dal import autocomplete

from brain_lab.models import Visitor


class VisitorAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return Visitor.objects.none()

        qs = Visitor.objects.all()

        self.q = self.q.encode('utf-8')
        print(self.q)

        if self.q:
            qs = qs.filter(ChildName__istartswith=self.q)

        return qs
