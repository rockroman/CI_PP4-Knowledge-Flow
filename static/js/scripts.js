
let images = document.querySelectorAll('.blog_image');
for (let image of images){
  image.classList.add("card-img-top");
}

let Catimages = document.querySelectorAll('.cat_image');
for (let image of Catimages){
  image.classList.add("img-fluid");
}

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




// $('.updateBtn').on('click', function (event) {
//   if (event.target = this) {
//     // console.log('You clicked btn');
//     var par = $(event.target).parent();
//     // console.log(par);
//     // console.log(par);
    
//     console.log(par.children('#comment-body').html());
//     let oldComment= par.children('#comment-body').html();
//     $('#comment-text').html(oldComment)
//     // par.children('#comment-text').html(oldComment)
//     //  let last =par.children().last()
//     //  console.log(last);
//     //  console.log(last.children(":first-child"))
//     // last.children('.modal-body').html('nono')
//     // last.children('#comment-text').html('nono')
    
  
 
//   }
// });


// $('.updateBtn').on('click', function (event) {
//   if (event.target = this) {
    
//     var par = $(event.target).parent();

    
//     console.log(par.children('#comment-body').html());
//     let oldComment= par.children('#comment-body').html();
//     $('.modal-body').each(function(){
//     $('#comment-text').html(oldComment)
//     });
 
    
  
 
//   }
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
  // end of working code

  // new code


  //end new code
 

});





$('.comment').on('hide.bs.modal', function (e) {
  console.log('modal closed');
  $('.modal-body').each(function(){
    $('.md-textarea').html('')
   
    });
});





// detect if modal is open
// $('.comment').on('hide.bs.modal', function (e) {
//   console.log('modal closed');
//   $('.modal-body').each(function(){
//     $('.md-textarea').html('')
//     });
// });


