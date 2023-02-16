'''
HYPERION DEV BOOTCAMP TASK

Requires spacy and english language model installed via 2 commands:
pip3 install spacy
python -m spacy download en_core_web_md
'''
import spacy

def watch_next(desc: str) -> str:
    """Compares given description against movies in list and returns most similar movie title
    
    Uses the spacy vector model (loaded as global variable 'nlp') and compares the given description
    to each of the movies in the 'movies' global variable dictionary using .similiarity().
    Returns the best match.

    Args:
        desc: A string containing the description of the previously watched movie
    
    Returns:
        A string containing the name of the most similar movie to given description
    """
    doc = nlp(desc)
    highest_match = None

    for title, nlp_desc in movies.items():
        comparison = doc.similarity(nlp_desc)
        if highest_match == None or comparison > highest_match[1]:
            highest_match = [title, comparison]

    return highest_match[0]

nlp = spacy.load('en_core_web_md')
# Dictionary where key = movie name and value = language processed movie description
movies = {}

try:
    with open('movies.txt', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            line_split = line.split(' :', 1)
            movies[line_split[0]] = nlp(line_split[1])
except FileNotFoundError:
    print('Unable to find movies.txt')
    exit()

print(watch_next('''Will he save
their world or destroy it? When the Hulk becomes too dangerous for the
Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
planet where the Hulk can live in peace. Unfortunately, Hulk land on the
planet Sakaar where he is sold into slavery and trained as a gladiator.'''))