/**
 * Theme: Ubold Admin Template
 * Author: Coderthemes
 * Component: Datatable
 * 
 */
var inicializarIdioma = function(){
    "use strict"
    $('#datatable').dataTable({
        language: {
            "sProcessing":     "Procesando...",
            "sLengthMenu":     "Mostrar _MENU_ registros",
            "sZeroRecords":    "No se encontraron resultados",
            "sEmptyTable":     "Ningún dato disponible en esta tabla",
            "sInfo":           "Mostrando registros del _START_ al _END_ de un total de _TOTAL_ registros",
            "sInfoEmpty":      "Mostrando registros del 0 al 0 de un total de 0 registros",
            "sInfoFiltered":   "(filtrado de un total de _MAX_ registros)",
            "sInfoPostFix":    "",
            "sSearch":         "Buscar:",
            "sUrl":            "",
            "sInfoThousands":  ",",
            "sLoadingRecords": "Cargando...",
            "oPaginate": {
                "sFirst":    "Primero",
                "sLast":     "Último",
                "sNext":     "Siguiente",
                "sPrevious": "Anterior"
            },
            "oAria": {
                "sSortAscending":  ": Activar para ordenar la columna de manera ascendente",
                "sSortDescending": ": Activar para ordenar la columna de manera descendente"
            }
        },
        order: [[ 3, "desc" ]]
    });
    $('#datatable-keytable').DataTable({keys: true});
    $('#datatable-responsive').DataTable();
    $('#datatable-colvid').DataTable({
        "dom": 'C<"clear">lfrtip',
        "colVis": {
            "buttonText": "Change columns"
        }
    });
    $('#datatable-scroller').DataTable({
        ajax: "assets/plugins/datatables/json/scroller-demo.json",
        deferRender: true,
        scrollY: 380,
        scrollCollapse: true,
        scroller: true
    });
    var table = $('#datatable-fixed-header').DataTable({fixedHeader: true});
    var table = $('#datatable-fixed-col').DataTable({
        scrollY: "300px",
        scrollX: true,
        scrollCollapse: true,
        paging: false,
        fixedColumns: {
            leftColumns: 1,
            rightColumns: 1
        }
    });
}
TablaInicializarIdioma = function() {
    "use strict";
    return {
        init: function() {
            inicializarIdioma();
        }
    }
}();

function imprimirlista(e, obj)
{
    e.preventDefault();
    this_url = $(obj).attr('href');
    window.open(this_url,"_blank","height=500,width=700,status=no,toolbar=no,menubar=no,location=no,scrollbars=yes");
}

function imprimirdocumento(e, obj)
{
    e.preventDefault();
    this_url = $(obj).attr('href');
    window.open(this_url,"_blank","height=500,width=700,status=no,toolbar=no,menubar=no,location=no,scrollbars=yes");
    $(obj).attr('class', 'btn btn-xs btn-danger');
}

function asistencia(e, obj)
{
    e.preventDefault();
    this_url = $(obj).attr('href');
    $.ajax({
        url: this_url,
        type: 'get',
        success: function(data){
            $(obj).attr('class', 'btn btn-xs btn-danger');
            alert(data.success);
        }
    })    
    //window.open(Routing.generate('reporte_mensual_imprimir',{fecha1: fecha1, fecha2: fecha2}),"_blank","height=500,width=700,status=no,toolbar=no,menubar=no,location=no,scrollbars=yes");
}