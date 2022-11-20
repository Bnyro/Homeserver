package handlers

import (
	"net/http"

	"github.com/SimpleAPI/config"
	"github.com/SimpleAPI/entities"
	"github.com/labstack/echo/v4"
)

func GetWeatherData(c echo.Context) error {
	var data []entities.WeatherItem

	config.Database.Find(&data)

	for index, entry := range data {
		var weatherData entities.WeatherData
		config.Database.Find(&weatherData, "id = ?", entry.ID)
		data[index].Data = weatherData
	}

	return c.JSON(http.StatusOK, data)
}

func CreateWeatherData(c echo.Context) error {
	weatherItem := new(entities.WeatherItem)

	if err := c.Bind(weatherItem); err != nil {
		return c.String(http.StatusBadRequest, "Bad Request")
	}

	config.Database.Create(&weatherItem)

	return c.JSON(http.StatusOK, weatherItem)
}

func DeleteWeatherData(c echo.Context) error {
	config.Database.Where("1 = 1").Delete(&entities.WeatherItem{})
	config.Database.Where("1 = 1").Delete(&entities.WeatherData{})

	return c.JSON(http.StatusOK, entities.Message{
		Message: "Succesfully deleted all!",
	})
}
