
let images = document.querySelectorAll('.blog_image');
for (let image of images){
  image.classList.add("card-img-top");
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

// $(document).ready(function(){


//   $('.treeDots').click(function(){
//     let serializedData = 
//     $('#comment-body').html();
//     console.log(serializedData);

//     $('#comment-text').html(serializedData);
    

   

    
    
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
  $('#comment-done').on('click', function(){
    $('.md-textarea').html('')
    

  })

});

// $('.go-back').each(function(){

//   $(this).on('click', function(event){
//     if(event.target = this){
//       $('.md-textarea').html('');

//     }
  
  
//   });

// });




