from stays.models import Stay, Review
from customers.models import Provider
from django.db.models import Avg

def recalculate_sitter_score(instance):
    provider = Provider.objects.get(person=instance)
    distinct_letters = len(set(provider.person.name))
    sitter_score = (5 * distinct_letters)/26
      
    print('lala',sitter_score)

def recalculate_ratings_score(instance):
    provider = Provider.objects.get(person=instance)
    stays = provider.stays.all()
    reviewed_stays = 0
    rating_sum = 0

    for stay in stays:
      if(hasattr(stay, 'review')):
        reviewed_stays +=1
        rating_sum += stay.review.rating
        rating_score = rating_sum/reviewed_stays

    print('hihi',rating_score)
    
def recalculate_overall_rank(instance):
    provider = Provider.objects.get(person=instance)
    stays = provider.stays.all()
    stays_count = stays.count()
    sitter_score = recalculate_sitter_score(instance)
    rating_score =   recalculate_ratings_score(instance)
    print('ratingScore from overall', rating_score)
    print('sitterscore from overall', sitter_score)

    # if stays_count < 1:
    #    print('stays_count <1',sitter_score)
    # elif stays_count >10:
    #    print('stays_count >10', rating_score)
    # print('avvvvgggg',sitter_score + rating_score)/2

    
