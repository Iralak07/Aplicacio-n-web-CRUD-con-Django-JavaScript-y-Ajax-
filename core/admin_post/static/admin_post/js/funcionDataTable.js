var table;
document.addEventListener('DOMContentLoaded', function (){
            var csrftoken = document.getElementsByName('csrfmiddlewaretoken')[0].value
            table = $('#table_category').DataTable({
                ajax:{
                    headers: {'X-CSRFToken': csrftoken},
                    url: window.location.pathname,
                    type: 'POST',
                    data: {
                        action: 'search',
                    },
                    dataSrc: ""
                },
                columns: [
                    {"data": [0]},
                    {"data": [1]},
                    {"data": [1]},
                ],
                "columnDefs": [ 
                {
                    "targets": 2,
                    "render": function ( data, type, row ) {
                        let button = '<button rel="edit" class="btn btn-warning m-1"><i class="bi bi-pencil-square"></i></button>'
                        button += '<button rel="delete" class="btn btn-danger m-1"><i class="bi bi-x-square-fill"></i></button>'
                        return button
                    }
                } 
                ]
            })

            $('#botonActualizar').on('click', function(){
                $('#table_category').DataTable().ajax.reload();
            })

            $('#botonRegistrar').on('click', ()=>{
                $('#modalCategory').modal('show');
                $('#modalCategory form')[0].reset();
                $('input[name="action"]').val('cargar');
            });

            $('#table_category tbody').on('click', 'button[rel="edit"]', 'tr', function(){
              var tr = table.cell($(this).closest('td,li')).index().row;
              var data = table.row(tr).data();
              $('#modalCategory').modal('show');
              $('#modalCategory form')[0].reset();
              $('input[name="name"]').val(data[1]);
              $('input[name="id"]').val(data[0]);
              $('input[name="action"]').val('edit');
            });

            $('#table_category tbody').on('click', 'button[rel="delete"]', function(){
              var csrftoken = document.getElementsByName('csrfmiddlewaretoken')[0].value
              var tr = table.cell($(this).closest('td,li')).index().row;
              var data = table.row(tr).data();
              let id = data[0];
              let name = data[1];
              Swal.fire({
                title: 'Atencion!',
                text: `Estas seguro que quieres eliminar esta categoria: ${name}`,
                icon: 'warning',
                showCancelButton: true,
                confirmButtonColor: '#3085d6',
                cancelButtonColor: '#d33',
                cancelButtonText: "Cancelar",
                confirmButtonText: 'Si, eliminar!'
              }).then((result) => {
                if (result.value) {
                  $.ajax({
                    headers: {'X-CSRFToken': csrftoken},
                    url: window.location.pathname,
                    type: 'POST',
                    data: {
                      action: "delete",
                      data: id,
                    },
                  })
                  .done(function(data) {
                    if(data['error']){
                      Swal.fire({
                        icon: 'error',
                        title: 'Ha ocurrido un error',
                        text: data.error
                      })
                    }else{
                      Swal.fire({
                        position: 'top-end',
                        icon: 'success',
                        title: 'La categoria se ha eliminado exitosamente',
                        showConfirmButton: false,
                        timer: 2000
                      })
                      table.ajax.reload();
                      return false;
                  }
                  })
                  .fail(function(data) {
                    
                  })
                  .always(function(data) {
                  });
                }
              })
            });
})


function ajax_submit(url, data, csrftoken, callback){
    Swal.fire({
        title: 'Atencion!',
        text: "Deseas guardar esta categoria?",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        cancelButtonText: "Cancelar",
        confirmButtonText: 'Si, guardar!'
      }).then((result) => {
        if (result.value) {
          $.ajax({
            headers: {'X-CSRFToken': csrftoken},
            url: url,
            type: 'POST',
            data: data,
          })
          .done(function(data) {
            if(data['error']){
              Swal.fire({
                icon: 'error',
                title: 'Ha ocurrido un error',
                text: data.error
              })
            }else{
              callback()
              return false;
          }
          })
          .fail(function(data) {
            
          })
          .always(function(data) {
          });
        }
      })
}