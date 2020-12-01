forever(function on_forever() {
    light.graph(input.temperature(TemperatureUnit.Fahrenheit))
    if (input.temperature(TemperatureUnit.Fahrenheit) < 45) {
        light.setAll(color.rgb(0, 0, 255))
    } else if (input.temperature(TemperatureUnit.Fahrenheit) >= 45 && input.temperature(TemperatureUnit.Fahrenheit) < 65) {
        light.setAll(color.rgb(0, 255, 0))
    } else if (input.temperature(TemperatureUnit.Fahrenheit) >= 65 && input.temperature(TemperatureUnit.Fahrenheit) < 80) {
        light.setAll(color.rgb(255, 140, 0))
    } else {
        light.setAll(color.rgb(255, 0, 0))
    }
    
})
