"""
Module containing generic message classes for communication from and to the game session.

A message from the player to the game session is called an intent.
An intent handler protocol specifies a callable that accepts an intent.

A message from the game session to the player is called an event.
An event handler protocol specifies a callable that accepts an event.
"""

from typing import Callable

class Intent:
    """
    A message from the player to the game controller
    """


IntentHandler = Callable[[Intent], None]


class Event:
    """
    A message from the game controller to the player
    """
    pass


EventNotifier = Callable[[Event], None]
"""
The protocol for sending events to clients
"""
