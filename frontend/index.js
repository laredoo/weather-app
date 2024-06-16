const container = document.querySelector('.container');
const search = document.querySelector('.search-box button');
const weatherBox = document.querySelector('.weather-box');
const weatherDetails = document.querySelector('.weather-details');
const error404 = document.querySelector('.not-found');

search.addEventListener('click', () => {

    const city = document.querySelector('.search-box input').value;

    if (city === '')
        return;

    fetch(`http://127.0.0.1:8000/weather?city=${city}`)
        .then(response => response.json())
        .then(json => {
            if (json.cod === '404') {
                container.style.height = '400px';
                weatherBox.style.display = 'none';
                weatherDetails.style.display = 'none';
                error404.style.display = 'block';
                error404.classList.add('fadeIn');
                return;
            }

            error404.style.display = 'none';
            error404.classList.remove('fadeIn');

            const image = document.querySelector('.weather-box img');
            image.src = json.weather_icon
            const temperature = document.querySelector('.weather-box .temperature');
            const description = document.querySelector('.weather-box .description');
            const humidity = document.querySelector('.weather-details .humidity span');
            const wind = document.querySelector('.weather-details .wind span');

            temperature.innerHTML = `${parseInt(json.weather_temperature)}<span>°C</span>`; // temeprature
            description.innerHTML = `${json.weather_description}`; // description
            humidity.innerHTML = `${json.weather_humidity}%`; // humidity
            wind.innerHTML = `${parseInt(json.weather_wind_speed)}Km/h`; // wind speedtew

            weatherBox.style.display = '';
            weatherDetails.style.display = '';
            weatherBox.classList.add('fadeIn');
            weatherDetails.classList.add('fadeIn');
            container.style.height = '590px';


        });

});