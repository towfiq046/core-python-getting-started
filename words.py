import sys
from urllib.request import urlopen


# def is a statement, top-level functions are defined when a module is imported or run.
def fetch_words(url):
    """
    Fetch a list of words from a URL.

    :param url: The URL of a UTF-8 text document.
    :return: A list of strings from the document.
    """
    story = urlopen(url)
    story_words = []

    for line in story:
        line_words = line.decode('utf-8').split()
        for word in line_words:
            story_words.append(word)
    story.close()
    return story_words


def print_items(items):
    """
    Print items one per line.

    :param items: A list of strings from the document.
    """
    for item in items:
        print(item)


def main(url):
    """
    Print each word from a text document fetched from a URL.

    :param url: The URL of a UTF-8 document.
    """
    print_items(fetch_words(url))


# __name__ detects whether a module runs as a script or imported into another module.
if __name__ == '__main__':
    main(sys.argv[1])   # The 0th arg is module filename.
