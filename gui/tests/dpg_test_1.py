import dearpygui.dearpygui as dpg
import math

dpg.create_context()

def update_plot(sender, app_data):
    amplitude = dpg.get_value("amplitude_slider")
    x = [i * 0.1 for i in range(100)]
    y = [amplitude * math.sin(i) for i in x]
    dpg.set_value("sine_series", [x, y])

with dpg.window(label="Sine Wave Graph", width=600, height=400):
    dpg.add_slider_float(label="Amplitude", min_value=0.1, max_value=2.0, default_value=1.0, 
                         callback=update_plot, tag="amplitude_slider")
    with dpg.plot(label="Sine Wave", height=-1, width=-1):
        dpg.add_plot_legend()
        dpg.add_plot_axis(dpg.mvXAxis, label="X")
        dpg.add_plot_axis(dpg.mvYAxis, label="Y", tag="y_axis")
        
        # Initial sine wave data
        x_initial = [i * 0.1 for i in range(100)]
        y_initial = [math.sin(i) for i in x_initial]
        dpg.add_line_series(x_initial, y_initial, label="Sine Wave", parent="y_axis", tag="sine_series")

    

dpg.create_viewport(title="Sine Wave Graph", width=620, height=480)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()