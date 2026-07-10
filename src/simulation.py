import numpy as np
from scipy.special import beta as beta_function
from scipy.stats import norm

def generate_correlated_returns(num_scenarios, cholesky_matrix, num_bonds=3):
    """
    Generate correlated asset returns using Cholesky decomposition.
    
    Args:
        num_scenarios: Number of MC scenarios (50,000)
        cholesky_matrix: 3x3 lower triangular Cholesky matrix
        num_bonds: Number of bonds (3)
    
    Returns:
        correlated_returns: (num_scenarios, num_bonds) array of correlated returns
    """
    # Generating uncorrelated standard normal returns
    uncorrelated_returns = np.random.standard_normal((num_scenarios, num_bonds))
    
    # Applying Cholesky matrix to induce correlation
    # Formula: correlated = uncorrelated @ cholesky.T
    correlated_returns = uncorrelated_returns @ cholesky_matrix.T
    
    return correlated_returns, uncorrelated_returns

def map_returns_to_ratings(correlated_returns, rating_thresholds):
    """
    Map correlated asset returns to rating states using proper CreditMetrics thresholds.
    
    rating_thresholds[bond] contains:
        - "thresholds": np.array([...]) sorted ascending
        - "states":     list of rating labels, len = len(thresholds) + 1
    """
    num_scenarios, num_bonds = correlated_returns.shape
    rating_scenarios = {}

    for bond_idx, (bond_name, info) in enumerate(rating_thresholds.items()):
        thresholds = info["thresholds"]      # e.g. [-2.63, -2.23, -1.56, 2.63]
        states     = info["states"]          # e.g. ["D","Caa","B","Ba","Baa"]

        z = correlated_returns[:, bond_idx]

        # searchsorted gives the correct interval index
        idx = np.searchsorted(thresholds, z)

        # Mapping indices to rating labels
        mapped = np.array([states[i] for i in idx])

        rating_scenarios[bond_name] = mapped

    return rating_scenarios

def generate_recovery_rates(num_scenarios, alpha, beta, num_bonds=3):
    """
    Generate uncorrelated recovery rates using Beta distribution.
    Uses Beta(alpha, beta) inverse CDF on uniform(0,1) random variables.
    
    Args:
        num_scenarios: Number of MC scenarios (50,000)
        alpha: Shape parameter (same for all bonds)
        beta: Shape parameter (same for all bonds)
        num_bonds: Number of bonds (3)
    
    Returns:
        recovery_rates: (num_scenarios, num_bonds) array of recovery rates [0,1]
    """
    # Generating uncorrelated uniform(0,1) random variables
    uniform_random = np.random.uniform(0, 1, (num_scenarios, num_bonds))
    
    # Applying inverse beta CDF: betainv(u) = Beta^(-1)(u; alpha, beta)
    # Use scipy's beta distribution PPF (percent point function = inverse CDF)
    from scipy.stats import beta as beta_dist
    recovery_rates = beta_dist.ppf(uniform_random, alpha, beta)
    
    # Clipping to [0, 1] to handle numerical edge cases
    recovery_rates = np.clip(recovery_rates, 0, 1)
    
    return recovery_rates, uniform_random
