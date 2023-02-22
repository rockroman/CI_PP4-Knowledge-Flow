
let images = document.querySelectorAll('.blog_image');
for (let image of images){
  image.classList.add("card-img-top");
}

let Catimages = document.querySelectorAll('.cat_image');
for (let image of Catimages){
  image.classList.add("img-fluid");
}


$('.user_image').each(function(){
  $(this).attr('alt', ' profile image uploaded by user')
})

$('.blog_image').each(function(){
  $(this).attr('alt', ' Blog image uploaded by user')
})


$('.updateBtn').each(function(){
  $(this).on("click", function(event){
    if (event.target = this) {
    
      var par = $(event.target).parent();
  
      
      console.log(par.children('#comment-body').html());
      let oldComment= par.children('#comment-body').html();
      $('.modal-body').each(function(){ 
      $('.md-textarea').html(oldComment)
      });
      // new code 
      //end  new code 
    
    }



  });
  // working-code
  $('#comment-done').on('click', function(){
    $('.md-textarea').html('')
    $('#comment-text').html('')
    

  });

});


// detect when closing modal
$('.comment').on('hide.bs.modal', function (e) {
  console.log('modal closed');
  $('.modal-body').each(function(){
    $('.md-textarea').html('')
    // $('#com-text').html('')
   
    });
});

// dissmiss django messages
// setTimeout(function(){
//   let messages= document.getElementById('msg');
//   let alert = new bootstrap.Alert(messages);
//   alert.fadeOut('slow');

// },1500)
$('#msg').hide().fadeIn(0).delay(1500).fadeOut(1300); 

// const navlink = document.querySelectorAll(".nav-link");
// navlink.forEach(elem => elem.addEventListener("click", smoothscroll));
// function smoothscroll(event){
//   event.preventDefault();
//   const targetId = event.currentTarget.getAttribute("href");
//   window.scrollTo({
//     top: document.querySelector(targetId).offsetTop,
//     behavior: "smooth"
//   })
// }

// jQuery(document).ready(function() {

//   // Scrolling for anchor links in within the same page
//   jQuery('a[href*="#"]:not([href="#"])').click(function(){
//       _hash = this.hash;
//       _scroll_it( _hash );
//   });

//   // scrolling for anchor links coming from a different page
//   var _hash = window.location.hash;
//   if( _hash.length > 0 ){     
//       window.scrollTo(0, 0);
      
//       setTimeout( function() { 
//           _scroll_it( _hash );
//       }, 300 );       
//   }
  
//   function _scroll_it( _hash ){
//       jQuery('html,body').animate({
//           scrollTop: jQuery( _hash ).offset().top
//       }, 300 );
//   }

// });

