//code block to populate version history
$(".image_holder").click(function(e) {
	var fav_item = $(".top-caption").val();
	alert(fav_item);
	/*
	$.ajax({
		type: "GET",
		url: "fetchWiki/?wiki="+decodeURI(res),
		dataType: "json",
		success : function(data) {
			var options = '<b>Select version to view article info : </b><select id="article" name="article" onchange=viewArticle();>';
			options += '<option value="">select wiki revision</optoin>';
			for(var i in data){
				options += '<option value='+data[i].url+' >' + data[i].title + '</option>';
			}
			options += '</select>';

			$('#result').html(options);
		},
		error : function(xhr,errmsg,err) {
			alert(xhr.status + ": " + xhr.responseText);
		}
	});
	*/
});
