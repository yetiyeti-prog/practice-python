import requests
from bs4 import BeautifulSoup

SOME_CLASS_TO_CHECK = "covid-tracker-wrapper"


def decode_a_webpage():
    base_url = 'http://www.nytimes.com'
    r = requests.get(base_url)
    soup = BeautifulSoup(r.text, features="html.parser")
    for story_heading in soup.find_all(class_=SOME_CLASS_TO_CHECK):
        if story_heading.a:
            print("StoryHeading Links --> " + story_heading.a.text.replace("\n", " ").strip())
        else:
            print("StoryHeading Texts --> " + story_heading.contents[0].strip())


if __name__ == '__main__':
    decode_a_webpage()
