function obtenerEventos() {
    var actividades;
    console.log("obtenerEventos");
    $.ajax({
        type: "GET",
        url: "http://127.0.0.1:5000/obtenerEventos",
        contentType: "application/json",
        dataType: 'json',
        success: function(data){
            console.log("data");
            console.log(data);
            console.log(data[1][1]);
            actividades = data
            generar_html(data);
        },
        error: function(error){
             console.log("Error:");
             console.log(error);
        }
      });

}

function generar_html(data){
    for (let i = 0; i < data.length;i++){
        var actividad = data[i]
        var titulo = actividad[1];
        var descripcion = actividad[2];
        var imagen = actividad[3]
        console.log("imagen");
        console.log(imagen);
        var item = document.createElement('div');
        item.classList.add = 'item';
        var cardColumns = document.getElementsByClassName('card-columns')[0];
        var cardContenido = `<div class="card" >
            <img class="card-img-top" src="../static/imagenes/${imagen}" alt="${imagen}">
            <div class="card-body">
                <h5 class="card-title" id="actividadTitulo">${titulo}</h5>
                <p class="card-text" id="actividadDescripcion">${descripcion}</p>
            </div>
        </div>`
        item.innerHTML = cardContenido;
        cardColumns.append(item)
    }
}