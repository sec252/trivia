from difflib import SequenceMatcher

PASSING = 70


def isCorrect(answer, response, passing=PASSING):
    """Function that returns the percentage of similarity
    between two strings

    Args:
      answer (string): Answer of a trivia question
      response (string): response of a user
      passing (int, optional): passing grade. Defaults to PASSING.

    Returns:
      Boolean: True or False
    """
    a = answer.lower().replace(" ", "")
    r = response.lower().replace(" ", "")

    perc = round(SequenceMatcher(None, a, r).ratio() * 100)

    return perc > passing
