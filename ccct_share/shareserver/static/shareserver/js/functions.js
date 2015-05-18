$(document).ready(function() {
	$(".dir").click(function() {
		perform($(this).text());
	});
	$(".filedir").click(function() {
		download($(this).text());
	});
	$("#ul-file").click(function() {
		$("#exampleInputFile").trigger("click");
	});
	$("#exampleInputFile").change(function() {
		perform("file");
	});
});

function perform(dir) {
	if(dir === "Back") {
		dir = ".."
	}
	$("#directory").val(dir);
	$("#inputFile")[0].submit();
}

function download(filedir) {
	$.ajax({
		method: "POST",
		url: "download/",
		headers: { "X-CSRFToken": getCookie("csrftoken") },
		data: { 'filename': filedir }, 
	})
	.done(function(data) {
		$("#downloadfile").attr('download', filedir);
		$("#downloadfile").attr('href', "http://127.0.0.1:8000/" + data.substring(12, data.length));
		$("#downloadfile").get(0).click();
	})
}

function getCookie(c_name) {
  if (document.cookie.length > 0)
  {
      c_start = document.cookie.indexOf(c_name + "=");
      if (c_start != -1)
      {
          c_start = c_start + c_name.length + 1;
          c_end = document.cookie.indexOf(";", c_start);
          if (c_end == -1) c_end = document.cookie.length;
          return unescape(document.cookie.substring(c_start,c_end));
      }
  }
  return "";
}