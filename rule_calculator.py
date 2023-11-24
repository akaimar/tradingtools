import dearpygui.dearpygui as dpg
from common_functions import arvutaja, puhastaja, sync_fields

def create_rule_calculator(width, height, offset_x, offset_y):
    with dpg.window(label="2% Rule Calculator", width=width, height=height, pos=(offset_x, offset_y)):
        # Add all the widgets for the 2% Rule Calculator here
        # Use the `arvutaja`, `puhastaja`, and `sync_fields` functions from common_functions.py
        dpg.add_input_float(label="Entry", tag="entry", step=0.01, callback=sync_fields, user_data="ostuhind")
        dpg.add_input_float(label="Stoploss", tag="stoploss", step=0.01)
        dpg.add_input_float(label="Target", tag="target", step=0.01, callback=sync_fields, user_data="myygihind")
        dpg.add_input_float(label="Purchase Cost", tag="buycost", step=0.01, callback=sync_fields, user_data="ostukulu")
        dpg.add_input_float(label="Selling Cost", tag="sellcost", step=0.01, callback=sync_fields, user_data="myygikulu")

        dpg.add_button(label="Calculate", callback=arvutaja)
        dpg.add_button(label="Clear", callback=puhastaja)
        dpg.add_text("Results:\n", tag="results_label")
        dpg.add_text("", tag="results_output")
        pass
