import dearpygui.dearpygui as dpg
from common_functions import arvuta, sync_fields

def create_profit_calculator(width, height, offset_y):
    with dpg.window(label="Profit Calculator", width=width, height=height, pos=(0, offset_y)):
    # Add all the widgets for the Profit Calculator here
    # Use the `arvuta` and `sync_fields` functions from common_functions.py
        dpg.add_text("Ticker: ")
        dpg.add_input_text(tag="ticker")

        dpg.add_text("Entry: ")
        dpg.add_input_float(tag="ostuhind", step=0.01, step_fast=0.1, callback=sync_fields, user_data="entry")

        dpg.add_text("Purchase Quantity: ")
        dpg.add_input_int(tag="ostukogus")

        dpg.add_text("Target: ")
        dpg.add_input_float(tag="myygihind", step=0.01, step_fast=0.1, callback=sync_fields, user_data="target")

        dpg.add_text("Selling Quantity: ")
        dpg.add_input_int(tag="myygikogus")

        dpg.add_text("Purchase Cost: ")
        dpg.add_input_float(tag="ostukulu", step=0.01, step_fast=0.1, callback=sync_fields, user_data="buycost")

        dpg.add_text("Selling Cost: ")
        dpg.add_input_float(tag="myygikulu", step=0.01, step_fast=0.1, callback=sync_fields, user_data="sellcost")

        dpg.add_button(label="Calculate", callback=arvuta)
        
        dpg.add_text("Total Cost: ")
        dpg.add_text("", tag="print_kogukulu")
        dpg.add_text("Profit: ")
        dpg.add_text("", tag="print_kasum")
        dpg.add_text("Transaction Cost: ")
        dpg.add_text("", tag="print_kulu")
        dpg.add_text("Breakeven: ")
        dpg.add_text("", tag="print_breakeven")
        pass
