import numpy as np

def calculate_loan_forward_values(rating_scenarios, recovery_rates, forward_values, exposures):
    """
    Calculate implied forward loan values at 1-year horizon.
    
    Args:
        rating_scenarios: dict[bond_name] = array of rating indices
        recovery_rates: (num_scenarios, num_bonds) array of recovery rates
        forward_values: dict[bond_name][rating] = forward value at that rating
        exposures: dict[bond_name] = current exposure
    
    Returns:
        loan_forward_values: dict[bond_name] = (num_scenarios,) array of values
    """
    num_scenarios = recovery_rates.shape[0]
    bond_names = list(rating_scenarios.keys())
    
    loan_forward_values = {bond_name: np.zeros(num_scenarios) 
                          for bond_name in bond_names}
    
    for bond_idx, bond_name in enumerate(bond_names):
        ratings = rating_scenarios[bond_name]
        recoveries = recovery_rates[:, bond_idx]
        exposure = exposures[bond_name]
        forward_vals = forward_values[bond_name]
        
        for scenario_idx in range(num_scenarios):
            rating = ratings[scenario_idx]
            
            if rating == 'Default':
                # In default: value = exposure × recovery rate
                loan_forward_values[bond_name][scenario_idx] = exposure * recoveries[scenario_idx]
            else:
                # Non-default: value = forward value for that rating
                loan_forward_values[bond_name][scenario_idx] = forward_vals[rating]
    
    return loan_forward_values

def calculate_portfolio_values(loan_forward_values):
    """
    Aggregate loan values to portfolio level.
    
    Args:
        loan_forward_values: dict[bond_name] = (num_scenarios,) array
    
    Returns:
        portfolio_values: (num_scenarios,) array of total portfolio values
    """
    num_scenarios = loan_forward_values[list(loan_forward_values.keys())[0]].shape[0]
    portfolio_values = np.zeros(num_scenarios)
    
    for bond_name, values in loan_forward_values.items():
        portfolio_values += values
    
    return portfolio_values
