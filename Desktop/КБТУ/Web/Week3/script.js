var newTask = document.querySelector('.myInput');
var ulList = document.querySelector('.myUL');

var addBtn = document.querySelector('.addBtn');
addBtn.addEventListener('click', addElement);

var deleteBtn = document.querySelector('.close');
deleteBtn.addEventListener('click', deleteElement);

function addElement(){
    let newel = document.createElement('li');
    if(newTask.value != ''){
      newel.innerHTML = newTask.value;
      ulList.appendChild(newel);
      newTask.value = "";
    }
    else{
      alert('Error! Write some task');
    }
}

function deleteElement() {
  if(ulList.hasChildNodes()){
    ulList.removeChild(ulList.firstChild);
  }
  else{
    alert('List is empty!');
  }
}