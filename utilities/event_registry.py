################################################################################
# This dictionary of lists denotes all subscribers to all registered events.
# The comment column provided next to the initial dictionary key provides
# the signature for that event and the associated preset method, for convenience.
################################################################################
EVENT_REGISTRY = {
    "on_attack" : [  # [AttackContext: "ctx"] (handle())
        Acceleration
    ],
    "recalculate_stats" : [  # [Optional[DMUnit]: "unit"] (stat_calc())
        Acceleration
    ],
    "reset_stats" : [  # [Optional[DMUnit]: "unit"]
        DMUnit
    ],
}
################################################################################
