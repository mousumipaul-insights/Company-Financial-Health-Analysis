"""
dcf_model.py
------------
Discounted Cash Flow (DCF) valuation model with WACC and sensitivity analysis.
Author: Mousumi Paul | Dec 2024
"""

import numpy as np
import pandas as pd


# ──────────────────────────────────────────
# WACC CALCULATION
# ──────────────────────────────────────────

def cost_of_equity(risk_free_rate, beta, market_return):
    """
    CAPM: Cost of Equity = Rf + β × (Rm - Rf)
    """
    return risk_free_rate + beta * (market_return - risk_free_rate)


def wacc(equity, debt, cost_equity, cost_debt, tax_rate):
    """
    WACC = (E/V × Re) + (D/V × Rd × (1 - T))
    """
    total = equity + debt
    weight_equity = equity / total
    weight_debt = debt / total
    return (weight_equity * cost_equity) + (weight_debt * cost_debt * (1 - tax_rate))


# ──────────────────────────────────────────
# FREE CASH FLOW PROJECTION
# ──────────────────────────────────────────

def project_fcf(base_fcf, growth_rates):
    """
    Project Free Cash Flows over forecast period.
    
    Parameters:
        base_fcf (float): Most recent FCF
        growth_rates (list): Annual growth rates for forecast period
    
    Returns:
        list: Projected FCFs
    """
    projected = []
    fcf = base_fcf
    for g in growth_rates:
        fcf = fcf * (1 + g)
        projected.append(fcf)
    return projected


# ──────────────────────────────────────────
# TERMINAL VALUE
# ──────────────────────────────────────────

def terminal_value(final_fcf, terminal_growth_rate, discount_rate):
    """
    Gordon Growth Model: TV = FCF_n × (1 + g) / (WACC - g)
    """
    return final_fcf * (1 + terminal_growth_rate) / (discount_rate - terminal_growth_rate)


# ──────────────────────────────────────────
# DCF INTRINSIC VALUE
# ──────────────────────────────────────────

def dcf_valuation(projected_fcfs, term_value, discount_rate, net_debt, shares_outstanding):
    """
    Compute enterprise value, equity value, and intrinsic value per share.
    
    Parameters:
        projected_fcfs (list): FCFs for each forecast year
        term_value (float): Terminal value at end of forecast period
        discount_rate (float): WACC
        net_debt (float): Total debt minus cash
        shares_outstanding (float): Number of shares
    
    Returns:
        dict: EV, equity value, intrinsic value per share
    """
    n = len(projected_fcfs)
    
    # PV of projected FCFs
    pv_fcfs = sum([cf / (1 + discount_rate) ** (i + 1) for i, cf in enumerate(projected_fcfs)])
    
    # PV of terminal value
    pv_tv = term_value / (1 + discount_rate) ** n
    
    enterprise_value = pv_fcfs + pv_tv
    equity_value = enterprise_value - net_debt
    intrinsic_value_per_share = equity_value / shares_outstanding

    return {
        "PV of FCFs":                   round(pv_fcfs, 2),
        "PV of Terminal Value":         round(pv_tv, 2),
        "Enterprise Value":             round(enterprise_value, 2),
        "Equity Value":                 round(equity_value, 2),
        "Intrinsic Value Per Share":    round(intrinsic_value_per_share, 2),
    }


# ──────────────────────────────────────────
# SENSITIVITY TABLE
# ──────────────────────────────────────────

def sensitivity_table(base_fcf, growth_rates, wacc_range, tgr_range, net_debt, shares_outstanding):
    """
    Build a sensitivity table of intrinsic value across WACC × Terminal Growth Rate combinations.
    
    Parameters:
        wacc_range (list): List of WACC values (e.g., [0.08, 0.09, 0.10, 0.11, 0.12])
        tgr_range (list): List of terminal growth rates (e.g., [0.02, 0.03, 0.04])
    
    Returns:
        pd.DataFrame: Sensitivity table
    """
    table = {}
    for tgr in tgr_range:
        row = {}
        for w in wacc_range:
            fcfs = project_fcf(base_fcf, growth_rates)
            tv = terminal_value(fcfs[-1], tgr, w)
            result = dcf_valuation(fcfs, tv, w, net_debt, shares_outstanding)
            row[f"WACC={w*100:.1f}%"] = result["Intrinsic Value Per Share"]
        table[f"TGR={tgr*100:.1f}%"] = row

    return pd.DataFrame(table).T


# ──────────────────────────────────────────
# EXAMPLE USAGE
# ──────────────────────────────────────────

if __name__ == "__main__":
    # Example inputs (replace with actual company data)
    BASE_FCF = 5000          # in ₹ Crores
    GROWTH_RATES = [0.12, 0.11, 0.10, 0.09, 0.08]  # 5-year forecast
    WACC_VALUE = 0.10
    TERMINAL_GROWTH = 0.03
    NET_DEBT = 2000
    SHARES = 100             # in Crores

    fcfs = project_fcf(BASE_FCF, GROWTH_RATES)
    tv = terminal_value(fcfs[-1], TERMINAL_GROWTH, WACC_VALUE)
    result = dcf_valuation(fcfs, tv, WACC_VALUE, NET_DEBT, SHARES)

    print("\n📊 DCF Valuation Results:")
    for k, v in result.items():
        print(f"  {k}: ₹{v:,.2f}")

    print("\n📉 Sensitivity Table (Intrinsic Value per Share):")
    sens = sensitivity_table(
        BASE_FCF, GROWTH_RATES,
        wacc_range=[0.08, 0.09, 0.10, 0.11, 0.12],
        tgr_range=[0.02, 0.03, 0.04],
        net_debt=NET_DEBT,
        shares_outstanding=SHARES
    )
    print(sens.to_string())
