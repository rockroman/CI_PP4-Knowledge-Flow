
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

$(document).ready(function(){


  $('.treeDots').click(function(){
    let serializedData = 
    $('#comment-body').html();
    console.log(serializedData);

    $('#comment-text').html(serializedData);
    

   

    
    
  });
});


// $('.comment-cont').on('click', function (event) {
//   if (event.target = this) {
//     console.log('You clicked a container');
//     // var par = $(event.target).parent();
//     // console.log(par);
    

 
//   }
// });
