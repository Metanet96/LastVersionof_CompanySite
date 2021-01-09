
    const API_OPERATORS_URL = '/operations/';
    const CSRF = $('meta[name="csrf"]').attr('content');


    $.ajaxSetup({
        beforeSend: function (xhr, settings){
            xhr.setRequestHeader("X-CSRFToken", CSRF);
        }
    });



    function deleteRecoverRow(event){
            const pk = this.dataset.pk;
    console.log(pk)

            let confirm = window.confirm('ARE YOU SURE?');

            if (confirm) {
                $.ajax( {
                    url: API_OPERATORS_URL,
                    method: 'post',
                    dataType: 'json',
                    data: { key:'delete_staff', pk: pk }
                }).done(function(response){
                    loadData();
                }).fail(function(response){
                    window.alert('SOMETHING IS WRONG?!');
                });
            }

    }

    function openUpdateModal() {
        const pk = this.dataset.pk;

        $.ajax({
            url: API_OPERATORS_URL + '?key=get_staff',
            method: 'post',
            dataType: 'json',
            data: {key: 'get_staff', pk: pk}
        }).done(function (response){
            $('#update-staff-pk').val(response.pk);
//            console.log(response.pk);
            $('#update-staff-name').val(response.name);
            $('#update-staff-short_name').val(response.short_name);
            $('#update-staff-branch').val(response.branch);
            $('#staffUpdateModal').modal('show');
        }).fail(function(response){
            window.alert('Something went wrong');
        })
    }

        function loadData() {
        let tbody = $('table tbody');
        tbody.html("<tr><td colspan='4'><div class='spinner-border text-warning' style='margin-left:210px'></div>  Please wait for results...</td></tr>");
        $.ajax({
            url: API_OPERATORS_URL,
            method: 'post',
            dataType: 'json',
            data: {key: 'load_staff_list'},
        }).done(function(response){
            setTimeout( function(){
                tbody.html('');
                response.map(stf =>{

                let TR = document.createElement('tr');

                {
                    let TD = document.createElement('td');
                    TD.innerText = stf.pk;
                    TR.appendChild(TD);
                }

                {
                    let TD = document.createElement('td');
                    TD.innerText = stf.branch;
                    TR.appendChild(TD);
                }

                {
                    let TD = document.createElement('td');
                    TD.innerText = stf.name;
                    TR.appendChild(TD);
                }

                {
                    let TD = document.createElement('td');
                    let UPDATE_BUTTON = document.createElement('button');
                    UPDATE_BUTTON.setAttribute('data-pk',stf.pk);
                    UPDATE_BUTTON.setAttribute('class','btn btn-sm btn-warning');
                    UPDATE_BUTTON.innerText = 'UPD';
                    UPDATE_BUTTON.onclick = openUpdateModal;
                    TD.appendChild(UPDATE_BUTTON);

                    let DELETE_BUTTON = document.createElement('button');
                    DELETE_BUTTON.setAttribute('data-pk',stf.pk);
                    DELETE_BUTTON.setAttribute('class','btn btn-sm btn-danger delete');
                    DELETE_BUTTON.innerText = 'DLT';
                    DELETE_BUTTON.onclick = deleteRecoverRow;
                    TD.appendChild(DELETE_BUTTON);

                    TR.appendChild(TD);
                }

                tbody.append(TR);

                });
            }, 1500);
        })
    }

    $('#staffModal').on('hidden.bs.modal',function(event){
        window.alert('Staff Modal Closed');
    });

    $('#add-staff-submit').click(function(event){
        const name = $('#add-staff-name').val();
        const short_name = $('#add-staff-short_name').val();
        const branch = $('#add-staff-branch').val();

        if(!name || !short_name || !branch){
            alert('Please fill all fields!');

            let inputs = document.querySelectorAll('#staffModal input');

            inputs.forEach(input=>{
                if(!input.value){
                    input.style.borderColor = 'red';
                } else{
                    input.style.borderColor = 'green';
                }
            });

        }

        $.ajax({
            url: API_OPERATORS_URL,
            method: 'post',
            dataType: 'json',
            data: {
                key: 'add_staff',
                name: name,
                short_name: short_name,
                branch: branch,
            }
        }).done(function(response){
            window.alert(response.details);
            $('#staffModal input').val('');
            $('#staffModal').modal('hide');
            loadData();
        }).fail(function(response){
            window.alert(response.responseJSON.details);
        });
    });






    $('#staffUpdateModal').on('hidden.bs.modal',function(event){
        window.alert('Staff Modal Closed');
    });


    $('#update-staff-submit').click(function(event){
        const pk = $('#update-staff-pk').val();
        const name = $('#update-staff-name').val();
        const short_name = $('#update-staff-short_name').val();
        const branch = $('#update-staff-branch').val();

        let confirm = window.confirm('ARE YOU SURE?');

        if(!name || !short_name || !branch) {
            alert('Please fill all fields!');

            let inputs = document.querySelectorAll('#staffUpdateModal input');

            inputs.forEach(input=>{
                if(!input.value){
                    input.style.borderColor = 'red';
                } else{
                    input.style.borderColor = 'green';
                }
            });
        }

        if (confirm) {
            if (pk && name && short_name && branch){
                $.ajax( {
                    url: API_OPERATORS_URL + '?key=update_staff',
                    method: 'post',
                    dataType: 'json',
                    data: {
                     key:'update_staff',
                     pk: pk ,
                     name: name,
                     short_name: short_name,
                     branch: branch,
                   }
                }).done(function(response){
                     window.alert(response.details);
                     $('#staffUpdateModal input').val('');
                     $('#staffUpdateModal').modal('hide');
                     loadData();
                }).fail(function(response){
                    window.alert(response.responseJSON.details);
                });
            }

        }
     })


loadData();