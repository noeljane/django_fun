$(function () {
    console.log("I've connected to your javascript file!");

    //Variables
    const $form = $('#unsplashForm');
    console.log($form);

    $form.submit(function(e) {
        e.preventDefault();
        console.log("submit function is working now!")

    })


    //Function
    function unsplash() {
        $.ajax({
          url: 'https://api.unsplash.com/photos/search/?client_id=${client_id}&query=puppies&page=1',
          type: 'GET',
          data: data,
          dataType: 'json',
          success: function(data){
            console.log('Data: ' + data);
          },
          error : function(request,error) {
            alert("Request: " + JSON.stringify(request))
          }
        })
    }
});