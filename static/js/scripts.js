
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



// $(document).ready(function(){


//   $('#commentButton').click(function(){
//     let serializedData = 
//     $('#comment_form').serialize();

//     $.ajax({
//       url: $('#comment_form').data('url'),
//       data: serializedData,
//       type: 'POST'
//     })
    
//   });
// });


$('.updateBtn').each(function(){
  $(this).on("click", function(event){
    if (event.target = this) {
    
      var par = $(event.target).parent();
  
      
      console.log(par.children('#comment-body').html());
      let oldComment= par.children('#comment-body').html();
      $('.modal-body').each(function(){ 
      $('.md-textarea').html(oldComment)
      }); 
    
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
   
    });
});

