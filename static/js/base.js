let date = new Date();
let month = date.getMonth();
let year = date.getFullYear();
let day = date.getDate();
let divDate = $('.date-now');
divDate[0].innerHTML = 'Date :' + day.toString() +'/'+ month.toString() +'/'+ year.toString();