def compute_sitter_score(person):
    distinct_letters = len(set(person.name))
    sitter_score = (5 * float(distinct_letters)) / 26

    return sitter_score


def compute_ratings_score(provider):
    stays = provider.stays.all()
    reviewed_stays = 0
    rating_sum = 0

    for stay in stays:
        if hasattr(stay, 'review'):
            reviewed_stays += 1
            rating_sum += stay.review.rating
            rating_score = float(rating_sum) / float(reviewed_stays)

    return rating_score


def compute_overall_rank(provider, sitter_score, rating_score):
    stays = provider.stays.all()
    stays_count = stays.count()

    if stays_count < 1:
        return sitter_score
    elif stays_count > 10:
        return rating_score

    return (float(sitter_score) + float(rating_score)) / 2
