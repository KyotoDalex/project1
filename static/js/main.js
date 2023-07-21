(function ($) {
  "use strict";

/*===========================================
      Table of contents
  01. On Load Function
  02. Preloader
  03. Mobile Menu Active
  04. Sticky fix
  05. Scroll To Top
  06. Set Background Image
  07. Popup Sidemenu
  08. Search Box Popup
  09. Select Box Active
  10. Date & Time Picker
  11. Magnific Popup
  12. Sub Menu Position
  13. One Page Nav
  14. Custom Animaiton
  15. Dropdown Toggler
  16. Right Click Disable
  17. Inspect Element Disable
=============================================*/


  /*---------- 01. On Load Function ----------*/
  $(window).on('load', function () {
    $('.preloader').fadeOut();
  });



  /*---------- 02. Preloader ----------*/
  if ($('.preloader').length > 0) {
    $('.preloaderCls').each(function () {
      $(this).on('click', function (e) {
        e.preventDefault();
        $('.preloader').css('display', 'none');
      });
    });
  }



  /*---------- 03. Mobile Menu Active ----------*/
  $('.mobile-menu-active').each(function(){
    $(this).vsmobilemenu({
      menuContainer: '.vs-mobile-menu',
      expandScreenWidth: $(this).data('expand'),
      menuToggleBtn: '.vs-menu-toggle'
    });
  });



  /*---------- 04. Sticky fix ----------*/
  var lastScrollTop = '';
  var scrollToTopBtn = '.scrollToTop';

  function stickyMenu($targetMenu, $toggleClass) {
    var st = $(window).scrollTop();
    if ($(window).scrollTop() > 600) {
      if (st > lastScrollTop) {
        $targetMenu.removeClass($toggleClass);

      } else {
        $targetMenu.addClass($toggleClass);
      }
    } else {
      $targetMenu.removeClass($toggleClass);
    }
    lastScrollTop = st;
  }
  $(window).on("scroll", function () {
    stickyMenu($('.sticky-header'), "active");
    if ($(this).scrollTop() > 400) {
      $(scrollToTopBtn).addClass('show');
    } else {
      $(scrollToTopBtn).removeClass('show');
    }
  });



  /*---------- 05. Scroll To Top ----------*/
  $(scrollToTopBtn).on('click', function (e) {
    e.preventDefault();
    $('html, body').animate({
      scrollTop: 0
    }, 3000);
    return false;
  });




  /*---------- 06.Set Background Image ----------*/
  if ($('.background-image').length > 0) {
    $('.background-image').each(function () {
      var src = $(this).attr('data-bg-src');
      $(this).css({
        'background-image': 'url(' + src + ')'
      });
    });
  }





  /*---------- 07. Popup Sidemenu ----------*/
  function popupSideMenu($sideMenu, $sideMunuOpen, $sideMenuCls, $toggleCls) {
    // Sidebar Popup
    $($sideMunuOpen).on('click', function (e) {
      e.preventDefault();
      $($sideMenu).addClass($toggleCls);
      $('body').addClass('overflow-hidden');
    });
    $($sideMenu).on('click', function (e) {
      e.stopPropagation();
      $($sideMenu).removeClass($toggleCls);
      $('body').removeClass('overflow-hidden');
    });
    var sideMenuChild = $sideMenu + ' > div';
    $(sideMenuChild).on('click', function (e) {
      e.stopPropagation();
      $($sideMenu).addClass($toggleCls);
      $('body').addClass('overflow-hidden');
    });
    $($sideMenuCls).on('click', function (e) {
      e.preventDefault();
      e.stopPropagation();
      $($sideMenu).removeClass($toggleCls);
      $('body').removeClass('overflow-hidden');
    });
  }
  popupSideMenu('.sidemenu-wrapper', '.sideMenuToggler', '.sideMenuCls', 'show');





  /*---------- 08. Search Box Popup ----------*/
  function popupSarchBox($searchBox, $searchOpen, $searchCls, $toggleCls) {
    $($searchOpen).on('click', function (e) {
      e.preventDefault();
      $($searchBox).addClass($toggleCls);
      $('body').addClass('overflow-hidden');
    });
    $($searchBox).on('click', function (e) {
      e.stopPropagation();
      $($searchBox).removeClass($toggleCls);
      $('body').removeClass('overflow-hidden');
    });
    $($searchBox).find('form').on('click', function (e) {
      e.stopPropagation();
      $($searchBox).addClass($toggleCls);
      $('body').addClass('overflow-hidden');
    });
    $($searchCls).on('click', function (e) {
      e.preventDefault();
      e.stopPropagation();
      $($searchBox).removeClass($toggleCls);
      $('body').removeClass('overflow-hidden');
    });
  }
  popupSarchBox('.popup-search-box', '.searchBoxTggler', '.searchClose', 'show');



  /*----------- 09. Select Box Active ----------*/
  if ($('select').length > 0) {
    $('select').niceSelect();
  }



  /*----------- 11. Magnific Popup ----------*/
  /* magnificPopup img view */
  $('.popup-image').magnificPopup({
    type: 'image',
    gallery: {
      enabled: true
    }
  });

  /* magnificPopup video view */
  $('.popup-video').magnificPopup({
    type: 'iframe'
  });



  /*----------- 12. Sub Menu Position ----------*/
  function subMenu() {
    var $subMain = $('.main-menu > .menu-item-has-children > ul');
    var $subSub = $('.main-menu .menu-item-has-children > ul ul');
    $subMain.each(function () {
      if ($(window).width() > 991) {
        if ($(this).offset().left + $(this).width() > $(window).width()) {
          $(this).css({
            'left': 'auto',
            'right': '100%'
          });
        } else {
          $(this).css({
            'left': '0',
            'right': 'auto'
          });
        }
      }
    });
    $subSub.each(function () {
      if ($(window).width() > 991) {
        if ($(this).offset().left + $(this).width() > $(window).width()) {
          $(this).css({
            'left': 'auto',
            'right': '100%'
          });
          $(this).find('.sub-menu').css({
            'left': 'auto',
            'right': '100%'
          });
        }
      }
    });
  }
  subMenu();
  $(window).on('resize', function () {
    subMenu();
  });



  /*----------- 13. One Page Nav ----------*/
  function onePageNav(element) {
    if ($(element).length > 0) {
      $(element).each(function(){
        $(this).find('a').each(function () {
          $(this).on('click', function () {
            var target = $(this.getAttribute('href'));
            if (target.length) {
              event.preventDefault();
              $('html, body').stop().animate({
                scrollTop: target.offset().top - 10
              }, 1000);
            }

          });
        });
      } );
    }
  }
  onePageNav('.onepage-nav');



  
  /*----------- 14. Custom Animaiton ----------*/
  $('[data-ani-duration]').each(function(){
    var durationTime = $(this).data('ani-duration');
    $(this).css('animation-duration', durationTime);
  });

  $('[data-ani-delay]').each(function(){
    var delayTime = $(this).data('ani-delay');
    $(this).css('animation-delay', delayTime);
  });

  $('[data-ani]').each(function(){
    var animaionName = $(this).data('ani'); 
    $(this).addClass(animaionName);
    $('.slick-current [data-ani]').addClass('animated');
  });
  
  $('.vs-carousel').on('afterChange', function (event, slick, currentSlide, nextSlide) {
    $('[data-ani]').removeClass('animated');
    $('.slick-current [data-ani]').addClass('animated');
  });



  /*----------- 15. Dropdown Toggler ----------*/
  $('.dropdown-btn').each(function(){
    var btn = $(this);
    btn.on('click', function(e){
      e.preventDefault();
      btn.toggleClass('active');
      btn.next('.dropdown-menu').toggleClass('show');
    });
  });



  
  /*----------- 16. Right Click Disable ----------*/
  // window.addEventListener('contextmenu', function (e) {
  //   // do something here... 
  //   e.preventDefault();
  // }, false);


  /*----------- 17. Inspect Element Disable ----------*/
  // document.onkeydown = function (e) {
  //   if (event.keyCode == 123) {
  //     return false;
  //   }
  //   if (e.ctrlKey && e.shiftKey && e.keyCode == 'I'.charCodeAt(0)) {
  //     return false;
  //   }
  //   if (e.ctrlKey && e.shiftKey && e.keyCode == 'C'.charCodeAt(0)) {
  //     return false;
  //   }
  //   if (e.ctrlKey && e.shiftKey && e.keyCode == 'J'.charCodeAt(0)) {
  //     return false;
  //   }
  //   if (e.ctrlKey && e.keyCode == 'U'.charCodeAt(0)) {
  //     return false;
  //   }
  // };

  jQuery(document).ready(function($){
    var offset = $( ".sticky" ).offset();
    checkOffset();

    $(window).scroll(function() {
        checkOffset();
    });

    function checkOffset() {
        if ( $(document).scrollTop() > offset.top){
            $('.sticky').addClass('fixed');
        } else {
            $('.sticky').removeClass('fixed');
        } 
    }

});
  

})(jQuery);