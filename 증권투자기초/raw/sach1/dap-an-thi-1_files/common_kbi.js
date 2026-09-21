//document.write('<script src="http://' + (location.host || 'localhost').split(':')[0] + ':1337/livereload.js"></' + 'script>');
document.write('<script src="https://www.kbi.or.kr/js/common/placeholders.min.js"></script>');


//jQuery.noConflict();



var etc = (function(){
	function init(){
		ieCheck();
		ie7Check();
	}
	function ie7Check(){
		var userA = navigator.userAgent.indexOf('MSIE 7.0');
		if(userA != -1){
			$('html').addClass('ie7');
		}
	};
	function ieCheck(){
		var IEIndex = navigator.appVersion.indexOf("MSIE");
		var IE8Over = navigator.userAgent.indexOf("Trident");
		if( IEIndex > 0 || IE8Over > 0 )  {
			var trident = navigator.userAgent.match(/Trident\/(\d.\d)/i);
			var strVer = "";
			if (trident != null){
				switch (trident[1]) {
					case "7.0" :
						strVer = "11.0";
						break;
					case "6.0" :
						strVer = "10.0";
						break;
					case "5.0" :
						strVer = "9.0";
						break;
					case "4.0" :
						strVer = "8.0";
						break;
					case "3.0" :
						strVer = "7.0";
						break;
					default :
						break;
				}
			}
		} else {
			strVer = "not";
		}
		if(strVer == "7.0"){
			$("html").addClass("ie7");
		}
		if(strVer == "8.0"){
			$("html").addClass("ie8");
		}
		if(strVer == "9.0"){
			$("html").addClass("ie9");
		}
	}

	return {init: init};
})();

var header = (function(){
	var el;

	function init(){
		el = $('#header');
		if(el.children().length <= 0){
			
			window.header = $.get('/jsp/home/include/classroom/header.jsp');
			
			window.header.done(function(data){
				el.html(data);
				setTimeout(function(){
					complete();
				}, 0);
			});
		}else{
			complete();
		}
	}

	function complete(){
		//gnbMenu();

	}

	function gnbMenu(){
		var el = $(".ul_gnb_menu li").find(">a");
		var timeout;
		var sub = ".gm_sub_list"
		el.on("mouseenter focusin", function(){
			$(".gm").removeClass("on")
			showSubArea($(this));

		})
		el.on("mouseleave focusout", function(){
			hideSubArea($(this));
		})
		$(".gm>a").on("mouseenter focusin", function(){
			subMenuWidth();
		})
		$(".gm>a").on("mouseleave focusout", function(){
			subMenuWidth();
		})

		/*el.parent().parent().find(">li").focusin(function(){
			showSubArea();
		})
		el.parent().parent().find(">li").focusout(function(){
			hideSubArea();
		})*/
		var _width = 0;
		var _ori_width;
		function showSubArea(a){
			var con = a.next();
			var con_li = con.find("li")


			a.parents(".gm").addClass("on")
			window.clearTimeout(timeout);
		}
		function subMenuWidth(){
			_width = 0;
			_ori_width = 0;
			$(".gm.on .gm_sub_list li").each( function(){
				_width = _width + $(this).width() + 2

			})
			$(".gm.on .gm_sub_list").width(_width)
		}
		function hideSubArea(a){
			var con = a
			timeout = window.setTimeout(function(){
				$(".gm").removeClass("on")
				$(".gm_sub_list").removeAttr("style")
				_width = 0;
				_ori_width = 0;

			}, 600);
		}
	}
	return {init: init};
})();

