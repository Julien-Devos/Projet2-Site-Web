function switchTheme() {
    changeThemeCookie();

    var theme_style = document.getElementsByTagName("link")[0];
    let figure_pages = ['figure1','figure2','figure3','figure4','figure5']

    // If the current page is a graph reload the page to show colors correctly
    if (figure_pages.includes(window.location.href.slice(-7))) {
        location.reload()
    }
    else if (theme_style.getAttribute('href') === "/static/styles/light_theme.css") {
        theme_style.setAttribute('href', '/static/styles/dark_theme.css')
    }
    else {
        theme_style.setAttribute('href', '/static/styles/light_theme.css')
    }
}

// Source de la fonction suivante https://stackoverflow.com/a/5968306
function getCookie(name) {
    var dc = document.cookie;
    var prefix = name + "=";
    var begin = dc.indexOf("; " + prefix);
    if (begin === -1) {
        begin = dc.indexOf(prefix);
        if (begin !== 0) return null;
    }
    else
    {
        begin += 2;
        var end = document.cookie.indexOf(";", begin);
        if (end === -1) {
        end = dc.length;
        }
    }
    return decodeURI(dc.substring(begin + prefix.length, end));
}
function changeThemeCookie() {
     var darkTheme = getCookie("darktheme");
     if (darkTheme === "True") {
         document.cookie = "darktheme=False"
     }
     else{
         document.cookie = "darktheme=True"
     }
}
function stopScroll() {
    if (document.body.style.overflow === "hidden"){
        document.body.style.overflow = "visible"
    }
    else {
        document.body.style.overflow = "hidden"
    }
}