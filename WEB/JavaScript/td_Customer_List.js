// 못 풂
function showCustomers(customers, targetList) {
    // Your code goes here
    var ul = document.getElementById("customers");
    var text = "";
    
    for(let i = 0; i < customers.length ; i++) {
        text += "<li><p>" + customers[i].name + "</p></li>";
    }
    ul.innerHTML += text;

    let p = document.querySelectorAll('li > p');
    
    for (let i = 0; i < customers.length; i++) {
        p[i].onclick = function() {
            if (p[i].parentElement.childNodes.length == 1) {
                var email = "<p>" + customers[i].email + "</p>";
                p[i].parentElement.innerHTML += email;
            }
            else {
                p[i].nextSibling.remove();
            }
        }
    }
}

document.body.innerHTML = `
  <div>
    <ul id="customers">
    </ul>
  </div>
  `;
let customers = [{ name: "John", email: "john@example.com" },
{ name: "Mary", email: "mary@example.com" }];
showCustomers(customers, document.getElementById("customers"));

let customerParagraph = document.querySelectorAll("li > p")[0];
if (customerParagraph) {
    customerParagraph.click();
}
console.log(document.body.innerHTML);