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
    if ($(this).scrollTop() >= 1000) {
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

































  //   start hover submenu
  // $(".dropdown1").hover(
  //   function () {
  //     $(this)
  //       .find(".dropdown-content")
  //       .stop(true, true)
  //       .delay(200)
  //       .fadeIn(200);
  //   },
  //   function () {
  //     $(this)
  //       .find(".dropdown-content")
  //       .stop(true, true)
  //       .delay(300)
  //       .fadeOut(500);
  //   }
  // );
  //    sacond sub menu
  // $(".btn-2").hover(
  //   function () {
  //     $(this)
  //       .find(".drop-con")
  //       .stop(true, true)
  //       .delay(200)
  //       .fadeIn(200);
  //   },
  //   function () {
  //     $(this)
  //       .find(".drop-con")
  //       .stop(true, true)
  //       .delay(200)
  //       .fadeOut(500);
  //   }
  // );

  //  end hover submenu

  //    click menu in medi
  // $(function () {
  //   // DOM ready
  //   if ($(window).width() < 798) {
  //     // If a link has a dropdown, add sub menu toggle.
  //     $(".dropdown1:not(:only-child)").click(function (e) {
  //       $(this)
  //         .siblings(".dropdown-content")
  //         .toggle();
  //       // Close one dropdown when selecting another
  //       $(".dropdown-content")
  //         .not($(this).siblings())
  //         .hide();
  //       e.stopPropagation();
  //     });
  //   } else {
  //     $(".dropdown1").hover(function (e) {
  //       $(this)
  //         .siblings(".dropdown-content")
  //         .toggle();
  //       // Close one dropdown when selecting another
  //       $(".dropdown-content")
  //         .not($(this).siblings())
  //         .hide();
  //       e.stopPropagation();
  //     });
  //   }
  //   // Clicking away from dropdown will remove the dropdown class
  //   $("html").click(function () {
  //     $(".dropdown-content").hide();
  //   });
  // }); // end DOM ready
  // $(function () {
  //   // DOM ready
  //   if ($(window).width() < 798) {
  //     // If a link has a dropdown, add sub menu toggle.
  //     $(".btn-2:not(:only-child)").click(function (e) {
  //       $(this)
  //         .siblings(".drop-con")
  //         .toggle();
  //       // Close one dropdown when selecting another
  //       $(".drop-con")
  //         .not($(this).siblings())
  //         .hide();
  //       e.stopPropagation();
  //     });
  //   } else {
  //     $(".btn-2").hover(function (e) {
  //       $(this)
  //         .siblings(".drop-con")
  //         .toggle();
  //       // Close one dropdown when selecting another
  //       $(".drop-con")
  //         .not($(this).siblings())
  //         .hide();
  //       e.stopPropagation();
  //     });
  //   }
  //   // Clicking away from dropdown will remove the dropdown class
  //   $("html").click(function () {
  //     $(".drop-con").hide();
  //   });
  // }); // end DOM ready

  // //  end ckick menu inmedia

  // //   style header boxShadow when  the scroll == 1000
  // //  start open and close menu

  // $(".open").click(function () {
  //   var link = document.querySelector(".links");
  //   link.classList.toggle("translateY");
  // });

  //  Start Slider-modrenproduct
  // $(".slide-modrenproduct").owlCarousel({
  //   rtl: true,
  //   loop: true,
  //   nav: false,
  //   dots: true,
  //   autoplay: true,
  //   autoplayTimeout: 5000,
  //   animateOut: "fadeOut",
  //   dotsEach: true,
  //   center: true,
  //   margin: 30,
  //   responsive: {
  //     0: {
  //       items: 1
  //     },
  //     500: {
  //       items: 1
  //     },
  //     600: {
  //       items: 2
  //     },
  //     1000: {
  //       items: 4
  //     }
  //   }
  // });
  //  End Slider

  //  Start Slider-view-prodcut
  // $(".slide-view-prodcut").owlCarousel({
  //   rtl: true,
  //   loop: true,
  //   nav: false,
  //   dots: false,
  //   autoplay: true,
  //   autoplayTimeout: 5000,
  //   animateOut: "fadeOut",
  //   dotsEach: true,
  //   center: true,
  //   margin: 30,
  //   responsive: {
  //     0: {
  //       items: 1
  //     },
  //     500: {
  //       items: 1
  //     },
  //     600: {
  //       items: 2
  //     },
  //     1000: {
  //       items: 4
  //     }
  //   }
  // });
  //  End Slider

  //  start slide-image
  // $(".slide-image").owlCarousel({
  //   rtl: true,
  //   mouseDrag: true,
  //   loop: true,
  //   nav: false,
  //   dots: false,
  //   autoplay: true,
  //   autoplayTimeout: 5000,
  //   animateOut: "fadeOut",
  //   animateIn: "pulse",
  //   dotsEach: true,
  //   center: true,
  //   autoWidth: false,
  //   responsive: {
  //     0: {
  //       items: 1
  //     },
  //     600: {
  //       items: 1
  //     },
  //     1000: {
  //       items: 1
  //     }
  //   }
  // });
  //  end slide-image

  //  start show and hide password

  // var showpass1 = $(".showpass1"),
  //   pass1 = document.getElementById("pass1"),
  //   pass2 = document.getElementById("pass2");
  // $(".showpass1").click(function () {
  //   //  if we click button change attrbite input to text
  //   if (pass1.getAttribute("type") === "password") {
  //     //  then change attribue
  //     pass1.setAttribute("type", "text");

  //     //  hide button show and show button hide
  //     $(this).hide();
  //     $(".not-show1").show();
  //     $(".not-show1").click(function () {
  //       //  setattrbite password
  //       pass1.setAttribute("type", "password");
  //       $(this).hide();
  //       $(".showpass1").show();
  //     });
  //   } else {
  //     pass1.setAttribute("type", "password");
  //   }
  // });

  //   $(".showpass2").click(function () {
  //     //  if we click button change attrbite input to text
  //     if (pass2.getAttribute("type") === "password") {
  //       //  then change attribue
  //       pass2.setAttribute("type", "text");

  //       //  hide button show and show button hide
  //       $(this).hide();
  //       $(".not-show2").show();
  //       $(".not-show2").click(function () {
  //         //  setattrbite password
  //         pass2.setAttribute("type", "password");
  //         $(this).hide();
  //         $(".showpass2").show();
  //       });
  //     } else {
  //       pass2.setAttribute("type", "password");
  //     }
  //   });
  //   //  end show and hide password
  //   //  start sarch form

  //   //  show password form login
  //   $(".showpass1").click(function () {
  //     //  if we click if input attrbite = password
  //     if ($("#pass1").getAttribute("type") === "password") {
  //       // then change attribut to text
  //       $("#pass1").setAttribute("type", "text");

  //       // hide icon show password
  //       $(this).hide();
  //       //  show icon no-show password
  //       $(".not-show1").show();

  //       // if we click icon no-show password then input pass to change
  //       $(".not-show1").click(function () {
  //         // set attribut password
  //         $("#pass1").setAttribute("type", "password");

  //         // if click then no-show icon to hide
  //         $(".not-show1").hide();
  //         // and show icon show password
  //         $(".showpass1").show();
  //       });
  //     } else {
  //       // else set atrribut password
  //       $("#pass1").setAttribute("type", "password");
  //     }
  //   });
  //   // end show password logign
  // 
});
