import re
import random


class Generator:
    place = None
    adjective = None
    noun = None
    verb = None
    emotion = None

    def __init__(
        self, place: str, adjective: str, noun: str, verb: str, emotion: str
    ) -> None:
        """
        Initializes the Generator class with the given parameters.

        Args:
            place (str): A place.
            adjective (str): An adjective.
            noun (str): A noun.
            verb (str): A verb.
            emotion (str): An emotion.
        """
        self.place = place
        self.adjective = adjective
        self.noun = noun
        self.verb = verb
        self.emotion = emotion

    def generate(self) -> str:
        """
        Generates a sentence using the instance variables.

        Returns:
            str: A generated sentence.
        """
        with open(
            "../MadLibs-Generator/files/story_template.txt", "r", encoding="utf-8"
        ) as file:
            story_template = file.read()

        story_template = (
            story_template.splitlines()
        )  # spliting the lines so we can choose one from the array of lines
        story_template = random.choice(
            story_template
        )  # choosing one random item from the array of lines each represents one story template

        # Replacing placeholders in the story template with instance variables with regex
        story_template = re.sub(r"{place}", self.place, story_template)
        story_template = re.sub(r"{adjective}", self.adjective, story_template)
        story_template = re.sub(r"{noun}", self.noun, story_template)
        story_template = re.sub(r"{verb}", self.verb, story_template)
        story_template = re.sub(r"{emotion}", self.emotion, story_template)

        return story_template
