function obtenerLugares() {
    var actividades;
    console.log("obtenerLugares");
    $.ajax({
        type: "GET",
        url: "http://127.0.0.1:5000/obtenerLugares",
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
        var Lugares = data[i]
        var titulo = Lugares[1];
        var lugar = Lugares[2];
        var descripcion = Lugares[3];
        var imagen = Lugares[4]
        console.log("imagen");
        console.log(imagen);
        var item = document.createElement('div');
        item.classList.add = 'item';
        var cardColumns = document.getElementsByClassName('card-columns')[0];
        var cardContenido = `<div class="card">
            <img class="card-img-top" src="../static/imagenes/${imagen}" alt="${imagen}">
            <div class="card-body">
                <h5 class="card-title" id="LugaresTitulo">${titulo}</h5>
                <p class="card-text" id="LugaresDescripcion">${descripcion}</p>
                <p class="card-text text-muted mb-2" id="LugaresLugar">${lugar}</p>
                <!-- <p class="card-text text-muted mb-2">Auditorio Bello</p> -->
            </div>
        </div>`
        item.innerHTML = cardContenido;
        cardColumns.append(item)
    }
}