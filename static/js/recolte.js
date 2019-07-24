function plotRecolte(poids, mois, legum) {
    let bode = {
        x: mois,
        y: poids,
        mode: 'markers',
        type: 'scatter',

    };
    let data = [bode];
    var layout = {
        title: 'recolte ' + legum,
        showlegend: false
    };

    Plotly.newPlot('graph', data, layout, {scrollZoom: true});
}

function getRecolte(legum) {
    let inputrecolte = $('#inputrecolte')[0];
    let recolte = JSON.parse(inputrecolte.value);
    let recolteLegum = recolte[legum];
    let listpoid = [];
    let listmonth = [];
    let listtotale = {};
    if (legum !== 'total') {
        for (let date in recolteLegum) {
            listpoid.push(recolteLegum[date]);
            let dateformat = date.substr(0, 9);
            listmonth.push(dateformat);
        }
        plotRecolte(listpoid, listmonth, legum);
    } else {
        for (let legum in recolte) {   // initialisation
            for (let date in recolte[legum]) {
                listtotale[date.substr(0, 9)] = 0;
            }
        }
        for (let legum in recolte) { // total de recolte par jour
            for (let date in recolte[legum]) {
                listtotale[date.substr(0, 9)] = listtotale[date.substr(0, 9)] + recolte[legum][date];
            }
        }
        for (let date in listtotale) { // formate les données en list
            listpoid.push(listtotale[date]);
            listmonth.push(date);
        }

        plotRecolte(listpoid, listmonth, 'total');
    }
}

getRecolte();
