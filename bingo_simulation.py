#!/usr/bin/env python3
##########################################
# Bingo Round Monte Carlo Simulation
# Estimates expected draws for a bingo win
##########################################

import random
import statistics
from typing import List, Tuple
import typer

def generate_bingo_card(nmax: int = 90, kmax: int = 25) -> set:
    """Generate a single bingo card with kmax unique numbers from 1 to nmax"""
    if kmax > nmax:
        raise ValueError(f"Numbers per card ({kmax}) cannot exceed max number ({nmax})")
    return set(random.sample(range(1, nmax + 1), kmax))

def simulate_bingo_round(nmax: int, cmax: int, kmax: int = 25) -> int:
    """
    Simulate a single bingo round and return number of draws until first win

    Args:
        nmax: Maximum number on cards (typically 90)
        cmax: Number of cards in play
        kmax: Numbers per card (default 25)

    Returns:
        Number of draws until first card wins
    """
    # Generate all cards
    cards = [generate_bingo_card(nmax, kmax) for _ in range(cmax)]
    
    # Track drawn numbers
    drawn_numbers = set()
    available_numbers = list(range(1, nmax + 1))
    random.shuffle(available_numbers)
    
    draws = 0
    
    # Draw numbers until someone wins
    for number in available_numbers:
        draws += 1
        drawn_numbers.add(number)
        
        # Check if any card wins (all 25 numbers drawn)
        for card in cards:
            if card.issubset(drawn_numbers):
                return draws
    
    # This shouldn't happen in a valid game
    return draws

def monte_carlo_bingo_estimation(nmax: int, cmax: int, simulations: int = 10000, kmax: int = 25) -> Tuple[float, float]:
    """
    Perform Monte Carlo simulation to estimate expected draws and standard deviation

    Args:
        nmax: Maximum number on cards (typically 90)
        cmax: Number of cards in play
        simulations: Number of simulations to run (default 10000)
        kmax: Numbers per card (default 25)

    Returns:
        Tuple of (expected_value, population_standard_deviation)
    """
    random.seed()  # Ensure randomness

    results = []

    for _ in range(simulations):
        draws = simulate_bingo_round(nmax, cmax, kmax)
        results.append(draws)
    
    expected_value = statistics.mean(results)
    pop_std_dev = statistics.pstdev(results)  # Population standard deviation
    
    return expected_value, pop_std_dev

def analyze_bingo_scenario(nmax: int = 90, cmax: int = 200, simulations: int = 10000, kmax: int = 25):
    """
    Analyze a bingo scenario and print results

    Args:
        nmax: Maximum number on cards (default 90)
        cmax: Number of cards in play (default 200)
        simulations: Number of simulations (default 10000)
        kmax: Numbers per card (default 25)
    """
    print(f"Analyzing Bingo Scenario:")
    print(f"  Max number: {nmax}")
    print(f"  Cards in play: {cmax}")
    print(f"  Simulations: {simulations}")
    print(f"  Numbers per card: {kmax}")
    print()

    expected, std_dev = monte_carlo_bingo_estimation(nmax, cmax, simulations, kmax)
    
    print(f"Results:")
    print(f"  Expected draws until win: {expected:.2f}")
    print(f"  Population standard deviation: {std_dev:.2f}")
    print(f"  95% confidence interval: {expected - 1.96 * std_dev:.2f} - {expected + 1.96 * std_dev:.2f}")

def main(
    nmax: int = typer.Option(90, "--nmax", "-n", help="Maximum number on cards"),
    cmax: int = typer.Option(200, "--cmax", "-c", help="Number of cards in play"),
    simulations: int = typer.Option(10000, "--simulations", "-s", help="Number of simulations to run"),
    kmax: int = typer.Option(25, "--kmax", "-k", help="Numbers per card")
):
    """
    Run bingo simulation with Monte Carlo estimation.

    Analyzes a bingo scenario and estimates the expected number of draws
    until the first card wins using Monte Carlo simulation.
    """
    analyze_bingo_scenario(nmax, cmax, simulations, kmax)

if __name__ == "__main__":
    typer.run(main)