var lnb = (function(){
	var el;
	var els;
	var pagename;
	var _index
	//function init(a,b){
	function init(a,b){
		
		_index = a-1
		els = $("#container")
		el = $('#lnb');
		//pagename = el.attr("class");
		//pagename = el.attr("class");
		if(el.children().length <= 0){
			//window.header = $.get('/publish/include/layout_kbi/lnb-' + pagename + b);
			window.header = $.get('/jsp/home/include/classroom/incl_lnb.jsp');
			window.header.done(function(data){
				el.html(data);
				pageNum();
				lnbStringRepFunc();
				setTimeout(function(){
					complete();
				}, 0);
			});
		}else{
			complete(_index);
		}
	}
	function pageNum(){
		
		if(typeof pageIndex != 'undefined'){
			$('.lnb_ul li').removeClass('active');
			$('.dep'+pageIndex).addClass('active');
		}
	}
	function lnbStringRepFunc(){
		/*
		if(typeof lnbStringRep != 'undefined'){
			$('.lnb_ul li:eq('+pageIndex+') a').text(lnbStringRep);
		}
		*/
	}
	function complete(a){

		//console.log(_index)

		$(".menu_area .lia:eq(" + _index  + ")").addClass("on")
		// 20160120 추가
		$(".menu_area .lia .menua").on("click", function(e){
			if($(this).get(0).nodeName == "A"){
				if($(this).attr("href") == "#"){
					e.preventDefault();
				}
			}
			$(".menu_area .lia").removeClass("on");
			$(this).parent().addClass("on");
		});
		// 20160120 추가
	}


	return {init: init, complete: complete};
})();
var mainPlanUl = (function(){
	var el;
	var els;
	var pagename;
	var _index
	//function init(a,b){
	function init(a,b){
		
		_index = a-1
		els = $("#container")
		el = $('#mainPlanUl');
		//pagename = el.attr("class");
		//pagename = el.attr("class");
		if(el.children().length <= 0){
			//window.header = $.get('/publish/include/layout_kbi/lnb-' + pagename + b);
			window.header = $.get('/jsp/home/include/classroom/mainPlanUl.jsp');
			window.header.done(function(data){
				el.html(data);
				
			});
		}else{
			//complete(_index);
		}
	}


	return {init: init};
})();
var footer = (function(){
	var el;

	function init(){
		el = $('#footer');

		if(el.children().length <= 0){
			window.footer = $.get('/jsp/home/include/classroom/footer.jsp');
			window.footer.done(function(data){
				el.html(data);

				setTimeout(function(){
					complete();
				}, 0);
			});
		}else{
			complete();
		}
	}

	function complete(){

	}

	return {init: init};
})();

