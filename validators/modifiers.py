"""Modifiers on a bill line, and whether they explain a repeat."""

import json

import config


def modifiers_of(item: dict) -> set[str]:
    """The line's modifiers as a set. They arrive as a list from a scan and as JSON text from the database."""
    value = item.get("modifiers")
    if isinstance(value, str):
        try:
            value = json.loads(value)
        except json.JSONDecodeError:
            value = []
    return {str(m).upper() for m in value or []}


def is_lab_code(code: str | None) -> bool:
    return bool(code) and code.isdigit() and len(code) == 5 and config.ER_LAB_RANGE[0] <= int(code) <= config.ER_LAB_RANGE[1]


def explains_repeat(first: dict, second: dict) -> bool:
    """True when the modifiers show the two lines are legitimately different: a repeat test (91), a repeat procedure
    (76/77), different sides, bilateral (50), a facility versus doctor's reading (26/TC) or a distinct service."""
    a, b = modifiers_of(first), modifiers_of(second)
    if (a | b) & (config.REPEAT_MODIFIERS | config.DISTINCT_SERVICE_MODIFIERS):
        return True
    if a & config.SIDE_MODIFIERS and b & config.SIDE_MODIFIERS and (a & config.SIDE_MODIFIERS) != (b & config.SIDE_MODIFIERS):
        return True
    return bool(a & config.COMPONENT_MODIFIERS and b & config.COMPONENT_MODIFIERS and (a & config.COMPONENT_MODIFIERS) != (b & config.COMPONENT_MODIFIERS))


def commonly_repeated(code: str | None) -> bool:
    return is_lab_code(code) or code in config.COMMONLY_REPEATED_CODES
