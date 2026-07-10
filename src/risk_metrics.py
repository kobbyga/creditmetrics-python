import numpy as np

def calculate_losses(portfolio_values, initial_portfolio_value):
    """
    Calculate portfolio losses (negative of returns).
    Loss = Initial Value - Forward Value
    """
    losses = initial_portfolio_value - portfolio_values
    return losses
  
def calculate_var_and_es(losses, confidence_levels):
    """
    Calculate Absolute VaR and Expected Shortfall.
    
    Args:
        losses: (num_scenarios,) array of portfolio losses
        confidence_levels: list of confidence levels [0.95, 0.99]
    
    Returns:
        results: dict with VaR and ES for each confidence level
    """
    results = {}
    
    for conf in confidence_levels:
        # VaR = loss at the confidence level percentile
        var = np.percentile(losses, conf * 100)
        
        # ES = average loss in tail (losses >= VaR)
        tail_losses = losses[losses >= var]
        es = np.mean(tail_losses) if len(tail_losses) > 0 else var
        
        results[conf] = {
            'VaR': var,
            'ES': es,
            'num_tail': len(tail_losses),
            'pct_tail': (len(tail_losses) / len(losses)) * 100
        }
    
    return results
