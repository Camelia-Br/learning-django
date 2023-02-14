from django.db.models.signals import post_save
from django.dispatch import receiver
from customers.models import Person, Provider
from .scoring import recalculate_ratings_score, recalculate_sitter_score, recalculate_overall_rank
from stays.models import Review

@receiver(post_save, sender=Person)
def update_search_score(sender, instance, **kwargs):
    dirty_name = instance.get_dirty_fields()
    if(hasattr(instance, 'provider')) and (dirty_name and 'name' in dirty_name):
        recalculate_sitter_score(instance)
        recalculate_overall_rank(instance)


@receiver(post_save, sender=Review)
def update_search_score(sender, instance, **kwargs):
    print('Salut', instance.get_dirty_fields())

    # if(hasattr(instance, 'provider')):
    #     provider = Provider.objects.get(person=instance)
    #     stays = provider.stays.all()
    #     reviewed_stays = 0
    #     rating_sum = 0

    #     for stay in stays:
    #         if(hasattr(stay, 'review')):
    #             print('yass')
    # recalculate_ratings_score(instance)
    # recalculate_overall_rank(instance)
    # print('instance', instance)