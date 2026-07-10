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

## How to run

1. Clone Repository
- Run;
- git clone https://github.com/kobbyga/creditmetrics-python.git
- cd creditmetrics-python
- in terminal

2. Install Dependencies
- pip install -r requirements.txt

3. Launch Jupyter Notebook
- Open creditmetrics_demo.ipynb
- Run all cells

## Example

...

## Results

(images)

## Future Improvements

...
