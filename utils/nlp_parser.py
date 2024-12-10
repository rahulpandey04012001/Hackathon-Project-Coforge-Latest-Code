import spacy

# Load SpaCy English model
nlp = spacy.load("en_core_web_sm")

def parse_user_story(user_story):
    """
    Parse a user story using SpaCy to extract important elements.

    Args:
        user_story (str): The user story to parse.

    Returns:
        dict: A dictionary of parsed elements such as roles, actions, and outcomes.
    """
    doc = nlp(user_story)
    parsed_data = {
        "entities": [(ent.text, ent.label_) for ent in doc.ents],
        "nouns": [chunk.text for chunk in doc.noun_chunks],
        "verbs": [token.lemma_ for token in doc if token.pos_ == "VERB"]
    }
    return parsed_data
