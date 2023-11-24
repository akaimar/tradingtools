import dearpygui.dearpygui as dpg
from profit_calculator import create_profit_calculator
from rule_calculator import create_rule_calculator

# Define window sizes
top_window_width = 600
top_window_height = 100
side_window_width = 300
side_window_height = 600

def main():
    dpg.create_context()

    with dpg.window(label="Main Settings", width=top_window_width, height=top_window_height, pos=(0, 0)):
        dpg.add_input_float(label="Total Capital", tag="capital", step=0.01)
        dpg.add_input_float(label="Max Accepted Risk %", tag="risk_percent", step=0.01)

    create_profit_calculator(side_window_width, side_window_height, top_window_height)
    create_rule_calculator(side_window_width, side_window_height, 300, 100)

    viewport_width = top_window_width
    viewport_height = top_window_height + side_window_height

    dpg.create_viewport(title='Tradertools.com', width=viewport_width, height=viewport_height)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()

if __name__ == "__main__":
    main()
