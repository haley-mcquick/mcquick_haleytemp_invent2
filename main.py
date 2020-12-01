def on_forever():
    light.graph(input.temperature(TemperatureUnit.FAHRENHEIT))
    if input.temperature(TemperatureUnit.FAHRENHEIT) < 45:
        light.set_all(color.rgb(0, 0, 255))
    elif input.temperature(TemperatureUnit.FAHRENHEIT) >= 45 and input.temperature(TemperatureUnit.FAHRENHEIT) < 65:
        light.set_all(color.rgb(0, 255, 0))
    elif input.temperature(TemperatureUnit.FAHRENHEIT) >= 65 and input.temperature(TemperatureUnit.FAHRENHEIT) < 80:
        light.set_all(color.rgb(255, 140, 0))
    else:
        light.set_all(color.rgb(255, 0, 0))
forever(on_forever)

