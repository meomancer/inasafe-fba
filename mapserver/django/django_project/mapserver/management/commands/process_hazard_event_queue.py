__author__ = 'Irwan Fathurrahman <irwan@kartoza.com>'
__date__ = '11/06/20'

from django.core.management.base import BaseCommand
from django.db.models import Q
from mapserver.models.hazard_event import HazardEvent
from mapserver.models.hazard_event_queue import HazardEventQueue


class Command(BaseCommand):
    """ Command to process first hazard event queue. """

    def handle(self, *args, **options):
        queue = HazardEventQueue.objects.order_by('id').first()
        print('found {}'.format(queue))
        if queue and queue.queue_status != 1:
            # run the script
            queue.queue_status = 1
            queue.save()

            print('run {}'.format(queue.id))
            HazardEvent.objects.get_or_create(
                flood_map_id=queue.flood_map_id,
                acquisition_date=queue.acquisition_date,
                forecast_date=queue.forecast_date,
                source=queue.source,
                notes=queue.notes,
                link=queue.link,
                trigger_status=queue.trigger_status,
                progress=queue.progress,
                hazard_type_id=queue.hazard_type_id
            )
            print('done {}'.format(queue.id))
            queue.delete()
        else:
            print('skip')
