

//(function ($) {
//  $.fn.rotateTableCellContent = function (options) {
//  /*
//  Version 1.0
//  7/2011
//  Written by David Votrubec (davidjs.com) and
//  Michal Tehnik (@Mictech) for ST-Software.com
//  */
//
//		var cssClass = ((options) ? options.className : false) || "vertical";
//
//		var cellsToRotate = $('.' + cssClass, this);
//
//		var betterCells = [];
//		cellsToRotate.each(function () {
//			var cell = $(this)
//		  , newText = cell.text()
//		  , height = cell.height()
//		  , width = cell.width()
//		  , newDiv = $('<div>', { height: width, width: height })
//		  , newInnerDiv = $('<div>', { text: newText, 'class': 'rotated' });
//// fix positioning issues in Jenkins
//            newInnerDiv.css('-webkit-transform-origin', (width / 2) + 'px ' + (width / 2) + 'px');
//            newInnerDiv.css('-moz-transform-origin', (width / 2) + 'px ' + (width / 2) + 'px');
//			newDiv.append(newInnerDiv);
//
//			betterCells.push(newDiv);
//		});
//
//		cellsToRotate.each(function (i) {
//			$(this).html(betterCells[i]);
//		});
//	};
//})(jQuery);

//(function ($) {
//  $.fn.rotateTableCellContent = function (options) {
//  /*
//  Version 1.0
//  7/2011
//  Written by David Votrubec (davidjs.com) and
//  Michal Tehnik (@Mictech) for ST-Software.com
//  */
//
//		var cssClass = ((options) ? options.className : false) || "vertikal";
//
//		var cellsToRotate = $('.' + cssClass, this);
//
//		var betterCells = [];
//		cellsToRotate.each(function () {
//			var cell = $(this)
//		  , newText = cell.text()
//		  , height = cell.height()
//		  , width = cell.width()
//		  , newDiv = $('<svg width=' + height + ' height=' + width + '>')
//		  , newInnerDiv = $('<text>', { x: Math.round(height/2), y: Math.round(width/2), transform: "rotate(-90, " + Math.round(height/2) + ", " + Math.round(width/2) + ")", style: "text-anchor:middle;", text: newText});
//			newDiv.append(newInnerDiv);
//			betterCells.push(newDiv);
//		});
//
//
//		cellsToRotate.each(function (i) {
//			$(this).html(betterCells[i]);
//            console.log($(this).html(betterCells[i]));
//		});
//	};
//})(jQuery);

//<svg width="50" height="300">
//##                <text x="28" y="150" transform="rotate(-90, 28, 150)" style="text-anchor:middle;">${req["label"]}</text>
//##            </svg>