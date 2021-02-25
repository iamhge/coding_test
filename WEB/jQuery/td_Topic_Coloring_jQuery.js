function newMessage(topicName) {
  //Write your code here
  $('p[data-topic-name="'+topicName+'"]').css('background-color', 'red');
}

// Example case
$('body').html(
  `<div>
    <p data-topic-name="discussion">General discussion</p>
    <p data-topic-name="bugs">Bugs</p>
    <p data-topic-name="animals">Animals</p>
  </div>`
);
newMessage("discussion");
console.log($('body').html());