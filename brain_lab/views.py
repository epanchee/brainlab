# coding:utf-8

import datetime

from dal import autocomplete
from django.db.models import F
from django.shortcuts import render_to_response
from django.template import RequestContext

from brain_lab.models import Visitor


class VisitorAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated():
            return Visitor.objects.none()

        qs = Visitor.objects.all()

        if self.q:
            qs = qs.filter(ChildName__icontains=self.q)

        return qs


def time_to_servey(request):
    request_context = RequestContext(request)

    visitors = []
    print(Visitor.objects.filter(VisitorID=9)[0].CorrectedBirthDate)
    print(Visitor.objects.filter(VisitorID=9)[0].CorrectedBirthDate + datetime.timedelta(3 * 30))
    print(Visitor.objects.filter(VisitorID=9)[0].LastVisit)
    for months in [3, 5, 10, 14, 24, 36]:
        current = []
        interval = {'start': datetime.datetime.now() - datetime.timedelta(months * 30),
                    'end': datetime.datetime.now() - datetime.timedelta(months * 30 - 20)}

        # TODO: разбраться до конца с фильтром
        current = Visitor.objects \
            .filter(CorrectedBirthDate__gte=interval['start']) \
            .filter(CorrectedBirthDate__lte=interval['end']) \
            .filter(LastVisit__lt=F('CorrectedBirthDate') + datetime.timedelta(months * 30))

        visitors.extend(current)

    request_context.push({"visitors": visitors})
    return render_to_response("admin/time_to_servey.html", locals(),
                              context_instance=request_context)
