from django.dispatch import Signal

game_completed = Signal(providing_args=['user_id'])
