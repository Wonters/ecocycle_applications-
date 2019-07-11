

function plotRecolte(poids,mois) {
    let bode = {
        x: mois,
        y:poids,
        mode: 'markers',
        type: 'scatter',

    };
    let data=[bode];
    Plotly.newPlot('graph', data);
}

plotRecolte([1,2,3,4],[2,5,9]);