var content = (function(){
	var el;

	function init(){
		$("#container").removeAttr("class")
		$("#container").addClass("clfix");
		$("#container").addClass("noimg")
		btnTop();
		askList();
		bookCategoryBox();
		uiInputFileFine();
		tabMenuAction();
		inputStyle();
		btnStyle();
		miniPop();
		idpwfind();
		customerList();
		conDefault()
		tblStyle();
		windowOpen();
		fileValueRetrun();
		setTimeout( function(){
			$("#lnb").css({"min-height":$("#content").innerHeight()});
		},1);
	}
	function fileValueRetrun(select , getSelect){
		$('.'+select).change(function(){
			var $_thisValue = $(this).val();
			var valIndex = $_thisValue.lastIndexOf('\\');
			var valReturn = $_thisValue.slice(valIndex + 1);
			$('.'+getSelect).val(valReturn);
		});
	}
	function windowOpen(select , url , name , width , height , left , top){
		var url = url;
		var name = name ? name : null;
		var width = width ? width : 730;
		var height = height ? height : 600;
		var left = left ? left : 50;
		var top = top ? top : 50;
	
		var _this = this;
		$('.' + select).on({
			'click' : function(){
				if(select == 'btnTestStart03'){
					var confir = window.confirm('최종 확인사항을 모두 숙지하셨습니까?\n\'확인\'을 누르면, 시험이 시작됩니다.');
					if(confir){
						confir = window.confirm('◈꼭 읽어 보세요◈\n\n\n◇시작시간으로부터 "120분" 간 응시할 수 있으며, "마감시간(04.19 22:00)"이 되면 남은 시간에 관계없이 "강제종료"됩니다.\n\n유의사항을 다시 한 번 읽어보시려면 \'취소\'버튼, 유의사항을 숙지하여 시험을 시작하시려면 \'확인\'버튼을 클릭하세요.');
						if(confir){
							window.open(url , '' , 'width='+width+' , height='+height+' , left='+left+' , top='+top+'');
							$('.popTestStart').removeClass('pop_on');
							$.samsiklib.ui.dimm.hide();
						}else{
							$('.popTestStart').removeClass('pop_on');
							$.samsiklib.ui.dimm.hide();
							$('.btnTestStart01').click();
						}
					}else{
						$('.popTestStart').removeClass('pop_on');
						$.samsiklib.ui.dimm.hide();
					}
				}else{
					window.open(url , '' , 'width='+width+' , height='+height+' , left='+left+' , top='+top+'');
				}
			}
		});
	}
	function tblStyle(){

		$(".tbl_col_gray01 td[rowspan]").css({
			"border-right":"1px solid #e6e6e6"
		})

		$(".tbl_col_gray01 td[rowspan]:last-child").css({
			"border-right":"0"
		})
	}
	function conOn(btn, common){
		var _btn = $("." + btn)
		var _common = $("." + common)
		var _con
		var _index
		_index = _btn.parents("ul").find(".on").index() + 1
		_con = $("." + common).hide();
		_con = $("." + common + _index)
		_con.show();
		_btn.on("click", function(){
			_common.hide();
			_index = $(this).parent().index() + 1;
			_con = $("." + common + _index)
			_con.show();
			_con.find("li").removeClass("on");
			_con.find("li:eq(0)").addClass("on");
		})
	}

	function conDefault(){
		if($(".page_title").find("p").length > 0){
			$(".content_top").addClass("to")
		} else {

		}
	}

	function conSlide(_slide, _slideMenu){

		var mIndex
		var current = 0;
		var _last
		var _slides = $("." + _slide)
		var _slidesMenu = $("." + _slideMenu)
		var _slidesActive
		var _slidesLastIndex

		_slidesMenu.find("a").on("click", function(e){
			e.preventDefault();
			_slidesMenu.find("a").removeClass("on")
			$(this).addClass("on")
			current = $(this).parent().index()
			_slidesActive.goToSlide(current)
			_slides.parents(".sliderwrap").find(".slider-stop").trigger("click")
		})

		_slidesActive = _slides.bxSlider({
			speed:1,
			slideWidth: 854,
			minSlides: 1,
			maxSlides: 1,
			auto:true,
			slideMargin: 28,
			autoControls:true,
			infiniteLoop: false,
			onSliderLoad: function(){

				//current = _slidesActive.getCurrentSlide();

			},
			onSlideBefore: function(){
				current = _slidesActive.getCurrentSlide();
				//console.log(current)
				lineActive();
			}
			//content.conSlide('books','menu')
		})
		//$("." + _slide + " .bx-clone").hide();
		function lineActive(){
			_slidesMenu.find("li a").removeClass("on")
			_slidesMenu.find("li:eq(" + current + ") a").addClass("on")
		}

	}
	function customerList(){
		var _index
		$(".customer_menu li a").on("click", function(e){
			e.preventDefault();
			_index = $(this).parent().index() + 1
			$(".customer_menu li").removeClass("on")
			$(this).parent().addClass("on")
			$(".customer_list ol").removeClass("on")
			//console.log(_index)
			$(".customer_list .ol" + _index).addClass("on")
		})
	}
	function btnTop(){
		var el = $(".ui_btn_top");
		el.on("click", function(e){
			e.preventDefault();
			$("body").scrollTop(0);
		})
	}
	function askList(){
		var con = $(".ask_head");

		con.on("click", function(){

			var _switch = $(this).parent().hasClass("on");
			if(_switch){
				$(this).parent().removeClass("on");
			} else {
				$(this).parent().addClass("on");
			}
		})
	}

	function bookCategoryBox(){
		var menu = $(".book_cate_menu ul li a")
		var book = $(".book_category_box .ul_book")
		var _index;

		start();

		function start(){
			_index = menu.parent(".on").index() + 1;
			show(_index);
		}

		function show(c){
			$(".m0" + c).show();
		}

		function hide(){
			book.hide();
		}
		menu.on("click", function(e){
			e.preventDefault();
			menu.parent().removeClass("on");
			$(this).parent().addClass("on")
			_index = $(this).parent().index() + 1;
			hide();
			show(_index);

		})
	}

	function uiInputFileFine(){
		var _el = $(".ui_input_filefind");
		var _el_btn = $(".ui_input_filefind_btn");
		_el_btn.change( function(){
			$(this).parent().parent().children(".ui_input_filefind").val($(this).val())
		})

		_el_btn.on('mousedown',function(event) {
			$(this).trigger('click')
		});

	}

	function tabMenuAction(){
		var _el = $(".ui_tab_menu")
		var _index;

		start();

		function start(){
			_index = _el.find(".on").index() + 1;
			show(_index);
		}

		function show(c){
			$(".con0" + c).show();
		}

		function hide(){
			_el.parent().find(".con").hide();
		}

		_el.find("li a").on("click", function(e){
			e.preventDefault();
			$(this).parent().parent().children().removeClass("on")
			$(this).parent().addClass("on")
			_index = $(this).parent().index() + 1;
			hide();
			show(_index);
		})


		function tabs02(){
			var _el = $(".bu_cate_ul li a")
			_el.on("click", function(){
				$(this).parent().parent().find(".on").removeClass("on")
				$(this).parent().addClass("on")
			})
		}tabs02();

		function tabs01(){
			var _el = $(".tab_menu01 li a")
			_el.on("click", function(e){
				if(!$(this).hasClass("ui_btn_top")){
					e.preventDefault();
					$(this).parent().parent().find(".on").removeClass("on")
					$(this).parent().addClass("on")
				}
			})
		}tabs01();

		function tabs03(){
			var _el = $(".tab_menu03>ul>li>a")
			var _bu
			_el.on("click", function(e){
				if($(this).attr("href") == "#"){
					e.preventDefault();
					$(this).parent().parent().find(".on").removeClass("on")
					$(this).parent().addClass("on")
				}
/*				if($(this).next().hasClass("bu")){
					_bu = $(this).next();
					$(this).parents(".six").css({"margin-bottom":_bu.height()})
					_bu.addClass("dpb")
				} else {
					$(this).parents(".six").removeAttr("style")

				}*/
			})
		}tabs03();

	}
	function tabContent(_tab,_con){
		var menu = $("." + _tab)
		var con = $("." + _con)
		var _index
		menu.find("a").on("click", function(e){
			e.preventDefault();
			_index = $(this).parent().index() + 1;
			//console.log("18")
			con.removeClass("dpb")
			$("." + _con + _index).addClass("dpb")
		})

	}
	function btnStyle(){

		function ternBtn(){
			var _switch
			$(".inq_tern a").on("click", function(e){
				e.preventDefault();
				$(".inq_tern a").removeClass("on_red")
				$(this).addClass("on_red")
			})
		}
		ternBtn();
	}

	function inputStyle(){

		function init(){
			inputStyleIng();

			return this;
		}
		init();

		function inputStyleIng(){
			function ie8Input(){
				if($("html").hasClass("ie8")){
					$("input").each( function(){
						var og = $(this).width();
						var ogpl = $(this).css("padding-left").replace("px","")
						var ogpr =  $(this).css("padding-right").replace("px","")
						//console.log(ogpl)
						$(this).width(og-ogpl-ogpr)
					})

				}
			}
			ie8Input();

			$(".radiostyle01 input[checked]").next().addClass("on");
			$(".checkstyle01 input[checked]").next().addClass("on");
			$(".checkstyle02 input[checked]").next().addClass("on")

			$(".radiostyle01").on("click", function(){
				var name = $(this).children("input").attr("name");
				$(".radiostyle01").children("input[name=" + name + "]").parent().children("span").removeClass("on")
				$(this).children("span").addClass("on");
			})
			$(".checkstyle01 input").on("click", function(){
				$(this).next("span").removeClass("on")
				if($(this).is(":checked")){
					$(this).next("span").addClass("on");
				}
			})
			$(".checkstyle02 input").on("click", function(){
				$(this).next("span").removeClass("on")
				if($(this).is(":checked")){
					$(this).next("span").addClass("on");
				}
			});
		};
	}

	function layerPopOpen(a,b ,scroll , height){
		//console.log(a)
		var popBtn = $("." + a)
		var _pop = $("." + b)
		var src
		var _pople;
		var height = height ? height : 600;
		var zIndex = 10000
		popBtn.on("click", function(e){
			//console.log(b)
			e.preventDefault();
			if(a.indexOf('btnAddressOpen111') != -1){//'지역별 평가장소 안내'(m-013-01) --> '약도'버튼 클릭시 20160418
				popPosition(false);
				$('.popTestStart').removeClass("pop_on");
				_pop.addClass("pop_on");
				_pop.css({
					"position" : "fixed",
					"z-index" : zIndex,
					"top" : $('.popSetMapModify').offset().top,
					"left" : $('.popSetMapModify').offset().left + $('.popSetMapModify').width()
				});
				$("body").css({
					'overflow-y' : 'hidden'
				})
				$.samsiklib.ui.dimm.hide();
				$.samsiklib.ui.dimm.show();
			}else{
				popPosition();
				_pop.addClass("pop_on");
				if(scroll){
					_pop.css({'height' : height, 'overflow-y' : 'auto'});
				}
				_pop.css({
					"position" : "fixed",
					"z-index" : zIndex,
					"top" : ($(window).height()/2) - (_pop.height()/2),
					"left" : ($(window).width()/2) - (_pop.width()/2)
				});
				$("body").css({
					'overflow-y' : 'hidden'
				})
				$.samsiklib.ui.dimm.show();
			}
		})

		function popPosition(addressPop){
			if(addressPop){
			$(window).resize(function(){
				_pop.css({
					"position" : "fixed",
					"z-index" : zIndex,
					"top" : $('.popSetMapModify').offset().top,
					"left" : $('.popSetMapModify').offset().left + $('.popSetMapModify').width()
				});
			});
			}else{
				$(window).resize(function(){
					_pop.css({
						"position" : "fixed",
						"z-index" : "100000",
						"top" : ($(window).height()/2) - (_pop.height()/2),
						"left" : ($(window).width()/2) - (_pop.width()/2)
					})
				});
			}
		}

		_pop.find(".ui_btn_exit").on("click", function(e){
			e.preventDefault();
			_pople = $(".pop_on").length

			$(this).parents(".pop_wrap").removeClass("pop_on")

			if(_pople == 1){
				$("body").css({
					'overflow-y' : 'auto'
				})
				$.samsiklib.ui.dimm.hide();
			}
			//$(this).parents(".pop_wrap").removeClass("dpb")
			//$.samsiklib.ui.dimm.hide();
		})
	}

	function layerPopAutoOpen(a){
		var _pop = $("." + a)
		var src

		popPosition();
		_pop.addClass("pop_on")
		_pop.css({
			"position" : "fixed",
			"z-index" : "100000",
			"top" : ($(window).height()/2) - (_pop.height()/2),
			"left" : ($(window).width()/2) - (_pop.width()/2)
		})
		$("body").css({
			'overflow-y' : 'hidden'
		})
		$.samsiklib.ui.dimm.show();


		function popPosition(){
			$(window).resize(function(){
				_pop.css({
					"position" : "fixed",
					"z-index" : "100000",
					"top" : ($(window).height()/2) - (_pop.height()/2),
					"left" : ($(window).width()/2) - (_pop.width()/2)
				})
			});
		}

		_pop.find(".ui_btn_exit").on("click", function(e){
			e.preventDefault();
			_pople = $(".pop_on").length

			_pop.removeClass("pop_on")

			if(_pople == 1){
				$("body").css({
					'overflow-y' : 'auto'
				})
				$.samsiklib.ui.dimm.hide();
			}
			//$(this).parents(".pop_wrap").removeClass("dpb")
			//$.samsiklib.ui.dimm.hide();
		})
	}




	function miniPop(){
		var _el = $(".alert_box .minibox")
		var _btn = $(".btn_alert01")
		var _btn_exit = $(".minibox .close")
		_btn.on("click", function(e){
			e.preventDefault();
			$(this).next().show();
		})
		_btn_exit.on("click", function(e){
			e.preventDefault();
			$(this).parent().parent().hide();
		})
	}

	function idpwfind(){
		var _el = $(".myself a")
		var _name;
		_el.on("click", function(e){
			e.preventDefault();
			_el.addClass("off")
			_el.removeClass("on")
			$(".con_self").addClass('dpn')
			$(this).removeClass("off")
			$(this).addClass("on")
			if($(this).hasClass("phone")){
				$(".con_phone").removeClass("dpn")
			} else if($(this).hasClass("mail")){
				$(".con_mail").removeClass("dpn")
			}
		})
	}
	return {init: init,layerPopOpen: layerPopOpen, layerPopAutoOpen:layerPopAutoOpen, inputStyle:inputStyle, conSlide:conSlide, tabContent:tabContent, conOn:conOn, windowOpen:windowOpen , fileValueRetrun:fileValueRetrun}
})();

