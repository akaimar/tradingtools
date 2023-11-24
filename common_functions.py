import dearpygui.dearpygui as dpg

def arvuta(sender, app_data, user_data):
    # Functionality for the Profit Calculator
    # Function to calculate values
    a = dpg.get_value("ostuhind")
    b = dpg.get_value("ostukogus")
    c = dpg.get_value("myygihind")
    d = dpg.get_value("myygikogus")
    e = dpg.get_value("ostukulu")
    f = dpg.get_value("myygikulu")

    kogukulu = round(a * b, 2)
    kulu = round((e + f), 2)
    kasum = round(((c * d) - (a * b)) - kulu, 2)
    breakeven = 0 if b == 0 else round((kulu / b) + a, 2)

    results_profit_calculator = f"Trade cost: {round(kogukulu, 2)}\nKasum: {round(kasum, 2)}\nTehingukulu: {round(kulu, 2)}\n" \
              f"Breakeven price: {round(breakeven, 2)}"
    
    dpg.set_value("results_profit_output", results_profit_calculator)
    pass

def arvutaja(sender, app_data, user_data):
    # Functionality for the 2% Rule Calculator
    capital = dpg.get_value("capital")
    risk_percent = dpg.get_value("risk_percent")
    entry = dpg.get_value("entry")
    stoploss = dpg.get_value("stoploss")
    target = dpg.get_value("target")
    buycost = dpg.get_value("buycost")
    sellcost = dpg.get_value("sellcost")

    risk_amount = capital * (risk_percent / 100)
    risk_per_share = entry - stoploss
    profit_per_share = target - entry
    risk_reward = profit_per_share / risk_per_share if risk_per_share != 0 else 0
    shares_to_buy = risk_amount / risk_per_share if risk_per_share != 0 else 0
    investment = shares_to_buy * entry
    potential_loss = risk_per_share * shares_to_buy
    potential_grossprofit = shares_to_buy * profit_per_share
    potential_netprofit = potential_grossprofit - buycost - sellcost

    results_rule_calculator = f"Capital: {round(capital, 2)}\nRisk Amount: {round(risk_amount, 2)}\nRisk per Share: {round(risk_per_share, 2)}\n" \
              f"Profit per Share: {round(profit_per_share, 2)}\nRisk Reward: {round(risk_reward, 3)}\nShares to Buy: {round(shares_to_buy, 2)}\n" \
              f"Investment: {round(investment, 2)}\nAllowed Max Loss: {round(potential_loss, 2)}\nPotential Gross Profit: {round(potential_grossprofit, 2)}\n" \
              f"Potential Net Profit: {round(potential_netprofit, 2)}"
    
    dpg.set_value("results_rule_output", results_rule_calculator)
    pass

def puhastaja(sender, app_data, user_data):
    # Clearing function for the 2% Rule Calculator
    dpg.set_value("capital", 0)
    dpg.set_value("risk_percent", 0)
    dpg.set_value("entry", 0)
    dpg.set_value("stoploss", 0)
    dpg.set_value("target", 0)
    dpg.set_value("buycost", 0)
    dpg.set_value("sellcost", 0)
    dpg.set_value("results_output", "Enter data!")
    pass

def puhastaja_profit_calculator(sender, app_data, user_data):
    dpg.set_value("ticker", "")
    dpg.set_value("ostuhind", 0)
    dpg.set_value("ostukogus", 0)
    dpg.set_value("myygihind", 0)
    dpg.set_value("myygikogus", 0)
    dpg.set_value("ostukulu", 0)
    dpg.set_value("myygikulu", 0)
    pass

def sync_fields(sender, app_data, user_data):
    # Synchronization function between windows
    dpg.set_value(user_data, dpg.get_value(sender))
    pass