import matplotlib.pyplot as plt

def plot_loss_distribution(losses, results):
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    fig.suptitle('CreditMetrics: Correlated Returns with Variable Recovery (Base)', 
                 fontsize=16, fontweight='bold')
 
    # Plot 1: Loss distribution
    ax = axes[0, 0]
    ax.hist(losses, bins=150, color='#2E86AB', alpha=0.7, edgecolor='black', linewidth=0.5)
    ax.axvline(results[0.95]['VaR'], color='red', linestyle='--', linewidth=2.5, 
               label=f"VaR95: ${results[0.95]['VaR']:,.0f}")
    ax.axvline(results[0.99]['VaR'], color='darkred', linestyle='--', linewidth=2.5,
               label=f"VaR99: ${results[0.99]['VaR']:,.0f}")
    ax.set_xlabel('Portfolio Loss ($)', fontsize=11, fontweight='bold')
    ax.set_ylabel('Frequency', fontsize=11, fontweight='bold')
    ax.set_title('Portfolio Loss Distribution (50K Scenarios) (Base)', fontsize=12, fontweight='bold')
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)
    ax.ticklabel_format(style='plain', axis='x')
    
    # Plot 2: Tail losses
    ax = axes[0, 1]
    tail_losses = losses[losses > results[0.95]['VaR']]
    ax.hist(tail_losses, bins=60, color='#A23B72', alpha=0.7, edgecolor='black', linewidth=0.5)
    ax.axvline(results[0.95]['VaR'], color='red', linestyle='--', linewidth=2.5,
               label=f"VaR95: ${results[0.95]['VaR']:,.0f}")
    ax.axvline(results[0.95]['ES'], color='orange', linestyle='--', linewidth=2.5,
               label=f"ES95: ${results[0.95]['ES']:,.0f}")
    ax.set_xlabel('Portfolio Loss ($)', fontsize=11, fontweight='bold')
    ax.set_ylabel('Frequency', fontsize=11, fontweight='bold')
    ax.set_title('Tail Risk (Worst 5%) (Base)', fontsize=12, fontweight='bold')
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)
    ax.ticklabel_format(style='plain', axis='x')
    
    # Plot 3: VaR vs ES
    ax = axes[1, 0]
    conf_labels = ['95%', '99%']
    var_vals = [results[0.95]['VaR'], results[0.99]['VaR']]
    es_vals = [results[0.95]['ES'], results[0.99]['ES']]
    
    x = np.arange(len(conf_labels))
    width = 0.35
    bars1 = ax.bar(x - width/2, var_vals, width, label='VaR', color='#F18F01', 
                   alpha=0.85, edgecolor='black', linewidth=1.5)
    bars2 = ax.bar(x + width/2, es_vals, width, label='ES', color='#C73E1D',
                   alpha=0.85, edgecolor='black', linewidth=1.5)
    
    ax.set_ylabel('Loss Amount ($)', fontsize=11, fontweight='bold')
    ax.set_title('Absolute VaR vs Expected Shortfall (Base)', fontsize=12, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(conf_labels)
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3, axis='y')
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x/1e6:.1f}M'))
    
    # Add value labels
    for bars in [bars1, bars2]:
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'${height/1e6:.2f}M', ha='center', va='bottom', 
                   fontsize=9, fontweight='bold')
    
    # Plot 4: CDF with percentiles
    ax = axes[1, 1]
    sorted_losses = np.sort(losses)
    cdf = np.arange(1, len(sorted_losses) + 1) / len(sorted_losses)
    ax.plot(sorted_losses, cdf * 100, linewidth=2.5, color='#2E86AB', label='Empirical CDF')
    ax.axvline(results[0.95]['VaR'], color='red', linestyle='--', linewidth=2, 
               alpha=0.7, label='VaR95')
    ax.axhline(95, color='red', linestyle=':', linewidth=1.5, alpha=0.5)
    ax.axvline(results[0.99]['VaR'], color='darkred', linestyle='--', linewidth=2,
               alpha=0.7, label='VaR99')
    ax.axhline(99, color='darkred', linestyle=':', linewidth=1.5, alpha=0.5)
    ax.set_xlabel('Portfolio Loss ($)', fontsize=11, fontweight='bold')
    ax.set_ylabel('Cumulative Probability (%)', fontsize=11, fontweight='bold')
    ax.set_title('Empirical CDF of Losses (Base)', fontsize=12, fontweight='bold')
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)
    ax.ticklabel_format(style='plain', axis='x')
    
    plt.tight_layout()
    #plt.savefig('creditmetrics_correlated.png', dpi=300, bbox_inches='tight')
    #print("  ✓ Saved: creditmetrics_correlated.png")
    plt.show()
