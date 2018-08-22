$(function () {
    console.log("I've connected to your javascript file!");

    //Variables
    const $unsplashForm = $('#unsplashForm');
    const $searchInput = $('#search');
    
    const url = $unsplashForm.attr('action');
    let data = null;

    //Form Submit Function
    $unsplashForm.submit(function(e) {
        e.preventDefault();
        data = $searchInput.val()
        console.log("This is what data is now, son!")
        console.log(data)
        unsplash();
    });

    //API Functions
    function unsplash() {
        $.ajax({
          url: url,
          type: 'GET',
          query_string: data,
          dataType: 'json',
          success: function(data){
            console.log('Query String: ' + data);
          },
          error : function(request,error) {
            alert("Request: " + JSON.stringify(request))
          }
        })
    }
});