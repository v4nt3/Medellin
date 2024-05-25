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
    var titulo = data[1][1];
    var fecha = data[1][2];
    var lugar = data[1][3];
    var descripcion = data[1][4];
    document.getElementById('actividadTitulo').innerHTML = titulo;
    document.getElementById('actividadDescripcion').innerHTML = descripcion;
    document.getElementById('actividadFecha').innerHTML = fecha;
    document.getElementById('actividadLugar').innerHTML = lugar;
}