$(function(){
	//console.log( "current device : " + getUserAgent() );
	etc.init();
	header.init();
	footer.init();
	content.init();
	lnb.init();
	mainPlanUl.init();
});

var samsiklib_config = {
	dimm: {
		style: {
			backgroundColor: "#000000"
			, opacity: 0.7
		}
		, animate: true
	}
};

(function(root, doc, factory){
	if (typeof define === "function" && define.amd){
		// AMD. Register as an anonymous module.
		define(["jquery"], function($) {
			factory($, root, doc);
			return $.samsiklib;
		});
	}else{
		// Browser globals
		factory(root.jQuery, root, doc);
	}
}(this, document, function(jQuery, window, document, undefined) {
(function($) {
	$.samsiklib = {};
	var extend = $.extend;
	extend($.samsiklib, {ui:{}});
	extend($.samsiklib, {net:{}});
	extend($.samsiklib, {util:{}});
	extend($.samsiklib, {config:{}});
})(jQuery);
(function($) {
	if(samsiklib_config){
		$.extend(true, $.samsiklib.config, {
			dimm: {
				style: {
					backgroundColor: "#000000"
					, opacity: 0.7
				}
				, animate: true
				, callback: undefined
			}
		}, samsiklib_config);
	}
})(jQuery);

(function($, window, document, undefined){
	$.extend($.samsiklib.ui, {
		dimm: (function(){
			var _instance;
			var $dom;
			var _domId = "samsikui_dimm";
			var _options = $.samsiklib.config.dimm;


			function _init(){
				_create();

			}

			function _create(){
				$dom = $("<div/>").hide();
				$dom.attr({id: _domId});

				$(".contents").append($dom);

				$dom.css({position: "fixed", top: 0, bottom: 0, left: 0, right: 0, zIndex:1000});
			}

			function _destroy(){
				$dom.remove();
			}

			function _show(options){
				if(_instance){
					return;
				}
				_instance = true;

				var dfd = new $.Deferred();

				_init();

				var tmpOptions = $.extend(true, {}, _options, options);

				$dom.css($.extend({}, tmpOptions.style));

				if(tmpOptions.animate){
					dfd = $dom.css({display: "block", opacity: 0}).animate({opacity: tmpOptions.style.opacity}, 0).promise();
				}else{
					$dom.show();
				}

				dfd.always(function(){
					if(tmpOptions && $.isFunction(tmpOptions.callback)){
						tmpOptions.callback();
					}
				});
			}

			function _hide(options){
				if(!_instance){
					return;
				}
				_instance = false;

				var dfd = new $.Deferred();

				var tmpOptions = $.extend(true, {}, _options, options);

				if(_options.animate){
					dfd = $dom.animate({opacity: 0}, 0).promise().done(function(){
						$(this).css({display: "none"});
					});
				}else{
					dfd = $dom.hide().promise();
				}

				dfd.always(function(){
					_destroy();

					if($.isFunction(tmpOptions.callback)){
						tmpOptions.callback();
					}
				});
			}
			return {
				init: _init
				, show: _show
				, hide: _hide
			};
		})()
	});
})(jQuery, window, document);
}));





