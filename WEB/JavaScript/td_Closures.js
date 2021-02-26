function registerHandlers() {
    let as = document.getElementsByTagName('a');
    // var 말고 let써야됨.
    for (let i = 0; i < as.length; i++) {
        as[i].onclick = function () {
            alert(i);
            return false;
        };
    }
}
registerHandlers();

/* HTML code for testing purposes (do not submit uncommented):
<body>
  In my life, I used the following web search engines:<br/>
  <a href="//www.yahoo.com">Yahoo!</a><br/>
  <a href="//www.altavista.com">AltaVista</a><br/>
  <a href="//www.google.com">Google</a><br/>
</body>
*/