

let images = document.querySelectorAll('.blog_image');
for (let image of images){
  image.classList.add("card-img-top");
}


// $(document).ready(function() {
//   $("#updatemy-{{comment.id}}").on("show.bs.modal", function(event) {
//     var button = $(event.relatedTarget);
//     var commentId = button.data("comment-id");
//     var modal = $(this);

//     $.ajax({
//       url: "{% url 'update_comment' comment.id %}",
//       data: {
//         "comment_id": commentId
//       },
//       success: function(data) {
//         modal.find(".modal-body").html(data);
//       }
//     });
//   });
// });

