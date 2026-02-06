# 1. Detailed Task Conceptualization
# Create an advanced Dice Roll Simulation that goes beyond basic random generation by implementing a weighted probability system and statistical analysis dashboard. Users can configure custom dice (any number of sides), roll multiple dice simultaneously, apply modifiers, and analyze the distribution of results over multiple simulations to verify probability theory.

# Subtasks
# Input Validation with Pydantic: Create models to validate user inputs including number of dice (1-10), number of sides per die (4, 6, 8, 10, 12, 20), number of rolls (1-10,000), and optional modifiers (-20 to +20)

# Random Number Generation: Use Python's random module (randint() or choices()) to simulate dice rolls with either uniform or weighted probability distributions

# Statistical Analysis with Regular Expressions: Parse and validate dice notation patterns (e.g., "3d6+5" meaning "roll 3 six-sided dice and add 5") using the re module to extract roll parameters
# ​

# Frequency Distribution Calculation: Track and calculate the frequency of each outcome, comparing actual results against theoretical probability distributions

# Visualization Output: Generate ASCII art representations of dice faces and statistical summaries showing percentage distributions, mean, median, and mode of results

# Input/Output
# Input Variables:
# dice_notation (string): Standard RPG dice notation (e.g., "2d6", "1d20+3", "4d8-2")
# num_simulations (integer): Number of times to roll the dice set (1-10,000)
# probability_weights (optional list): Custom probability weights for non-uniform distributions
# show_individual_rolls (boolean): Whether to display each roll or just statistics

# Output Variables:
# roll_results (list): All individual roll results
# total_sum (integer): Sum of all dice in final roll
# frequency_distribution (dictionary): Count of each possible outcome
# statistics (dictionary): Mean, median, mode, standard deviation
# theoretical_vs_actual (dictionary): Comparison of expected vs observed probabilities
# ascii_visualization (string): Visual representation of dice faces

from typing import List, Optional
from pydantic import BaseModel, Field, field_validator
import random
from enum import Enum


class DiceType(str, Enum):
    D4 = "d4"
    D6 = "d6"
    D8 = "d8"
    D10 = "d10"
    D12 = "d12"
    D20 = "d20"
    D100 = "d100"


class DiceConfig(BaseModel):
    sides: int = Field(gt=0, description="Number of sides on the dice")
    count: int = Field(default=1, gt=0, le=100, description="Number of dice to roll")
    modifier: int = Field(default=0, description="Modifier to add to the total")

    @field_validator("sides")
    @classmethod
    def validate_sides(cls, v):
        if v not in [4, 6, 8, 10, 12, 20, 100]:
            raise ValueError(
                "Sides must be a standard dice value (4, 6, 8, 10, 12, 20, 100)"
            )
        return v


class RollResult(BaseModel):
    rolls: List[int] = Field(description="Individual roll results")
    total: int = Field(description="Sum of all rolls")
    total_with_modifier: int = Field(description="Total including modifier")
    config: DiceConfig = Field(description="Configuration used for this roll")

    @property
    def formatted(self) -> str:
        dice_str = f"{self.config.count}d{self.config.sides}"
        if self.config.modifier != 0:
            mod_str = f"{self.config.modifier:+d}"
            return f"{dice_str}{mod_str}: {self.rolls} = {self.total_with_modifier}"
        return f"{dice_str}: {self.rolls} = {self.total}"


class DiceRoller(BaseModel):
    config: DiceConfig
    history: List[RollResult] = Field(default_factory=list)

    def roll(self) -> RollResult:
        rolls = [random.randint(1, self.config.sides) for _ in range(self.config.count)]
        total = sum(rolls)
        total_with_modifier = total + self.config.modifier

        result = RollResult(
            rolls=rolls,
            total=total,
            total_with_modifier=total_with_modifier,
            config=self.config,
        )
        self.history.append(result)
        return result

    def roll_multiple(self, times: int) -> List[RollResult]:
        """Roll dice multiple times"""
        return [self.roll() for _ in range(times)]

    @property
    def average_roll(self) -> Optional[float]:
        if not self.history:
            return None
        return sum(r.total_with_modifier for r in self.history) / len(self.history)


if __name__ == "__main__":
    config = DiceConfig(sides=6, count=2, modifier=3)
    roller = DiceRoller(config=config)

    result = roller.roll()
    print(result.formatted)

    results = roller.roll_multiple(5)
    for r in results:
        print(r.formatted)

    print(f"\nAverage roll: {roller.average_roll:.2f}")
    print(f"Total rolls: {len(roller.history)}")
