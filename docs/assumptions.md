# Exposure Assumptions

- EAD remains constant.
- No new lending.
- No early termination.
- No prepayments.
- No principal amortisation (only coupon payments occur).
  
# Credit Rating Assumptions

- Ratings are accurate representations of borrower credit quality.
- Ratings only change once during the one-year horizon.
- Transition probabilities remain constant.
- Historical transition behaviour is representative of future behaviour.

# Transition Matrix Assumptions

- Model uses Moody's 2024 one year transition matrix, normalised to remove the WR column.
- No further recalibration is performed to aling the matrix with market implied default probabilities, sector specific risk, or macroecronomic conditions.
- Migration behaviour reflects Moody's empirical 2024 observations rather than forward looking or stress adjusted risk.

# Default Assumptions

- Default occurs only if the borrower transitions to the default state.
- Default is a permanent absorbing state.
- Recovery rates are modelled using beta distribution of the mean and standard LGD of senior unsecured bonds from historical Moody's data; historical LGD sample may not reflect modern recovery behaviour.
- Recovery occurs immediately after default.

# Valuation Methodology

- Forward values computed using rating specific Nelson-Siegel yield curve approximations, which may not fully capture market discontinuities
- The forward rates are static and have an arbitrage free term strucure with no stochastic features or spread volatility
- Cash flows are discountted deterministically, with no reinvestment risk.
- Forward values reflect a simplified, rating driven view of future bond prices rather than a fully dynamic interest rate or credit spread model.

# Correlation Assumptions

- Historical daily retusn from 2022 - 2024 used to estimate empirical asset return correlation matrix.
- A Cholesky decomposition of this matrix was applied to generate correlated shocks within a Gaussian copula framework.
- Credit migration outcomes are not independent but reflect observed co-movements in market conditions.

# Time Horizon

- One-year horizon
- No intermediate migrations
- Single-period analysis

Despite these simplifications, the project demonstrates the core mechanics of portfolio credit risk measurement and provides a foundation for more advanced models incorporating macroeconomic stress testing.
