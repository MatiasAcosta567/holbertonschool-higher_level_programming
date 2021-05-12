$(document).ready(function() {
    $("INPUT#btn_translate").click(() => {
        const input = $('INPUT#language_code').val()
        fetch( `https://fourtonfish.com/hellosalut/?lang=${input}` )
        .then( function( response ){
            return response.json()
    } )
        .then( function( jsonData ){
            $("DIV#hello").text(jsonData['hello']); 
    } );
    });
    
});