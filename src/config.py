import numpy as np

NUM_SCENARIOS = 50000
CONFIDENCE_LEVELS = [0.95, 0.99]
np.random.seed(42)
 
# Ratings (ordered from best to worst)
RATINGS = ['Aa', 'Aa', 'A', 'Baa', 'Ba', 'B', 'Caa-C', 'Default']
RATING_INDEX = {rating: i for i, rating in enumerate(RATINGS)}

bond_names = ['Boyd Gaming Corp', 'Brinker International Inc', 'American Airlines Group Inc']

# Current exposures (in dollars)
exposures = {
    'Boyd Gaming Corp': 4_000_000,
    'Brinker International Inc': 5_000_000,
    'American Airlines Group Inc': 6_000_000
}

# Current forward values at t=0 (should be close to exposures) (Calculation can be found in data/valuation.csv)
current_values = {
    'Boyd Gaming Corp': 3_980_869,
    'Brinker International Inc': 5_125_176,
    'American Airlines Group Inc': 6_116_918
    }

initial_portfolio_value = sum(current_values.values())

# Forward values at 1-year horizon for each rating. (Calculation can be found in data/valuation.csv)
forward_values = {
    'Boyd Gaming Corp': {
        'Aaa': 4_105_450,
        'Aa': 4_077_394,
        'A': 4_065_235,
        'Baa': 4_042_173,
        'Ba': 3_978_112,
        'B': 3_890_678,
        'Caa-C': 3_688_288,
        'Default': 0  # Will be overridden by recovery × exposure
            },
    'Brinker International Inc': {
        'Aaa': 5_319_568,
        'Aa': 5_266_557,
        'A': 5_245_895,
        'Baa': 5_201_549,
        'Ba': 5_080_615,
        'B': 4_932_823,
        'Caa-C': 4_569_623,
        'Default': 0
    },
    'American Airlines Group Inc': {
        'Aaa': 6_698_778,
        'Aa': 6_612_932,
        'A': 6_582_203,
        'Baa': 6_509_991,
        'Ba': 6_313_624,
        'B': 6_098_192,
        'Caa-C': 5_534_339,
        'Default': 0
    }
}

# Cholesky matrix (3x3 lower triangular for 3 bonds) (Calculation can be found in data/correlation.csv)
cholesky_matrix = np.array([
    [1.0000, 0.0000, 0.0000],
    [0.5219, 0.8530, 0.0000],
    [0.4665, 0.2129, 0.8585]
])

# Rating thresholds.
# Structure: thresholds[bond][rating] = threshold value (Calculation can be found in data/thresholds.csv)
rating_thresholds = {
    "Boyd Gaming Corp": {
    "thresholds": np.array([-2.6336,-2.2361,-1.5621,2.6336]),
    "states": ["Default", "Caa-C", "B", "Ba", "Baa"]
    },
    "Brinker International Inc": {
    "thresholds": np.array([-2.6336,-2.2361,-1.5621,2.6336]),
    "states": ["Default", "Caa-C", "B", "Ba", "Baa"]
    },
    "American Airlines Group Inc": {
    "thresholds": np.array([-2.1082,0.8566,2.3759]),
    "states": ["Caa-C", "B", "Ba", "Baa"]
    }
}

# Recovery rate distribution parameters (Beta distribution). (Calculation can be found in data/valuation.csv)
# Same alpha and beta for all bonds (Senior Unsecured)
alpha = 8.3653      # Beta alpha parameter
beta_param = 13.7068 # Beta beta parameter
