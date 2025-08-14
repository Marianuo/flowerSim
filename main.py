import matplotlib.pyplot as plt
import random
import os

# Simulation parameters
time_steps = 30
growth = [0]
current_height = 0

# Updated weather logic with sunny hours effect
weather_growth_effects = {
    "sunny": {"chance": 0.8, "sunny_hours": (4, 8), "base_growth": (1.0, 2.5)},
    "cloudy": {"chance": 0.7, "sunny_hours": (1, 3), "base_growth": (0.5, 1.5)},
    "rainy": {"chance": 0.9, "sunny_hours": (2, 5), "base_growth": (0.8, 2.0)},
    "stormy": {"chance": 0.3, "sunny_hours": (0, 1), "base_growth": (0.0, 0.5)}
}

daily_weather = []
daily_growth = []
daily_sun = []

# Simulation loop with enhanced weather rules
for day in range(1, time_steps + 1):
    weather = random.choice(list(weather_growth_effects.keys()))
    effect = weather_growth_effects[weather]

    sunny_hours = random.uniform(*effect["sunny_hours"])
    chance = effect["chance"]
    base_growth_range = effect["base_growth"]

    # this is to add a bonus for more sun time we get during a specific day, maximum sun hours is 8 that's why we factor by 8
    sun_factor = sunny_hours / 8
    adjusted_chance = chance + (sun_factor * 0.1)  # small bonus
    adjusted_chance = min(adjusted_chance, 1.0)

    if random.random() < adjusted_chance:
        growth_range = base_growth_range
        daily_increase = random.uniform(*growth_range) * sun_factor
        current_height += daily_increase
    else:
        daily_increase = 0

    daily_weather.append(weather)
    daily_growth.append(daily_increase)
    daily_sun.append(sunny_hours)
    growth.append(current_height)

# Plotting
days = list(range(0, time_steps + 1))
plt.figure(figsize=(12, 6))
plt.plot(days, growth, marker='o', color='green')
plt.title(" Plant Growth Simulation with Sunny Hours")
plt.xlabel("Day")
plt.ylabel("Plant Height (cm)")
plt.grid(True)

# Annotate weather on the graph
for i in range(len(daily_weather)):
    weather = daily_weather[i]
    sun = daily_sun[i]
    label = f"{weather[0].upper()} ({sun:.1f}h)"
    plt.annotate(label, (i, growth[i]), textcoords="offset points", xytext=(0,5), ha='center', fontsize=8)

# Save the plot (it will be saved in your downloads on ur pc)
downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
final_path = os.path.join(downloads_folder, "plant_growth_simulation.png")
plt.tight_layout()
plt.savefig(final_path)
