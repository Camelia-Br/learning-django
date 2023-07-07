from django.dispatch import Signal

review_added = Signal(
    providing_args=[
        'provider',
    ]
)
