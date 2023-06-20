# import matplotlib.pyplot as plt
#
# # Initialize variables
# days = 2000
# heroes_start = 8
# heroes_end = heroes_start + days // 20
# exp_normal = 5
# exp_elite = 10
# exp_required_start = 100
# exp_required_end = 2000
# heroes = []
# exp_gained = []
# exp_required = []
#
# # Calculate values for each day
# for day in range(1, days+1):
#     # Calculate number of heroes invading
#     hero_increase_rate = 5 + 15 * (day / days)
#     if day % hero_increase_rate < 1:
#         heroes_start += 1
#     heroes.append(heroes_start)
#
#     # Calculate experience gained
#     exp_gained_day = heroes_start * exp_normal
#     if day % 10 == 0:  # Assume an elite hero comes every 10 days
#         exp_gained_day += exp_elite
#     exp_gained.append(exp_gained_day)
#
#     # Calculate experience required to level up
#     exp_required_day = exp_required_start + (exp_required_end - exp_required_start) * (day / days)
#     exp_required.append(exp_required_day)
#
# # Plot results
# plt.figure(figsize=(10, 6))
# plt.plot(range(1, days+1), heroes, label='Heroes')
# plt.plot(range(1, days+1), exp_gained, label='EXP Gained')
# plt.plot(range(1, days+1), exp_required, label='EXP Required')
# plt.xlabel('Day')
# plt.ylabel('Value')
# plt.legend()
# plt.show()

def game_progression(day, battle_type='normal'):
    # Initialize variables
    exp_normal = 5
    exp_elite = 10
    exp_required_start = 100
    exp_required_end = 20000

    # Calculate number of heroes invading
    hero_increase_start = 5
    hero_increase_end = 20
    hero_increase_rate = hero_increase_start + (hero_increase_end - hero_increase_start) * (day / 2000)
    heroes = 8 + int(day / hero_increase_rate)

    # Calculate experience gained
    if battle_type == 'normal':
        exp_gained_day = heroes * exp_normal
    else:  # battle_type == 'elite'
        exp_gained_day = heroes * exp_elite

    # Calculate experience required to level up
    exp_required_day = exp_required_start + (exp_required_end - exp_required_start) * (day / 2000)

    return heroes, exp_gained_day, exp_required_day

# Test the function
day = 1000
heroes, exp_gained, exp_required = game_progression(day, battle_type='elite')
print(f"Day {day}: {heroes} heroes, {exp_gained} EXP gained, {exp_required} EXP required")
