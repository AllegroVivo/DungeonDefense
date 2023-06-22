################################################################################
# This dictionary isn't intended for use within the application, and is merely
# informational. It denotes all subscribers to all registered events.
################################################################################
EVENT_REGISTER = {
    "boss_skill_blood_lord": [  # -> BossSkillContext
        BloodStaff, BloodyMeteorite,
    ],
    "egg_hatch": [  # -> EggHatchContext
        AdvancedIncubator,
    ],
    "on_target_acquire": [  # -> TargetingContext
        AbyssLamp,
    ],
    "stat_refresh": [  # -> None
        DMRelic,
    ],
}
################################################################################
