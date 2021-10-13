const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

// alerts fadeout
setTimeout(function(){
    $('#message').fadeOut('slow');
}, 3000);