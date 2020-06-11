import logging
from celery import shared_task
from django.core import management

logger = logging.getLogger(__name__)


@shared_task(name='mapserver.process_hazard_event_queue')
def process_hazard_event_queue():
    management.call_command(
        'process_hazard_event_queue'
    )
