//  start load page

window.onload = function () {
  document.getElementById('loader').style.display = "none";
}

//  end load page

$(document).ready(function () {


  //  markdown
  // $(".content-markdown").each(function () {
  //   let content = $(this).text();
  //   let contentMark = marked(content);
  //   $(this).html(contentMark);
  // });
  $(".content-markdown img").each(function () {

    $(this).addClass("embed-responsive");
  });
  //  set preview
  let title = $("#id_title");
  let content = $("#wmd-input-id_content");
  // let image = $("#id_image");
  // console.log(image.val());
  // $("#preview-title").text(title.val());
  // $("#preview-content").html(marked(content.val()));
  function setTitle(value) {
    $("#preview-title").text(value);

  };
  setTitle(title.val());
  title.keyup(function () {
    var newTitle = $(this).val()
    setTitle(newTitle)
  });

  function setContent(value) {
    if (value) {
      var markContent = marked(value)
      $("#preview-content").html(markContent);
    }
    $("#preview-content img").each(function () {

      $(this).addClass("embed-responsive");
    });
  };
  setContent(content.val());
  content.keyup(function () {
    var newContent = $(this).val()
    setContent(newContent)
  });



  // document.getElementById("id_image").onChange = function (evt) {
  //   var tgt = evt.target || window.event.srcElement;
  //   var files = tgt.files;
  //   if (FileReader && files && files.length) {
  //     var fr = new FileReader();
  //     console.log("=====", fr.result);
  //     // fr.onload = function () {
  //     //   document.getElementById("img").src = fr.result;

  //     // }
  //     fr.readAsDataURL(files[0])
  //   }
  // };



  // image.keyup(function () {
  //   var newContent = $(this).val()
  //   setImage(newContent)
  // });


  // style header boxShadow when  the scroll == 1000

  var header = $("header");

  $(window).scroll(function () {
    if ($(this).scrollTop() >= 1500) {
      $(header).addClass("fixed-top box-shadow");
    } else {
      $(header).removeClass("fixed-top box-shadow");
    }
  });


  //  comment and reply

  $(document).on('click', ".comment-reply-btn-thread", function (event) {
    event.preventDefault();
    $(".comment-reply").fadeToggle();
    //$(this).parent().next(".comment-reply").fadeToggle();
  });

  $(document).on('click', ".comment-reply-btn", function (event) {
    event.preventDefault();
    $(this).parent().next(".comment-reply").fadeToggle();
  });


  // setTimeout(function () {
  //   $('.mmm').fadeOut();
  // }, 15000);

  //  end comment and reply

  //  end block java scripts





  // $('.summernote').summernote({
  //   code: true,
  //   airMode: true,
  //   fontNames: ['Arial', 'Arial Black', 'Comic Sans MS', 'Courier New'],
  //   spellCheck: true,

  // });

  // var code = $('#summernote').code();
  // var newCode = $('<div dir="ltr"></div>').append(code)
  //   .find('iframe').wrap('<div class="flex-video"/>').end()
  //   .find('img').removeAttr('style').end()
  //   .html();






});
