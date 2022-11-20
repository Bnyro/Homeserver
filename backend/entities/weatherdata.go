package entities

import "gorm.io/gorm"

type WeatherData struct {
	gorm.Model
	Ds18_t float32 `json:"ds18_t"`
	Dht_t  float32 `json:"dht_t"`
	Dht_h  float32 `json:"dht_h"`
	Bmp_t  float32 `json:"bmp_t"`
	Bmp_p  float32 `json:"bmp_p"`
}
