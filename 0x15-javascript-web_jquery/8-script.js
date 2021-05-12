const url = "https://swapi-api.hbtn.io/api/films/?format=json";
jQuery.getJSON( url, (data) => {
    data['results'].forEach(element => {
        $("UL#list_movies").append(`<li>${element['title']}</li>`)
    });
});