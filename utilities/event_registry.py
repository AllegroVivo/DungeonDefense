################################################################################
# This dictionary denotes all subscribers to all registered events. The comment
# column provided next to the initial dictionary key provides the signature of
# that event, for convenience.
################################################################################
EVENT_REGISTRY = {
    "after_attack" : [  # [None]
        DMStatus
    ],
    "battle_end" : [  # [None]
        LifePotion, RegenerationOrb
    ],
    "battle_exp_assigned" : [  # [ExperienceContext]
        TokenOfFriendship
    ],
    "battle_start" : [  # [None]
        IronPlate, LesserManaStone
    ],
    "before_attack" : [  # [None]
        Poison,
    ],
    "boss_room_entered" : [  # [DMUnit]
        CurseOfTheSkull
    ],
    "boss_skill_bite" : [  # [BossSkillContext]
        VampiricMonster, DemonTooth
    ],
    "boss_skill_blood_lord" : [  # [BossSkillContext]
        BloodStaff, BloodyMeteorite
    ],
    "boss_skill_forbidden_love" : [  # [BossSkillContext]
        DemonicWater
    ],
    "boss_skill_petrifying_gaze": [  # [BossSkillContext]
        ObsidianFang,
    ],
    "boss_skill_vampiric_impulse": [  # [BossSkillContext]
        BatControl
    ],
    "boss_skill_vampiric_infection": [  # [BossSkillContext]
        InfectedBlood,
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
    "experience_awarded" : [  # [ExperienceContext]
        ConstructionMaterial
    ],
    "on_death" : [  # [AttackContext]
        GhostAmulet, LifePotion, UndeadGrip, ElectricalShort, Spore, DeathGrip,
        LittleCoin, ManaRecoveryRune, SecondHeart
    ],
    "reset_stats" : [  # [Optional[DMUnit]]
        DMUnit
    ],
    "room_enter" : [  # [DMUnit]
        BattleDrums,
    ],
    "room_exit" : [  # [DMUnit][DMRoom]
        DragonKingsBelt
    ],
    "status_acquired" : [  # [DMStatus]
        Regeneration, Despair
    ],
    "status_execute" : [  # [DMStatus]
        AbyssThorn, Net, RingOfDefense, RingOfWeakness, RuneOfVulnerability
    ],
    "trap_activated" : [  # [AttackContext] (maybe?)
        InsigniaOfTerror
    ]
}
################################################################################
