import datetime
from django.core.management.base import BaseCommand, CommandError

from brain_lab.forms import NORMAL_GESTATION
from brain_lab.models import Visitor


class Command(BaseCommand):
    help = 'Runs save procedure all over the visitors'

    def handle(self, *args, **options):
        for visitor in Visitor.objects.all():
            try:
                if visitor.Gestination < 37:
                    visitor.CorrectedBirthDate = visitor.BirthDate + datetime.timedelta(
                        (NORMAL_GESTATION - visitor.Gestination) * 7)
                else:
                    visitor.CorrectedBirthDate = visitor.BirthDate

                visitor.save()
            except:
                raise CommandError('Something went wrong with %s' % visitor.ChildName)

            self.stdout.write(self.style.SUCCESS('Successfully saved visitor %d "%s"' % (visitor.VisitorID, visitor.ChildName)))
