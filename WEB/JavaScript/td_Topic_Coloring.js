function newMessage(topicName) {
    // Write your code here
    var p = document.getElementsByTagName('p');

    Array.from(p).forEach(element => {
        if (element.getAttribute('data-topic-name') == topicName) {
            element.style.background = "red";
        }
    });
}
  
// Example case
document.body.innerHTML = `<div>
    <p data-topic-name="discussion">General discussion</p>
    <p data-topic-name="bugs">Bugs</p>
    <p data-topic-name="animals">Animals</p>
</div>`;
newMessage("discussion");
console.log(document.body.innerHTML);