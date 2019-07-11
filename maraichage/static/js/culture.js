
function deleteLegume() {

    let hLegume = document.querySelector('.nomLegume');
    let name_LegtoDel = hLegume.innerText;
    $.ajax({
            url: '/maraichage/delete',
            type: 'GET',
            data: {name: name_LegtoDel },
            success: function (data) {
                alert('success');
            },

            error: function () {
                alert('error ajax');
            }

        }
    );
    console.log('ajax done');

}




