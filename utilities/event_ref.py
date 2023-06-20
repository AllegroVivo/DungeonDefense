from typing     import List
################################################################################

__all__ = ("_EVENT_REFERENCE",)

################################################################################
# This list denotes all registered event names within the application.
# The comment column provides the argument signature expected by the callback
# subscribed to a given event.
# ===========================================================================
_EVENT_REFERENCE: List[str] = [
    # Battle-Related
    "after_attack",                 # [AttackContext]
    "after_battle",                 # [None]
    "attacking_boss",               # [BossAttackContext]
    "before_attack",                # [AttackContext]
    "before_battle",                # [None]
    "boss_room_entered",            # [DMFighter]
    "boss_skill_used",              # [BossSkillContext]
    "damage_applied",               # [DamageComponent]
    "hero_spawn",                   # [DMHero]
    "on_attack",                    # [AttackContext]
    "on_death",                     # [AttackContext]
    "healing_applied",              # [HealingContext]
    "room_enter",                   # [DMUnit]
    "on_room_exit",                 # [DMRoom][DMFighter]
    "trap_activation",              # [AttackContext]

    # Boss Skill-Related
    "boss_skill_blood_lord",        # [BossSkillContext]
    "boss_skill_bite",              # [BossSkillContext]
    "boss_skill_climax",            # [BossSkillContext]
    "boss_skill_forbidden_love",    # [BossSkillContext]
    "boss_skill_frost_arrow",       # [BossSkillContext]
    "boss_skill_fury_explosion",    # [BossSkillContext]
    "boss_skill_harvest",           # [BossSkillContext]
    "boss_skill_hemokinesis",       # [BossSkillContext]
    "boss_skill_infection",         # [BossSkillContext]
    "boss_skill_petrifying_gaze",   # [BossSkillContext]
    "boss_skill_rallying_cry",      # [BossSkillContext]
    "boss_skill_snake_trap",        # [BossSkillContext]
    "boss_skill_split",             # [BossSkillContext]
    "boss_skill_vampiric_impulse",  # [BossSkillContext]
    "boss_skill_venom_fang",        # [BossSkillContext]
    "boss_skill_whip",              # [BossSkillContext]

    # General Status-Related
    "status_acquired",              # [DMStatus][Optional[AttackContext]]
    "status_execute",               # [DMStatus]

    # Specific Status-Related
    "recovery_canceled_by_burn",    # [???]

    # Item Generation-Related
    "egg_hatch",                    # [EggHatchContext]
    "room_spawn",                   # [RoomSpawnContext]

    # Fate-Related
    "event_fate",                   # [DMEvent]
    "dungeon_fate",                 # [None]

    # Enhancement-Related
    "experience_awarded",           # [ExperienceContext]
    "room_enhance",                 # [ExperienceContext]

    # Inventory-Related
    "gold_acquired",                # [GoldSoulContext]
    "relic_acquired",               # [DMRelic]
    "soul_acquired",                # [GoldSoulContext]
    "book_acquired",                # [DMBook]
    "book_complete",                # [DMBook]
    "on_purchase",                  # [PurchaseContext]

    # Stats-Related
    "stat_calculation",             # [None]
    "reset_stats",                  # [None]

    # Dungeon-Related
    "day_advance",                  # [None]
    "room_placed",                  # [DMRoom]
    "room_removed",                 # [DMRoom]
    "room_swap",                    # [DMRoom]
]
################################################################################
