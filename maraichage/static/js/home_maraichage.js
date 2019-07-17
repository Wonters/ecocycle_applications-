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
function plotRecolte(){
    let inputRecolte = $('#recolte')[0];
    let recolte = JSON.parse(inputRecolte.value);
    let datalist = new Array();
    let legendList = new Array();
    for (let val in recolte){
        datalist.push(recolte[val]);
        legendList.push(val);
    }
}


plotPlantation();
