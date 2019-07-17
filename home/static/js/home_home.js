function map() {
    let data = [{
        type: 'scattermapbox',
        lat: ['45.1272761'],
        lon: ['1.0938997'],
        mode: 'markers',
        marker: {
            size: 14
        },
        text: ['Etang'],
        name : 'Etang',
    },
    {
        type: 'scattermapbox',
        lat: ['45.1272400'],
        lon: ['1.0945457'],
        mode: 'markers',
        marker: {
            size: 14
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
            size: 14
        },
        text: ['Agroforesterie'],
         name:'Agroforesterie',
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
        lon: ['1.0999063'],
        mode: 'markers',
        marker: {
            size: 14
        },
        text: ['Tiers lieu AcTI'],
        name: 'AcTI',
    }];

    let layout = {
        autosize: true,
        hovermode: 'closest',
        mapbox: {
            bearing: 0,
            center: {
                lat: 45.1272590,
                lon: 1.0934328,
            },
            pitch: 0,
            zoom: 14,
            style:'satellite',
        },
    };

    Plotly.setPlotConfig({
        mapboxAccessToken: 'pk.eyJ1IjoiZXRwaW5hcmQiLCJhIjoiY2luMHIzdHE0MGFxNXVubTRxczZ2YmUxaCJ9.hwWZful0U2CQxit4ItNsiQ'
    });

    Plotly.plot('maps', data, layout, {showSendToCloud: true});
}


map();
