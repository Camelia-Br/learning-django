from django.dispatch import Signal


person_name_changed = Signal(
    providing_args=[
        'person',
    ]
)

provider_created = Signal(
    providing_args=[
        'provider',
    ]
)
