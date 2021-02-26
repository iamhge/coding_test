function createProductCodeForm(parent) {
    var form = $("<form/>");
  
    form.append($("<label>").text('Product Code:'));
    form.append($("<input>").attr('name', 'productCode').attr('type', 'text'));
    form.append($("<label>").attr('name', 'hint').text('The product code can be found on the label.'));
  
    form.append('<br>');
  
    form.append($("<input>").attr('type', 'submit'));
  
    parent.append(form);
    $('label[name="hint"]').css("display", "none");
    $("input").blur(function(){
        $('label[name="hint"]').css("display", "none");
    });
    $("input").bind('focus', function(){
        $('label[name="hint"]').css("display", "inline");
    });
}


$('body').html(
    `<div id="hi">
    </div>`
);

createProductCodeForm($('#hi'))