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
    "after_attack",                 # [AttackContext: "ctx"]
    "after_battle",                 # [None]
    "attacking_boss",               # [BossAttackContext: "ctx"]
    "before_attack",                # [AttackContext: "ctx"]
    "before_battle",                # [AttackContext: "ctx"]  # Do I need the ctx here?
    "boss_room_entered",            # [DMFighter: "unit"]
    "boss_skill_used",              # [BossSkillContext: "ctx"]
    "damage_applied",               # [DamageComponent: "damage"]
    "hero_spawn",                   # [DMHero: "hero"]
    "on_attack",                    # [AttackContext: "ctx"]
    "on_death",                     # [AttackContext: "ctx"]
    "on_heal",                      # [HealingContext: "ctx"]
    "on_room_enter",                # [DMRoom: "room"][DMFighter: "unit"]
    "on_room_exit",                 # [DMRoom: "room"][DMFighter: "unit"]
    "trap_activation",              # [AttackContext: "ctx"]

    # Boss Skill-Related
    "boss_skill_blood_lord",        # [BossSkillContext: "ctx"]
    "boss_skill_bite",              # [BossSkillContext: "ctx"]
    "boss_skill_climax",            # [BossSkillContext: "ctx"]
    "boss_skill_forbidden_love",    # [BossSkillContext: "ctx"]
    "boss_skill_frost_arrow",       # [BossSkillContext: "ctx"]
    "boss_skill_fury_explosion",    # [BossSkillContext: "ctx"]
    "boss_skill_harvest",           # [BossSkillContext: "ctx"]
    "boss_skill_hemokinesis",       # [BossSkillContext: "ctx"]
    "boss_skill_infection",         # [BossSkillContext: "ctx"]
    "boss_skill_petrifying_gaze",   # [BossSkillContext: "ctx"]
    "boss_skill_rallying_cry",      # [BossSkillContext: "ctx"]
    "boss_skill_snake_trap",        # [BossSkillContext: "ctx"]
    "boss_skill_split",             # [BossSkillContext: "ctx"]
    "boss_skill_vampiric_impulse",  # [BossSkillContext: "ctx"]
    "boss_skill_venom_fang",        # [BossSkillContext: "ctx"]
    "boss_skill_whip",              # [BossSkillContext: "ctx"]

    # General Status-Related
    "status_applied",               # [DMStatus: "status"][Optional[AttackContext]: "ctx"]
    "status_execute",               # [DMStatus: "status"]

    # Specific Status-Related
    "recovery_canceled_by_burn",    # [int: "amount"]

    # Item Generation-Related
    "egg_hatch",                    # [EggHatchContext: "ctx"]
    "room_spawn",                   # [RoomSpawnContext: "ctx"]

    # Fate-Related
    "event_fate",                   # [DMEvent: "event"]
    "dungeon_fate",                 # [None]

    # Enhancement-Related
    "experience_awarded",           # [ExperienceContext: "ctx"]
    "room_enhance",                 # [ExperienceContext: "ctx"]

    # Inventory-Related
    "gold_acquired",                # [GoldSoulContext: "ctx"]
    "relic_acquired",               # [DMRelic: "relic"]
    "soul_acquired",                # [GoldSoulContext: "ctx"]
    "book_acquired",                # [DMBook: "book"]
    "book_complete",                # [DMBook: "book"]
    "on_purchase",                  # [PurchaseContext: "ctx"]

    # Stats-Related
    "stat_calculation",             # [None]
    "reset_stats",                  # [None]

    # Dungeon-Related
    "day_advance",                  # [None]
    "room_placed",                  # [DMRoom: "room"]
    "room_removed",                 # [DMRoom: "room"]
    "room_swap",                    # [DMRoom: "room"]
]
################################################################################
