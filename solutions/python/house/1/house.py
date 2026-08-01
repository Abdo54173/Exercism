PHRASES = [
    ("house that Jack built.", ""),
    ("malt", "lay in"),
    ("rat", "ate"),
    ("cat", "killed"),
    ("dog", "worried"),
    ("cow with the crumpled horn", "tossed"),
    ("maiden all forlorn", "milked"),
    ("man all tattered and torn", "kissed"),
    ("priest all shaven and shorn", "married"),
    ("rooster that crowed in the morn", "woke"),
    ("farmer sowing his corn", "kept"),
    ("horse and the hound and the horn", "belonged to"),
]


def recite(start_verse, end_verse):
    verses = []

    for verse in range(start_verse - 1, end_verse):
        sentence = f"This is the {PHRASES[verse][0]}"

        for i in range(verse, 0, -1):
            sentence += f" that {PHRASES[i][1]} the {PHRASES[i - 1][0]}"

        verses.append(sentence)

    return verses