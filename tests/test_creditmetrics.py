def stability_analysis(num_replications=50):
    """
    Re-run the full CreditMetrics simulation multiple times
    to assess stability of VaR and ES estimates.
    """

    var_99_list = []
    es_99_list = []

    for seed in range(num_replications):

        np.random.seed(seed)

        # Run CreditMetrics model
        correlated_returns, _ = generate_correlated_returns(
            NUM_SCENARIOS,
            L,
            num_bonds=3
        )

        rating_scenarios = map_returns_to_ratings(
            correlated_returns,
            rating_thresholds
        )

        recovery_rates, _ = generate_recovery_rates(
            NUM_SCENARIOS,
            alpha,
            beta,
            num_bonds=3
        )

        loan_forward_values = calculate_loan_forward_values(
            rating_scenarios,
            recovery_rates,
            forward_values,
            exposures
        )

        portfolio_values = calculate_portfolio_values(
            loan_forward_values
        )

        losses = calculate_losses(
            portfolio_values,
            initial_portfolio_value
        )

        results = calculate_var_and_es(losses, [0.99])

        var_99_list.append(results[0.99]['VaR'])
        es_99_list.append(results[0.99]['ES'])

    var_99_array = np.array(var_99_list)
    es_99_array = np.array(es_99_list)

    print("\nSTABILITY ANALYSIS")

    print(f"Number of replications: {num_replications}")
    print(f"Scenarios per replication: {NUM_SCENARIOS:,}")

    print("\n99% VaR")
    print(f"Mean: {var_99_array.mean():,.2f}")
    print(f"Std Dev: {var_99_array.std(ddof=1):,.2f}")
    print(f"CV: {(var_99_array.std(ddof=1)/var_99_array.mean())*100:.3f}%")

    print("\n99% Expected Shortfall")
    print(f"Mean: {es_99_array.mean():,.2f}")
    print(f"Std Dev: {es_99_array.std(ddof=1):,.2f}")
    print(f"CV: {(es_99_array.std(ddof=1)/es_99_array.mean())*100:.3f}%")

    # 99% confidence intervals
    var_ci = np.percentile(var_99_array, [1, 99])
    es_ci = np.percentile(es_99_array, [1, 99])

    print("\n99% Confidence Interval")
    print(f"VaR: [{var_ci[0]:,.2f}, {var_ci[1]:,.2f}]")
    print(f"ES : [{es_ci[0]:,.2f}, {es_ci[1]:,.2f}]")

    return var_99_array, es_99_array

def convergence_plot_var(var_results):
  
  plt.figure(figsize=(10,5))

  plt.plot(var_results, marker='o', color='#A23B72', alpha=0.8)
  plt.axhline(np.mean(var_results), color='red', linestyle='--', linewidth=2.5,
              label=f"Mean VaR99: £{np.mean(var_results):,.0f}")
  
  plt.title("Convergence of 99% VaR Across Replications", fontsize=12, fontweight='bold')
  plt.xlabel("Replication Index", fontsize=11, fontweight='bold')
  plt.ylabel("99% VaR (£)", fontsize=11, fontweight='bold')

  plt.grid(True, alpha=0.3)
  plt.legend(fontsize=10)
  plt.ticklabel_format(style='plain', axis='y')

  plt.show()

def convergence_plot_es(es_results):
  
  plt.figure(figsize=(10,5))

  plt.plot(es_results, marker='o', color='#A23B72', alpha=0.8)
  plt.axhline(np.mean(es_results), color='red', linestyle='--', linewidth=2.5,
            label=f"Mean VaR99: £{np.mean(es_results):,.0f}")

  plt.title("Convergence of 99% ES Across Replications", fontsize=12, fontweight='bold')
  plt.xlabel("Replication Index", fontsize=11, fontweight='bold')
  plt.ylabel("99% ES (£)", fontsize=11, fontweight='bold')

  plt.grid(True, alpha=0.3)
  plt.legend(fontsize=10)
  plt.ticklabel_format(style='plain', axis='y')

  plt.show()
