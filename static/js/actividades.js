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
    for (let i = 0; i < data.length;i++){
        var actividad = data[i]
        var titulo = actividad[1];
        var fecha = actividad[2];
        var lugar = actividad[3];
        var descripcion = actividad[4];
        var imagen = actividad[5]
        console.log("imagen");
        console.log(imagen);
        var item = document.createElement('div');
        item.classList.add = 'item';
        var cardColumns = document.getElementsByClassName('card-columns')[0];
        var cardContenido = `<div class="card">
            <img class="card-img-top" src="../static/imagenes/${imagen}" alt="${imagen}">
            <div class="card-body">
                <h5 class="card-title" id="actividadTitulo">${titulo}</h5>
                <p class="card-text" id="actividadDescripcion">${descripcion}</p>
                <p class="card-text card-text text-muted mb-2" id="actividadFecha">${fecha}</p>
                <!-- Miercoles 9 Abril 16:00 - 18:00 -->
                <p class="card-text text-muted mb-2" id="actividadLugar">${lugar}</p>
                <!-- <p class="card-text text-muted mb-2">Auditorio Bello</p> -->
            </div>
        </div>`
        item.innerHTML = cardContenido;
        cardColumns.append(item)
    }
}