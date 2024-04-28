$(document).ready(function(){
  ["header", "nav", "footer"].forEach((e) => {
    $(e).load(e+".html");
  });
});
