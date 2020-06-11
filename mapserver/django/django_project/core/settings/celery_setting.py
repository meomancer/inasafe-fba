CELERYBEAT_SCHEDULE = {
    'hazard_event_queue': {
        'task': 'mapserver.process_hazard_event_queue',
        'schedule': 60 * 1,  # every 1 minute
    },
}

CELERY_TIMEZONE = 'UTC'
