function init(){
    fetch('./index.py')
  .then(response => response.json())
  .then(data => console.log(data));
}


window.onload = init();