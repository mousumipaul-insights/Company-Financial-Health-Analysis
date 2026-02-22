"""
ratio_calculator.py
-------------------
Financial ratio calculation functions.
Author: Mousumi Paul | Dec 2024
"""

# ──────────────────────────────────────────
# LIQUIDITY RATIOS
# ──────────────────────────────────────────

def current_ratio(current_assets, current_liabilities):
    """Measures ability to cover short-term obligations."""
    return current_assets / current_liabilities


def quick_ratio(current_assets, inventory, current_liabilities):
    """Liquidity excluding inventory."""
    return (current_assets - inventory) / current_liabilities


def cash_ratio(cash_and_equivalents, current_liabilities):
    """Most conservative liquidity measure."""
    return cash_and_equivalents / current_liabilities


# ──────────────────────────────────────────
# PROFITABILITY RATIOS
# ──────────────────────────────────────────

def gross_margin(revenue, cogs):
    """Gross Profit Margin (%)."""
    return ((revenue - cogs) / revenue) * 100


def ebitda_margin(ebitda, revenue):
    """EBITDA Margin (%)."""
    return (ebitda / revenue) * 100


def net_profit_margin(net_income, revenue):
    """Net Profit Margin (%)."""
    return (net_income / revenue) * 100


def return_on_equity(net_income, shareholders_equity):
    """ROE (%)."""
    return (net_income / shareholders_equity) * 100


def return_on_assets(net_income, total_assets):
    """ROA (%)."""
    return (net_income / total_assets) * 100


def return_on_capital_employed(ebit, total_assets, current_liabilities):
    """ROCE (%)."""
    capital_employed = total_assets - current_liabilities
    return (ebit / capital_employed) * 100


# ──────────────────────────────────────────
# LEVERAGE RATIOS
# ──────────────────────────────────────────

def debt_to_equity(total_debt, shareholders_equity):
    """Debt-to-Equity ratio."""
    return total_debt / shareholders_equity


def debt_to_assets(total_debt, total_assets):
    """Proportion of assets financed by debt."""
    return total_debt / total_assets


def interest_coverage(ebit, interest_expense):
    """Times interest is covered by operating profit."""
    return ebit / interest_expense


# ──────────────────────────────────────────
# EFFICIENCY RATIOS
# ──────────────────────────────────────────

def asset_turnover(revenue, total_assets):
    """Revenue generated per unit of asset."""
    return revenue / total_assets


def inventory_turnover(cogs, average_inventory):
    """How many times inventory is sold per year."""
    return cogs / average_inventory


def receivables_turnover(revenue, average_receivables):
    """How efficiently receivables are collected."""
    return revenue / average_receivables


def days_sales_outstanding(average_receivables, revenue):
    """Average days to collect receivables."""
    return (average_receivables / revenue) * 365


def days_inventory_outstanding(average_inventory, cogs):
    """Average days inventory is held."""
    return (average_inventory / cogs) * 365


# ──────────────────────────────────────────
# SUMMARY FUNCTION
# ──────────────────────────────────────────

def compute_all_ratios(fs: dict) -> dict:
    """
    Compute all ratios from a flat financial statement dict.
    
    Parameters:
        fs (dict): Keys include revenue, cogs, ebitda, ebit, net_income,
                   current_assets, current_liabilities, inventory,
                   cash_and_equivalents, total_assets, total_debt,
                   shareholders_equity, interest_expense,
                   average_inventory, average_receivables
    
    Returns:
        dict: All computed ratios
    """
    ratios = {
        # Liquidity
        "Current Ratio":        current_ratio(fs["current_assets"], fs["current_liabilities"]),
        "Quick Ratio":          quick_ratio(fs["current_assets"], fs["inventory"], fs["current_liabilities"]),
        "Cash Ratio":           cash_ratio(fs["cash_and_equivalents"], fs["current_liabilities"]),

        # Profitability
        "Gross Margin (%)":     gross_margin(fs["revenue"], fs["cogs"]),
        "EBITDA Margin (%)":    ebitda_margin(fs["ebitda"], fs["revenue"]),
        "Net Margin (%)":       net_profit_margin(fs["net_income"], fs["revenue"]),
        "ROE (%)":              return_on_equity(fs["net_income"], fs["shareholders_equity"]),
        "ROA (%)":              return_on_assets(fs["net_income"], fs["total_assets"]),
        "ROCE (%)":             return_on_capital_employed(fs["ebit"], fs["total_assets"], fs["current_liabilities"]),

        # Leverage
        "Debt-to-Equity":       debt_to_equity(fs["total_debt"], fs["shareholders_equity"]),
        "Debt-to-Assets":       debt_to_assets(fs["total_debt"], fs["total_assets"]),
        "Interest Coverage":    interest_coverage(fs["ebit"], fs["interest_expense"]),

        # Efficiency
        "Asset Turnover":       asset_turnover(fs["revenue"], fs["total_assets"]),
        "Inventory Turnover":   inventory_turnover(fs["cogs"], fs["average_inventory"]),
        "Receivables Turnover": receivables_turnover(fs["revenue"], fs["average_receivables"]),
        "Days Sales Outstanding": days_sales_outstanding(fs["average_receivables"], fs["revenue"]),
        "Days Inventory Outstanding": days_inventory_outstanding(fs["average_inventory"], fs["cogs"]),
    }
    return ratios
