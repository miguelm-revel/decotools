import warnings
import random

SARCASM_MESSAGES = [
    "Oh, you’re still using *this* function? How vintage.",
    "This function is like a fax machine — impressive in the 80s.",
    "Bravo. You’ve discovered a relic from the past.",
    "Good luck! This function has seen things… horrible things.",
    "Are you sure? This function’s best days are behind it. Way behind.",
    "Calling this is like using Internet Explorer — you *can*, but should you?",
    "Welcome to the legacy zone. Hope you brought a time machine.",
    "Still works. Barely. Like your old Nokia.",
    "If bugs were awards, this function would have a full trophy case.",
    "Careful — archaeologists might want to study this function soon.",
    "Somewhere, a modern dev just cringed.",
    "This function was last updated when dinosaurs roamed the earth.",
    "Is this code or an ancient spellbook?",
    "Using this is a bold choice… for someone who hates stability.",
    "You're either brave or lost. Possibly both.",
    "Warning: this function might summon Clippy.",
    "Fun fact: this function once ran on Windows 95.",
    "Just because it works doesn’t mean it should be used.",
    "This was cool… until the Cold War ended.",
    "Why modernize when you can live dangerously?",
    "Deprecation is just a suggestion… right?",
    "Your linter cried a little when it saw this.",
    "Using this function increases your technical debt — and your cholesterol.",
    "Legend says this function was written during a coffee-fueled all-nighter.",
    "This function has more edge cases than a dodecahedron.",
    "Oh look, technical debt with a bow on it!",
    "Every time you call this, a unit test fails somewhere.",
    "It's not a bug, it's a feature! From 2003.",
    "You must really trust legacy code. Bold.",
    "This function should come with a warning label. Oh wait — now it does."
]

def deprecate(func):
    def wrapper(*args, **kwargs):
        message = random.choice(SARCASM_MESSAGES)
        warnings.warn(
            f"[DEPRECATED] {func.__name__}() -> {message}",
            category=DeprecationWarning,
            stacklevel=2
        )
        return func(*args, **kwargs)
    return wrapper
