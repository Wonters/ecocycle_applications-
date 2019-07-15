function plotlyPie(datalist, legendlist) {
    var data = [{
        values: datalist,
        labels: legendlist,
        type: 'pie'
    }];

    Plotly.newPlot('pie', data, {}, {showSendToCloud: true});

}

function getWeidthLegum() {
    let list = {list};
}

function plotPlantation() {
    let inputPLantation = $('#plantation')[0];
    let plantation = JSON.parse(inputPLantation.value);
    let datalist = new Array();
    let lengendlist = new Array();
    for (let val in plantation) {
        datalist.push(plantation[val]);
        lengendlist.push(val);
    }
    plotlyPie(datalist, lengendlist);
}

function map() {
    let data = [{
        type: 'scattermapbox',
        lat: ['45.1272761'],
        lon: ['1.0938997'],
        mode: 'markers',
        marker: {
            size: 14
        },
        text: ['Etang']
    },
    {
        type: 'scattermapbox',
        lat: ['45.1278192'],
        lon: ['1.099584'],
        mode: 'markers',
        marker: {
            size: 14
        },
        text: ['AcTI']
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

plotPlantation();
map();
