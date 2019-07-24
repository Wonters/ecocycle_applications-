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

function plotRecolte() {
    let inputRecolte = $('#recolte')[0];
    let recolte = JSON.parse(inputRecolte.value);
    let datalist = new Array();
    let legendList = new Array();
    for (let val in recolte) {
        datalist.push(recolte[val]);
        legendList.push(val);
    }
}

// listLegum = [['nom1','nom2','nom3','nom4','','',''],]
// nombre de plant à cuillir

function getcalendar() {
    let inputdata = document.querySelector('#calendardata');
    let calendar = inputdata.value;
    calendar = JSON.parse(calendar);
    return calendar;
}
function plotCalendarRecolte(calendar) {
    var values = calendar;
    var data = [{
        type: 'table',
        header: {
            values: [["<b>Legumes</b>"],["<b>Janvier</b>"], ["<b>Fevrier</b>"], ["<b>Mars</b>"], ["<b>Avril</b>"], ["<b>Mai</b>"], ["<b>Juin</b>"],
                ["<b>Juillet</b>"], ["<b>Août</b>"], ["<b>Septembre</b>"], ["<b>Octobre</b>"], ["<b>Novembre</b>"], ["<b>Decembre</b>"]],
            align: "center",
            line: {width: 1, color: 'black'},
            fill: {color: "grey"},
            font: {family: "Arial", size: 12, color: "white"}
        },
        cells: {
            values: values,
            align: "center",
            line: {color: "black", width: 1},
            font: {family: "Arial", size: 11, color: ["black"]}
        }
    }]

    Plotly.plot('calendar', data);
}


plotPlantation();
plotCalendarRecolte(getcalendar());


