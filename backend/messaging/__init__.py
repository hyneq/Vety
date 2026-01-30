"""
A subpackage for support of messages.

A message from the player to the game is called an intent,
whereas a message from the game to one or more players is called an event.
"""

from .protocols import Intent, IntentHandler
from .protocols import Event, EventNotifier