/*function PrintElem(elem)
{
	$(elem).attr("id","print")
	Popup($(elem).html());
}
function Popup(data)
{
	var mywindow = window.open('', 'print', 'height=400,width=600');
	mywindow.document.write('<html><head><title>my div</title>');
	mywindow.document.write('</head><body >');
	mywindow.document.write(data);
	mywindow.document.write('</body></html>');
	mywindow.document.close(); // IE >= 10에 필요
	mywindow.focus(); // necessary for IE >= 10
	mywindow.print();
	mywindow.close();
	return true;
}

$(function(){
	$(".btn_grada01").on("click", function(){
		PrintElem(".content_f")
	})
	PrintElem(".content_f")
})
*/


$( function(){
	$(".btn_grada01").on("click", function(){
		if($(this).find("span").text() == "인쇄하기"){
			$(".content_f").print({

			});
		}
	});
	$(".btn_ico_gray01").on("click", function(){
		if($(this).find("span").text() == "인쇄하기"){
			$(this).parents(".pop_body").print({

			});
		}
	});
	$('.txtAToggBtn').on({
		'click' : function(){
			$(this).parent().parent().parent().next('.reply_textarea.shhi').toggleClass('active');
			return false;
		}
	});
	$('.btnPrint').on({//m-013 수험표 출력 -> 출력버튼
		'click' : function(){
			var width = $('.popReportNum').width();
			var left = $('.popReportNum').css('left');
			$('.popReportNum').css({
				'width' : '100%',
				'left' : 0
			});
			$('.popReportNum').print({
				globalStyles: true,
				mediaPrint: false,
				noPrintSelector: ".pop_btn_wrap",
				iframe: true
			});
			$('.popReportNum').css({
				'width' : width,
				'left' : left
			});
		}
	});
	
	$('.btnPrint2').on({
		'click' : function(){
			$('.popReportNum  > .pop_body').print({
				globalStyles: true,
				mediaPrint: false,
				noPrintSelector: ".pop_btn_wrap",
				iframe: true
			});
		}
	});
})