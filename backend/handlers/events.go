package handlers

import (
	"net/http"

	"github.com/SimpleAPI/config"
	"github.com/SimpleAPI/entities"
	"github.com/labstack/echo/v4"
)

func GetEvents(c echo.Context) error {
	var events []entities.Event

	config.Database.Find(&events)

	return c.JSON(http.StatusOK, &events)
}

func CreateEvent(c echo.Context) error {
	event := new(entities.Event)

	if err := c.Bind(event); err != nil {
		return c.String(http.StatusBadRequest, "Bad Request")
	}

	config.Database.Create(&event)

	return c.JSON(http.StatusCreated, event)
}

func DeleteEvent(c echo.Context) error {
	event := new(entities.Event)

	if err := c.Bind(event); err != nil {
		return c.String(http.StatusBadRequest, "Bad Request")
	}
	result := config.Database.Delete(&entities.Event{}, event.ID)

	if result.RowsAffected == 0 {
		return c.String(http.StatusBadRequest, "Bad Request")
	}

	return c.JSON(http.StatusAccepted, entities.Message{
		Message: "Deleted succesfully!",
	})
}
