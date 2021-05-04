function darkMode() {
       document.location.reload();
}

// Source de la fonction suivante https://stackoverflow.com/a/5968306
function getCookie(name) {
    var dc = document.cookie;
    var prefix = name + "=";
    var begin = dc.indexOf("; " + prefix);
    if (begin == -1) {
        begin = dc.indexOf(prefix);
        if (begin != 0) return null;
    }
    else
    {
        begin += 2;
        var end = document.cookie.indexOf(";", begin);
        if (end == -1) {
        end = dc.length;
        }
    }
    return decodeURI(dc.substring(begin + prefix.length, end));
}
function changeThemeCookie() {
     var darkTheme = getCookie("darktheme");
     if (darkTheme == "False") {
         document.cookie = "darktheme=True"
     }
     else{
         document.cookie = "darktheme=False"
     }
}
// function hide_credits(){
//     if (document.getElementById('credits').style.display == "none") {
//         document.getElementById('credits').style.display = "flex"
//     }
//     else{
//         document.getElementById('credits').style.display = "none"
//     }
//
// }