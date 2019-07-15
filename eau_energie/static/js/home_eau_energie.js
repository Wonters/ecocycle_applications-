function map() {
    let data = [{
        type: 'scattermapbox',
        lat: ['45.1272548'],
        lon: ['1.0993822'],
        mode: 'markers',
        marker: {
            size: 14
        },
        text: ['Réserve nord']
    },
    {
        type: 'scattermapbox',
        lat: ['45.127322'],
        lon: ['1.0995009'],
        mode: 'markers',
        marker: {
            size: 14
        },
        text: ['Réserve sud']
    },
    {
        type: 'scattermapbox',
        lat: ['45.1272931'],
        lon: ['1.0995344'],
        mode: 'markers',
        marker: {
            size: 14
        },
        text: ['Ballon Sud']
    },
    {
        type: 'scattermapbox',
        lat: ['45.1273456'],
        lon: ['1.09958'],
        mode: 'markers',
        marker: {
            size: 14
        },
        text: ['Chaudière']
    }];

    let layout = {
        autosize: true,
        hovermode: 'closest',
        mapbox: {
            bearing: 0,
            center: {
                lat: 45.1274258,
                lon: 1.0992233,
            },
            pitch: 0,
            zoom: 15,
            style:'satellite',
        },
    };

    Plotly.setPlotConfig({
        mapboxAccessToken: 'pk.eyJ1IjoiZXRwaW5hcmQiLCJhIjoiY2luMHIzdHE0MGFxNXVubTRxczZ2YmUxaCJ9.hwWZful0U2CQxit4ItNsiQ'
    });

    Plotly.plot('maps', data, layout, {showSendToCloud: true});
}

map();
