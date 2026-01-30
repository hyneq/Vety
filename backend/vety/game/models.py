"""
The game logic

TODO: Add description
"""

from typing import Sequence, Mapping, Set, Optional
from dataclasses import dataclass
from collections import deque

from . import exceptions


class Game:
    """
    A game in progress

    TODO: Add description
    """

    _players: Sequence["Player"]
    _questions: Sequence["Question"]
    _sentences: Mapping["Player", "Sentence"]
    _players_answered: Set["Player"]

    finished: bool = False
    _current_question_i = 0

    def __init__(self,
                 players: Sequence["Player"],
                 questions: Sequence["Question"]):

        self._players = players
        self._questions = questions

        self._sentences = {player: Sentence(questions) for player in players}

    
    @property
    def current_question(self) -> "Question":
        return self._questions[self._current_question_i]


    def _get_sentence_for_player(self, player: "Player") -> "Sentence":
        return self._sentences[player]
    

    def answer_current_question(self, player: "Player", element: str):
        self._get_sentence_for_player(player).answer(self.current_question, element)


    def proceed(self):
        if self.finished:
            raise exceptions.GameAlreadyFinishedException()

        if self._current_question_i == len(self._questions) - 1:
            self.finished = True
            return True

        self._current_question_i += 1
        self._rotate_sentences()

        return False


    def _rotate_sentences(self):
        values = deque(self._sentences.values())
        values.rotate(1)
        self.sentences = dict(zip(self.sentences.keys(), values))


    def get_results(self):
        if not self.finished:
            raise exceptions.GameNotFinishedYetException()

        return self._sentences


@dataclass
class Player:
    """
    A player participating in a Game

    Attributes:
        name: The nickname of the player
    """

    name: str


@dataclass
class Question:
    """
    A specification of a question when building a Sentence

    Attributes:
        name: The name of the question, as used internally in the game
        description: The question in human-friendly language
    """

    name: str
    description: str


class Sentence:
    """
    A single sentence in a game

    The sentence is determined by a mapping of questions to responses (elements)
    """


    elements: dict[Question,Optional[str]]

    def __init__(self, questions: Sequence[Question]):
        self.elements = {question: None for question in questions}


    def __str__(self) -> str:
        return " ".join(value for value in self.elements.values() if value)


    def answer(self, question: Question, element: str):
        """
        Sets the element as the response to question
        
        Arguments:
            question: the question to answer
            element: the response to the question
        """

        self.elements[question] = element
