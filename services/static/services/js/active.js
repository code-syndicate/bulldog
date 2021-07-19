(function ($) {
    'use strict';

    var $window = $(window);

    // :: Preloader Active Code
    ! function (e) {
        "use strict";
        var i = e(window),
            n = (e("dd"), e(".ecaps-page-wrapper")),
            o = e(".ecaps-sidemenu-area");
        e("body")[0], i.on("load", function () {
            e(".loading-area").fadeOut("slow", function () {
                e(this).remove()
            })
        })
    }(jQuery);

    // :: Fullscreen Active Code
    $window.on('resizeEnd', function () {
        $(".window-height").height($window.height());
    });

    $window.on('resize', function () {
        if (this.resizeTO) clearTimeout(this.resizeTO);
        this.resizeTO = setTimeout(function () {
            $(this).trigger('resizeEnd');
        }, 0);
    }).trigger("resize");

    // :: Marquee Active Code
    $('#closeMarquee').on('click', function () {
        $('#currMarque').fadeOut()
        $('footer').addClass('footer-marquee-close');
    })

    $('#currMarque').SimpleMarquee({
        duration: 50000,
        padding: 0,
        marquee_class: '.marquee',
        container_class: '.currency-marquee-area',
        sibling_class: 0,
        hover: true
    });

    // :: Slides Active Code
    if ($.fn.owlCarousel) {

        $(".team-carousel").owlCarousel({
            items: 3,
            loop: true,
            autoplay: true,
            smartSpeed: 800,
            margin: 50,
            center: true,
            nav: true,
            navText: ["<i class='fa fa-angle-left'</i>", "<i class='fa fa-angle-right'</i>"],
            responsive: {
                320: {
                    items: 1
                },
                576: {
                    items: 2
                },
                768: {
                    items: 3
                }
            }
        })

        $(".clients-logo-slider").owlCarousel({
            items: 5,
            loop: true,
            autoplay: true,
            smartSpeed: 300,
            margin: 30,
            center: true,
            dots: true,
            responsive: {
                0: {
                    items: 1
                },
                480: {
                    items: 2
                },
                576: {
                    items: 3
                },
                768: {
                    items: 4
                },
                992: {
                    items: 5
                }
            }
        });

        $(".latest-news-carousel").owlCarousel({
            items: 3,
            loop: true,
            autoplay: true,
            smartSpeed: 800,
            margin: 10,
            responsive: {
                320: {
                    items: 1
                },
                768: {
                    items: 2
                },
                992: {
                    items: 3
                }
            }
        })
    }

    // :: Hover Effects Active Code
    var hoverEffects = $('.why_choose_single_content');

    hoverEffects.on('mouseenter', function () {
        hoverEffects.removeClass('active');
        $(this).addClass('active');
    });

    // :: Sticky Menu Active Code

    $("#coreNav").sticky({
        topSpacing: 0
    });

    // nicescroll Active Code
    if ($.fn.niceScroll) {
        $("textarea").niceScroll({
            cursorcolor: "#111111",
            cursorwidth: "4px",
            background: "transparent",
            cursorborder: "none",
            cursorborderradius: 0
        });
    }

    // :: ScrollUp Active Code
    if ($.fn.scrollUp) {
        $.scrollUp({
            scrollSpeed: 1500,
            scrollText: '<i class="fa fa-angle-up" aria-hidden="true"></i>'
        });
    }


    // matchHeight Active Code
    if ($.fn.matchHeight) {
        $('.equalHeight').matchHeight();
    }

    // :: Magnific-popup Video Active Code
    if ($.fn.magnificPopup) {
        $('.video_btn').magnificPopup({
            disableOn: 0,
            type: 'iframe',
            mainClass: 'mfp-fade',
            removalDelay: 160,
            preloader: true,
            fixedContentPos: false
        });
        $('.gallery_img').magnificPopup({
            type: 'image',
            gallery: {
                enabled: true
            },
            removalDelay: 300,
            mainClass: 'mfp-fade',
            preloader: true
        });
    }

    // :: Countdown Active Code
    $('#clock').countdown('2026/11/10', function (event) {
        $(this).html(event.strftime('<div>%D <span>Days</span></div> <div>%H <span>Hours</span></div> <div>%M <span>Minutes</span></div> <div>%S <span>Seconds</span></div>'));
    });

    /// Date Picker JS
    if ($.fn.flatpickr) {
        $('.datepicker').flatpickr({
            dateFormat: 'd/m/Y',
        })
    }

    // :: Jarallax Active Code
    if ($.fn.jarallax) {
        $('.jarallax').jarallax({
            speed: 0.2
        });
    }

    // :: WOW Active Code
    new WOW().init();

})(jQuery);