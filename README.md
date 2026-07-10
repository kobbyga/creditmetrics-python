# CreditMetrics Portfolio Risk Model

A Python implementation of the CreditMetrics framework for estimating
portfolio credit risk using Monte Carlo simulation.

## Features

- Credit rating migration
- Monte Carlo simulation
- Expected Loss (EL)
- Unexpected Loss (UL)
- Credit VaR
- Expected Shortfall
- Portfolio loss distribution
- Risk visualisation

## Mathematical Framework

The model follows the CreditMetrics methodology by:

1. Generate uncorrelated asset returns (50,000 scenarios)
2. Apply Cholesky matrix to induce correlations
3. Map correlated returns to rating scenarios using thresholds
4. Generate uncorrelated recovery rates using Beta distribution
5. Calculate implied loan forward values (default or non-default)
6. Aggregate to portfolio values
7. Calculate Absolute VaR and Expected Shortfall

## Portfolio Construction



## Repository Structure

...

## Installation

pip install -r requirements.txt

## Example

...

## Results

(images)

## Future Improvements

...
