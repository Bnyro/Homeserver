let $ = document.querySelector.bind(document);
let $$ = document.querySelectorAll.bind(document);

const apiURL = 'http://192.168.178.116:443';

let sensors = {
	ds18_t: 'DS18 Temperature',
	dht_t: 'DHT22 Temperature',
	dht_h: 'DHT22 Humidity',
	bmp_t: 'BMP180 Temperature',
	bmp_p: 'BMP180 Pressure'
};
var time = [];

function timeConverter(unixTimestamp) {
	var a = new Date(unixTimestamp * 1000);
	var months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
	var year = a.getFullYear();
	var month = months[a.getMonth()];
	var date = a.getDate();
	var hour = a.getHours();
	var min = a.getMinutes();
	var sec = a.getSeconds();
	var time = date + ' ' + month + ' ' + year + ' ' + hour + ':' + min + ':' + sec;
	return time;
}

var dynamicColors = function () {
	var r = Math.floor(Math.random() * 255);
	var g = Math.floor(Math.random() * 255);
	var b = Math.floor(Math.random() * 255);
	return 'rgb(' + r + ',' + g + ',' + b + ')';
};

function createChart(ctx, label, data) {
	const color = dynamicColors();
	new Chart(ctx, {
		type: 'line',
		data: {
			labels: time.reverse(),
			datasets: [
				{
					label: label,
					data: data.reverse(),
					backgroundColor: color,
					borderColor: color,
					borderWidth: 1
				}
			]
		}
	});
}

const drawGraphs = async () => {
	const response = await fetch(apiURL + '/weather/data');
	const weatherData = await response.json();

	Object.keys(weatherData);

	var data = {};

	weatherData.forEach((obj) => {
		time.push(timeConverter(obj.time));
		Object.keys(obj.data).forEach((key) => {
			// filter out createdAt, updatedAt, modifiedAt and the id
			if (key.includes("_")) {
				data[key] = data[key] || [];
				data[key].push(obj.data[key]);
			}
		});
	});

	Object.keys(data).forEach((key, index) => {
		createChart($$('#container>canvas')[index], sensors[key], data[key]);
	});
};

drawGraphs();
