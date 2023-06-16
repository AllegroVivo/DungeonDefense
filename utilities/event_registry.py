################################################################################
# This dictionary denotes all subscribers to all registered events. The comment
# column provided next to the initial dictionary key provides the signature of
# that event, for convenience.
################################################################################
EVENT_REGISTRY = {
    "battle_end" : [  # [None]
        LifePotion, RegenerationOrb
    ],
    "battle_exp_assigned" : [  # [ExperienceContext]
        TokenOfFriendship
    ],
    "battle_start" : [  # [None]
        IronPlate,
    ],
    "before_attack" : [  # [None]
        Poison,
    ],
    "boss_room_entered" : [  # [DMUnit]
        CurseOfTheSkull
    ],
    "boss_skill_bite" : [  # [BossSkillContext]
        VampiricMonster
    ],
    "boss_skill_blood_lord" : [  # [BossSkillContext]
        BloodStaff, BloodyMeteorite
    ],
    "boss_skill_venom_fang" : [  # [BossSkillContext]
        DeadlySting
    ],
    "burn_activated" : [  # [???]
        CateyeStone
    ],
    "dull_applied" : [  # [DMStatus]
        Hammer
    ],
    "egg_hatch" : [  # [EggHatchContext]
        AdvancedIncubator
    ],
    "on_death" : [  # [AttackContext]
        GhostAmulet, LifePotion, UndeadGrip, ElectricalShort, Spore
    ],
    "reset_stats" : [  # [Optional[DMUnit]]
        DMUnit
    ],
    "status_acquired" : [  # [DMStatus]
        Regeneration, Despair
    ],
    "trap_activated" : [  # [AttackContext] (maybe?)
        InsigniaOfTerror
    ]
}
################################################################################
