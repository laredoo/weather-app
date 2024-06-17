class WeatherApp {
    constructor() {
        this.container = document.querySelector('.container');
        this.searchButton = document.querySelector('.search-box button');
        this.weatherBox = document.querySelector('.weather-box');
        this.weatherDetails = document.querySelector('.weather-details');
        this.error404 = document.querySelector('.not-found');

        this.addEventListeners();
    }

    addEventListeners() {
        this.searchButton.addEventListener('click', () => this.fetchWeather());
    }

    async fetchWeather() {
        const city = document.querySelector('.search-box input').value;

        if (city === '') return;

        try {
            const response = await fetch(`http://127.0.0.1:8000/weather?city=${city}`);
            const json = await response.json();
            this.updateUI(json);
        } catch (error) {
            console.error('Error fetching weather data:', error);
        }
    }

    updateUI(data) {
        if (data.cod === '404') {
            this.showError();
            return;
        }

        this.hideError();

        const image = document.querySelector('.weather-box img');
        const temperature = document.querySelector('.weather-box .temperature');
        const description = document.querySelector('.weather-box .description');
        const humidity = document.querySelector('.weather-details .humidity span');
        const wind = document.querySelector('.weather-details .wind span');

        image.src = data.weather_icon;
        temperature.innerHTML = `${parseInt(data.weather_temperature)}<span>°C</span>`;
        description.innerHTML = `${data.weather_description}`;
        humidity.innerHTML = `${data.weather_humidity}%`;
        wind.innerHTML = `${parseInt(data.weather_wind_speed)}Km/h`;

        this.weatherBox.style.display = '';
        this.weatherDetails.style.display = '';
        this.weatherBox.classList.add('fadeIn');
        this.weatherDetails.classList.add('fadeIn');
        this.container.style.height = '590px';
    }

    showError() {
        this.container.style.height = '400px';
        this.weatherBox.style.display = 'none';
        this.weatherDetails.style.display = 'none';
        this.error404.style.display = 'block';
        this.error404.classList.add('fadeIn');
    }

    hideError() {
        this.error404.style.display = 'none';
        this.error404.classList.remove('fadeIn');
    }
}

// Initialize the app
document.addEventListener('DOMContentLoaded', () => {
    new WeatherApp();
});
