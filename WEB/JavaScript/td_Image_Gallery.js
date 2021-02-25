function setup() {
    // Write your code here.
    var remove = document.getElementsByClassName("remove");

    Array.from(remove).forEach(element => {
        element.onclick = function() {
            element.parentElement.remove();
        };
    });
    
}
  
// Example case. 
document.body.innerHTML = `
<div class="image">
    <img src="https://goo.gl/kjzfbE" alt="First">
    <button class="remove">X</button>
</div>
<div class="image">
    <img src="https://goo.gl/d2JncW" alt="Second">
    <button class="remove">X</button>
</div>`;
  
setup();
  
document.getElementsByClassName("remove")[0].click();
console.log(document.body.innerHTML);