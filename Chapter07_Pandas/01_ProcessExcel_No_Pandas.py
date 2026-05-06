######################
#  Plain Python
#
#
##################
import csv


def calculate_rating_stats(data, industry=None):
    ratings = []

    for row in data:
        rating = row[3].strip()  # remove spaces

        if rating and rating != 'NULL' and (not industry or row[1] == industry):
            try:
                ratings.append(float(rating))
            except ValueError:
                continue  # skip bad data

    if not ratings:
        return None, None, None

    max_rating = max(ratings)
    min_rating = min(ratings)
    avg_rating = sum(ratings) / len(ratings)

    return max_rating, min_rating, avg_rating



with open("movies.csv") as f:
    data = list(csv.reader(f))
    header = data[0]
    data = data[1:]

max_rating, min_rating, avg_rating = calculate_rating_stats(data)
print(f"All records: Min rating = {min_rating}, Max rating = {max_rating}, Avg rating = {avg_rating}")

max_rating, min_rating, avg_rating = calculate_rating_stats(data, industry="Bollywood")
print(f"Bollywood: Min rating = {min_rating}, Max rating = {max_rating}, Avg rating = {avg_rating}")

max_rating, min_rating, avg_rating = calculate_rating_stats(data, industry="Hollywood")
print(f"Hollywood: Min rating = {min_rating}, Max rating = {max_rating}, Avg rating = {avg_rating}")