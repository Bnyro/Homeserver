package entities

type Event struct {
	ID    uint   `gorm:"primaryKey" json:"id"`
	Title string `json:"title"`
	Start string `json:"start"`
	End   string `json:"end"`
	Color string `json:"color"`
}
