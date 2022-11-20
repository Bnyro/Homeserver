package main

import (
	"net/http"

	"github.com/SimpleAPI/config"
	"github.com/SimpleAPI/entities"
	"github.com/SimpleAPI/handlers"
	"github.com/labstack/echo/v4"
	"github.com/labstack/echo/v4/middleware"
)

func main() {
	config.Connect()

	e := echo.New()

	e.Use(middleware.CORS())

	e.GET("/", func(c echo.Context) error {
		return c.JSON(http.StatusOK, entities.Message{
			Message: "API online",
		})
	})
	e.GET("/events", handlers.GetEvents)
	e.POST("/events/post", handlers.CreateEvent)
	e.DELETE("/events/delete", handlers.DeleteEvent)

	e.GET("/weather/data", handlers.GetWeatherData)
	e.POST("/weather/post", handlers.CreateWeatherData)
	e.DELETE("/weather/delete", handlers.DeleteWeatherData)

	e.Logger.Fatal(e.Start(":8000"))
}
