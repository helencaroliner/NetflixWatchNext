import spacy

nlp = spacy.load('en_core_web_md')

description ='''Will he save their world or destroy it?
                    When the Hulk becomes too dagerous for the
                    Earth, the Illuminati trick Hulk into a
                    shuttle and launch him into a space to a planet
                    where the Hulk can live in peace. Unfornately,
                    Hulk land on the planet Sakaar where he is sold
                    into slavery and trained as a gladiator.'''

def similarMovie(description):
    planetHulk = nlp(description)
    max_similarity = 0
    most_similar_movie = ""

    with open ('movies.txt', 'r') as file:

        for line in file:
            # Split each line into title and description
            movie_title,movie_description = line.strip().split(":")
            # Create a spaCy object for the description
            movie_description = nlp(movie_description)
            # Calculate similarity between 'description' and current movie's description
            similarity = planetHulk.similarity(movie_description)

            # Update the most similar movie if the similarity score is higher
            if similarity > max_similarity:
                max_similarity = similarity
                most_similar_movie = movie_title
    return most_similar_movie

            
most_similar_movie = similarMovie(description)
print(most_similar_movie)




            

