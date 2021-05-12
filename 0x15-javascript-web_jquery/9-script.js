const url = "https://fourtonfish.com/hellosalut/?lang=fr"
jQuery.getJSON( url, (data) => {
    $("DIV#hello").text(data['hello']);
}); 