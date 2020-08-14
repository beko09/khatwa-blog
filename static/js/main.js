//  start load page

window.onload = function () {
  document.getElementById('loader').style.display = "none";
}

//  end load page

$(document).ready(function () {


  $(".open").click(function () {
    document.getElementById("Sidenav").style.display = "block";
    // document.body.style.overflowX = "hidden";
  });
  $(".closebtn").click(function () {
    document.getElementById("Sidenav").style.display = "none";
  });

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
  // let content = $("#wmd-input-id_content");
  let content = $(".note-editing-area");
  let contentComment = $("#id_content");
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

  function setContentComment(value) {
    if (value) {
      var markContent = marked(value)
      // $("#preview-content").html('عرض');
      $("#preview-content").html(markContent);
    }
    $("#preview-content img").each(function () {

      $(this).addClass("embed-responsive");
    });
  };
  setContentComment(contentComment.val());
  contentComment.keyup = (() => {
    var newContent = $(this).val()
    setContentComment(newContent)
  });

  $("textarea, .content-markdown,.about").attr("dir", "auto");
  $(".about ,.about p, .about h1, #search").attr("dir", "auto");
  $(".note-editing-area,.CodeMirror-scroll").attr("dir", "auto");
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

  // $(document).on('click', ".comment-reply-btn-thread", function (event) {
  //   event.preventDefault();
  //   $(".comment-reply").fadeToggle();
  //   //$(this).parent().next(".comment-reply").fadeToggle();
  // });

  // $(document).on('click', ".comment-reply-btn", function (event) {
  //   event.preventDefault();
  //   $(this).parent().next(".comment-reply").fadeToggle();
  // });


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



  // var showCode = $("#comments-form textarea").click(function () {
  //   $(".hide").css("display", "block");
  //   if ($(this).val() == ' ') {
  //     $(".hide").css("display", "none");
  //   }
  // })
  var showCode = $(document).on('click', ".comments-form textarea", function (event) {
    event.preventDefault();
    $(".hide").css("display", "block");
  });
  window.onclick = function (event) {
    if (event.target == showCode) {
      // showCod.style.display = "none";
      $(".hide").css("display", "none");
    }
  }




  //  dark mode

  if (window.CSS && CSS.supports("color", "var(--primary)")) {
    var toggleColorMode = function toggleColorMode(e) {
      // Switch to Light Mode
      if (e.currentTarget.classList.contains("light--hidden")) {
        // Sets the custom html attribute
        document.documentElement.setAttribute("color-mode", "light"); // Sets the user's preference in local storage

        localStorage.setItem("color-mode", "light");
        return;
      }
      /* Switch to Dark Mode
      Sets the custom html attribute */
      document.documentElement.setAttribute("color-mode", "dark"); // Sets the user's preference in local storage

      localStorage.setItem("color-mode", "dark");
    }; // Get the buttons in the DOM

    var toggleColorButtons = document.querySelectorAll(".toggle-mode"); // Set up event listeners

    toggleColorButtons.forEach(function (btn) {
      btn.addEventListener("click", toggleColorMode);
    });
  } else {
    // If the feature isn't supported, then we hide the toggle buttons
    var btnContainer = document.querySelector(".toggle-mode");
    btnContainer.style.display = "none";
  }
  const currentTheme = localStorage.getItem('color-mode');
  if (currentTheme) {
    document.documentElement.setAttribute('color-mode', currentTheme);
  }



  // if ($(window).width() < 798) { }


  $(".comment-reply-btn-thread").click(function (event) {
    event.preventDefault();
    $(".comment-reply-thread").fadeToggle();
    //$(this).parent().next(".comment-reply").fadeToggle();
  });
  $(".comment-reply-btn").click(function (e) {
    e.preventDefault();
    $(this).parent().next(".comment-reply").fadeToggle();
  });







  var open = document.querySelector(".open-comment");
  var main = document.querySelector(".main");

  let openComment = $(".open-comment").click(function () {
    $(".main").addClass("active");
  });
  let closeComments = $(".closeComment").click(function () {
    $(".main").removeClass("active");
  });
  // var closeComment = document.querySelector(".closeComment")
  // if (open) {
  //   closeComment.addEventListener('click', () => {
  //     main.classList.remove("active");
  //   });
  // }

  //  when we click any pint in windo slide hide
  window.onclick = function (event) {
    if (event.target == openComment) {
      event.hide = closeComments;
    }
  }





});


