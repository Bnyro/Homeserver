package entities

import "gorm.io/gorm"

type WeatherItem struct {
	gorm.Model
	Time float64     `json:"time"`
	Data WeatherData `json:"data" gorm:"foreignKey:ID"`
}
