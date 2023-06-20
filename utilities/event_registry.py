################################################################################
# This dictionary denotes all subscribers to all registered events. The comment
# column provided next to the initial dictionary key provides the signature of
# that event, for convenience.
################################################################################
EVENT_REGISTRY = {
    "after_attack" : [  # [None]
        DMStatus, BloomingBud
    ],
    "battle_end" : [  # [None]
        LifePotion, RegenerationOrb, ManaConverter, ElderDragon, Return,

    ],
    "battle_start" : [  # [None]
        IronPlate, LesserManaStone, BloodyCloth, CubeFromOtherworld, DemonicLamp,
        ElixirOfImmortality, ManaCollector, ManaStone, VoodooMask, PioneersEye,
        Graveyard, TreeOfLife, IronWall, SapplingOfYggdrasil,
    ],
    "before_attack" : [  # [None]
        Poison,
    ],
    "book_acquired" : [  # [DMBook]
        MysteriousQuill
    ],
    "book_read" : [  # [DMBook]
        RingOfEnlightenment, SagesBrush,
    ],
    "boss_room_entered" : [  # [DMUnit]
        CurseOfTheSkull
    ],
    "boss_skill_bite" : [  # [BossSkillContext]
        VampiricMonster, DevilsTooth,
    ],
    "boss_skill_blood_lord" : [  # [BossSkillContext]
        BloodStaff, BloodyMeteorite
    ],
    "boss_skill_forbidden_love" : [  # [BossSkillContext]
        DemonicWater
    ],
    "boss_skill_frost_arrow" : [  # [BossSkillContext]
        ConchShell,
    ],
    "boss_skill_harvest" : [  # [BossSkillContext]
        DemonsScale,
    ],
    "boss_skill_hemokinesis" : [  # [BossSkillContext]
        BloodyHourglass,
    ],
    "boss_skill_petrifying_gaze": [  # [BossSkillContext]
        ObsidianFang,
    ],
    "boss_skill_rallying_cry" : [  # [BossSkillContext]
        DeliciousMilk
    ],
    "boss_skill_split" : [  # [BossSkillContext]
        EmmasTailAccessory
    ],
    "boss_skill_used" : [  # [BossSkillContext]
        VampireAxe, VampireRing, FairyWings,
    ],
    "boss_skill_vampiric_impulse": [  # [BossSkillContext]
        BatControl, VampireRune
    ],
    "boss_skill_vampiric_infection": [  # [BossSkillContext]
        InfectedBlood,
    ],
    "boss_skill_venom_fang" : [  # [BossSkillContext]
        DeadlySting
    ],
    "boss_skill_venom_whip" : [  # [BossSkillContext]
        DemonGlove,
    ],
    "burn_activated" : [  # [???]
        CateyeStone
    ],
    "corruption_start" : [  # [???]
        TheOriginOfTheFall, BlackMask,
    ],
    "day_advance" : [  # [DMDay]
        AncientEgg, ElderDragon, StatueOfSealedRage,
    ],
    "dull_applied" : [  # [DMStatus]
        Hammer
    ],
    "dungeon_fate" : [  # [None]
        StaffOfReign,
    ],
    "egg_hatch" : [  # [EggHatchContext]
        AdvancedIncubator, Biography, Hatchery,
    ],
    "experience_awarded" : [  # [ExperienceContext]
        ConstructionMaterial, MagicalSoil, WarriorsBlood, TokenOfFriendship,
        CursedAmberStone, CrackedAmberStone, PerfectAmberStone,
        ReapersSoulFragment,
    ],
    "gold_acquired" : [  # [GoldAcquiredContext]
        BottomlessWallet,
    ],
    "hero_spawn" : [  # [DMHero]
        BlueCoralReef, Monocle, RustyBlade, AmethystChoker, Greenstone,
        AncientEgg, CorruptedDragon,
    ],
    "on_death" : [  # [AttackContext]
        GhostAmulet, LifePotion, UndeadGrip, ElectricalShort, Spore,
        DeathGrip, LittleCoin, ManaRecoveryRune, SecondHeart, CorpseFlower,
        Scorpion, DemonicFruit, TeardrinkerSword, MarkOfShadow,
        ShiningMarkOfShadow, StigmaOfAsceticism, FirstMarkOfAsceticism,
        SecondMarkOfAsceticism, ThirdMarkOfAsceticism, LastMarkOfAsceticism,
        Sacrifice, Scream, Prism, Dynamite,
    ],
    "on_heal" : [  # [HealingContext]
        Cake
    ],
    "on_purchase" : [  # [PurchaseContext]
        AncientCoin, PremiumMembershipCert,
    ],
    "reset_stats" : [  # [Optional[DMUnit]]
        DMUnit, DMRelicManager
    ],
    "room_enter" : [  # [DMUnit]
        BattleDrums, TurbanOfCharm, DMTrapRoom, Betrayal, DMChargeable,
        Bloodthirst, Pressure, Haste, MirrorRoom, ShieldOfSteel, Gunpowder,
        BloodPool, TreeOfLife, BiggerFight, Prism, IronWall, IronCurtain,
        SteelThorn, InfinityClock
    ],
    "room_exit" : [  # [DMUnit][DMRoom]
        DragonKingsBelt
    ],
    "status_acquired" : [  # [DMStatus]
        Regeneration, Despair, PearlShell, DarkCube, AcceleratingWatch,
        CursedPocketWatch,
    ],
    "status_execute" : [  # [DMStatus]
        AbyssThorn, Net, RingOfDefense, RingOfWeakness, RuneOfVulnerability,
        GiantThorn, SmokedMeat, WoodenStaff, Rafflesia, Thunderbolt,
        FullMoonNecklace, HalfMoonNecklace, CrescentNecklace, StickyNet,
        LittleSwampMonster, DeathMist

    ],
    "soul_acquired" : [  # [SoulAcquiredContext]
        CorruptedAncientEgg,
    ],
    "trap_activated" : [  # [AttackContext] (maybe?)
        InsigniaOfTerror
    ]
}
################################################################################
