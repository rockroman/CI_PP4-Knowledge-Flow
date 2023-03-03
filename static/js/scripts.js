let images = document.querySelectorAll('.blog_image');
for (let image of images){
  image.classList.add("card-img-top");
}

let Catimages = document.querySelectorAll('.cat_image');
for (let image of Catimages){
  image.classList.add("img-fluid");
}


$('.user_image').each(function(){
  $(this).attr('alt', ' profile image uploaded by user');
});

$('.blog_image').each(function(){
  $(this).attr('alt', ' Blog image uploaded by user');
});


// code for updating comment in bootstrap modal

$('.updateBtn').each(function(){
  $(this).on("click", function(event){
   
    event.target = this;
    var par = $(this).parent();
    console.log(par.children('.comment-body').html());
    let oldComment= par.children('.comment-body').html();
    $('.modal-body').each(function(){ 
      $('.md-textarea').html(oldComment);
    });
  });


// working-code
  $('.comment-done').on('click', function(){
    $('.md-textarea').html('');
    $('#comment-text').html('');
    
  });

});


// detect when closing modal
$('.comment').on('hide.bs.modal', function (e) {
  console.log('modal closed');
  $('.modal-body').each(function(){
    $('.md-textarea').html('');
    
    });
});




 

// dissmiss django messages

$('#msg').hide().fadeIn(0).delay(1500).fadeOut(1300); 

// back to top button source  https://mdbootstrap.com/docs/standard/extended/back-to-top/
//Get the button
let mybutton = document.getElementById("btn-back-to-top");

// When the user scrolls down 300px from the top of the document, show the button
window.onscroll = function () {
  scrollFunction();
};

function scrollFunction() {
  if (
    document.body.scrollTop > 300 ||
    document.documentElement.scrollTop > 300
  ) {
    $("#btn-back-to-top").fadeIn(1200);
  } else {
    $("#btn-back-to-top").fadeOut(800);
  }
}
// When the user clicks on the button, scroll to the top of the document
mybutton.addEventListener("click", backToTop);

function backToTop() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
}





























// // code in progress

// $('.updateBtn').each(function(){
//   $(this).on("click", function(event){
   
//     event.target = this;
//     var par = $(this).parent();
//     console.log(par.children('.comment-body').html());
//     let oldComment= par.children('.comment-body').html();
//     $('.modal-body').each(function(){ 
//       $('.md-textarea').html(oldComment);
//     });
//   });


// // working-code
//   $('.comment-done').on('click', function(){
//     $('.md-textarea').html('');
//     $('#comment-text').html('');
    
//   });

// });


// $('.updateBtn').each(function(){
//   $(this).on("click", function(event){
//     if (event.target = this) {
    
//       var par = $(event.target).parent();
  
      
//       console.log(par.children('#comment-body').html());
//       let oldComment= par.children('#comment-body').html();
//       $('.modal-body').each(function(){ 
//       $('.md-textarea').html(oldComment)
//       });

//     }



//   });


// // working-code
//   $('#comment-done').on('click', function(){
//     $('.md-textarea').html('')
//     $('#comment-text').html('')
    
//   });

// });

// new  better code
// $('.updateBtn').each(function(){
//   $(this).on("click", function(event){
//     event.target = this;
//     var par = $(this).parent();
//     console.log(par.children('#comment-body').html());
//     let oldComment= par.children('#comment-body').html();
//     $('.modal-body').each(function(){ 
//       $('.md-textarea').html(oldComment);
//     });
//   });


// // working-code
//   $('#comment-done').on('click', function(){
//     $('.md-textarea').html('');
//     $('#comment-text').html('');
    
//   });



// });




 
  

