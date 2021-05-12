$(document).ready(function() {
    function fetch_api(){
        
        const input = $('INPUT#language_code').val()
        fetch( `https://fourtonfish.com/hellosalut/?lang=${input}` )
        .then( function( response ){
            return response.json()
    } )
        .then( function( jsonData ){
            $("DIV#hello").text(jsonData['hello']); 
    } );
    }

    $("INPUT#btn_translate").click(() => {
        fetch_api();
    });

    $("INPUT#language_code").keypress((event) => {
            let keycode = (event.keyCode ? event.keyCode : event.which);
            if(keycode == '13'){
               fetch_api();
            }
        });
});
    