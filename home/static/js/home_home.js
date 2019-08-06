src="/static/webcomponentsjs/webcomponents-lite.js";

function map() {
    let data = [{
        type: 'scattermapbox',
        lat: ['45.1272761'],
        lon: ['1.0938997'],
        mode: 'markers',
        marker: {
            size: 14,
            color: 'rgb(30,144,255)',
        },
        text: ['Etang'],
        name: 'Etang',
    },
        {
            type: 'scattermapbox',
            lat: ['45.1272400'],
            lon: ['1.0945457'],
            mode: 'markers',
            marker: {
                size: 14,
                color: 'rgb(62, 195, 40)',
            },
            text: ['Mandala'],
            name: 'Mandala',
        },
        {
            type: 'scattermapbox',
            lat: ['45.12810'],
            lon: ['1.102022'],
            mode: 'markers',
            marker: {
                size: 20,
                color: 'rgb(62, 195, 40)',
            },
            text: ['Agroforesterie'],
            name: 'Agroforesterie',
        },
        {
            type: 'scattermapbox',
            lat: ['45.1273607'],
            lon: ['1.0994017'],
            mode: 'markers',
            marker: {
                size: 14
            },
            text: ['Gîte&Hôtes'],
            name: 'Gîte&Hôtes',

        },
        {
            type: 'scattermapbox',
            lat: ['45.1277595'],
            lon: ['1.0996063'],
            mode: 'markers',
            marker: {
                size: 14,
                color: 'rgb(40, 187, 195)',
            },
            text: ['Tiers lieu AcTI'],
            name: 'AcTI',
        },
        {
            type: 'scattermapbox',
            lat: ['45.1269695'],
            lon: ['1.0993063'],
            mode: 'markers',
            marker: {
                size: 14,
                color: 'rgb(30,144,255)',
            },
            text: ['Bassin de baignade'],
            name: 'Bassin de baignade',
        },
        {
            type: 'scattermapbox',
            lat: ['45.1280695'],
            lon: ['1.0996563'],
            mode: 'markers',
            marker: {
                size: 14,
                color: 'rgb(210,105,30)',
            },
            text: ['scierie'],
            name: 'scierie',
        }
    ];

    let layout = {
        autosize: true,
        hovermode: 'closest',
        mapbox: {
            bearing: 0,
            center: {
                lat: 45.1272590,
                lon: 1.0980328,
            },
            pitch: 0,
            zoom: 14,
            style: 'satellite',
        },
    };

    Plotly.setPlotConfig({
        mapboxAccessToken: 'pk.eyJ1IjoiZXRwaW5hcmQiLCJhIjoiY2luMHIzdHE0MGFxNXVubTRxczZ2YmUxaCJ9.hwWZful0U2CQxit4ItNsiQ'
    });

    Plotly.plot('maps', data, layout, {showSendToCloud: true});
}


function event() {
    let listevent = [
            {title: 'event1', start:'2019-12-03' , end:''},
            {title: 'event2', start: moment().add(2, 'day')},
            {
                title: 'event3',
                start: moment().add(4, 'days'),
                end: moment().add(5, 'days')
            },
            {
                title: 'event4',
                start: moment().add(7, 'days'),
                end: moment().add(7, 'days').add(25, 'minutes')
            }
        ]
 return listevent
}

function calendar() {
    var app = document.querySelector('#app');
    app.options = {
        header: false,
        events: event(),
    };
    
    app.addEventListener('dom-change', function () {
        var calendar = Polymer.dom(document).querySelector('fullcalendar-calendar');
        var notification = Polymer.dom(document).querySelector('paper-toast');

        app.changeView = function (event) {
            calendar.changeView(event.target.attributes.getNamedItem('view').value);
        };

        app.previous = function () {
            calendar.previous();
        };

        app.next = function () {
            calendar.next();
        };

        app.notifyDayClick = function (event) {
            notification.setAttribute('text', 'You clicked on: ' + event.detail.date.format());
            notification.open();
        };

        app.setTitle = function (event) {
            this.title = event.detail.view.title;
        };
    
        calendar.addEvent({
                       title: 'dynamic event',
                       start: new Date(dateStr + 'T00:00:00'),
                       allDay: true
                       });
    });

}

calendar();

map();
