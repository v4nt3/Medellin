function obtenerActividades() {
    var actividades;
    console.log("obtenerActividades");
    $.ajax({
        type: "GET",
        url: "http://127.0.0.1:5000/obtenerActividades",
        // data: JSON.stringify(pedido),
        contentType: "application/json",
        dataType: 'json',
        success: function(data){
            console.log("data");
            console.log(data);
            console.log(data[1][1]);
            actividades = data
            generar_html(data);
            //window.location.href = "actividades.html";
        },
        error: function(error){
             console.log("Error:");
             console.log(error);
        }
      });

}

function generar_html(data){
    console.log("data_generar_html");
    console.log(data[1][1]);
    document.getElementById('actividadUno').innerHTML = data[1][1];
    document.getElementById('actividadFecha').innerHTML = data[1][2];
}