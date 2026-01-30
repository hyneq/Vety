"""
Helper module containing a generic intent router
"""

from .protocols import Intent, IntentHandler

class IntentRouter:
    """
    Routes intents to the correct handlers
    """

    _routes: dict[type[Intent], IntentHandler]
    
    def __init__(self, routes: dict[type[Intent], IntentHandler]):
        self._routes = routes

    def _get_handler(self, intent: Intent):
        for intent_type, handler in self._routes.items():
            if isinstance(intent, intent_type):
                return handler

        raise ValueError("Unknown intent")


    def __call__(self, intent: Intent):
        return self._get_handler(intent)(intent)
