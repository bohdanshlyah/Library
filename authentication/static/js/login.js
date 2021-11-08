
$(document).ready(function(){
    $('.login-info-box').fadeOut();
    $('.login-show').addClass('show-log-panel');

    $('#label-login').on('click',function() {
        $('#log-login-show').attr('checked', true);
        $('#log-reg-show').attr('checked', false);
        $('.register-info-box').fadeOut(); 
        $('.login-info-box').fadeIn();
        
        $('.white-panel').addClass('right-log');
        $('.register-show').addClass('show-log-panel');
        $('.login-show').removeClass('show-log-panel');
    });

    $('#label-register').on('click',function() {
        $('#log-login-show').attr('checked', false);
        $('#log-reg-show').attr('checked', true);
       
        $('.register-info-box').fadeIn();
        $('.login-info-box').fadeOut();
        
        $('.white-panel').removeClass('right-log');
        
        $('.login-show').addClass('show-log-panel');
        $('.register-show').removeClass('show-log-panel');
    });

});

// function my() {
//     $(window).load(function() {
//         $('#label-register').click();
//         alert('ho')
//     })
//     // $('#label-register').trigger('click');
    

// }

function changeClass(){
    setTimeout(function() {
        $('#label-login').trigger('click');
        
        console.log('here i am')
    }, 10)
    console.log('I worked');
}
// $(window).on('load', changeClass);
      
    