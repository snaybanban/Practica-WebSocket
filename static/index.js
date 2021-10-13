document.addEventListener('DOMContentLoaded', () => {
    var socket = io.connect(location.protocol+'//' + document.domain + ':' + location.port);
    socket.on('connect', () => {

        socket.on('message', function(msg) { //la conexion del cliente a servidor.
            $('#texto-msj').append('<li>' + msg + '</li>') // insertamos el contenido de a la lista, es decir el texto-msj.
          })
      
          $('#Enviar').on('click', function() { //nuestro boton tendra la funcion al momento de clikear de mandar ese contenido a texto-msj
            socket.send($('#mi-msj').val());
            $('#mi-msj').val('');
          })
    });

});