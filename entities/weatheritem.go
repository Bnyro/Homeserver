package entities

import "gorm.io/gorm"

type WeatherItem struct {
	gorm.Model
	Time float32     `json:"time"`
	Data WeatherData `json:"data" gorm:"foreignKey:ID"`
}
