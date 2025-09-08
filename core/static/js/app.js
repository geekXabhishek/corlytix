// const mybtn =   document.getElementsByClassName('mybtn')

// function changeAndStoreColor(color){
//     mybtn.style.backgroundColor = color;
//     localStorage.setItem('buttonColor', color);

// }

// mybtn.addEventListener('click', function() {
//     if (mybtn.style.backgroundColor === 'color') {
        
//     }
// })

document.addEventListener("DOMContentLoaded", () => {
      const buttons = document.querySelectorAll(".mybtn");

      buttons.forEach((button) => {
        button.addEventListener("click", () => {
          
          buttons.forEach((b) => {
            b.classList.remove("bg-green-500");
            b.classList.add("bg-blue-500"); 
          });
          
          button.classList.remove("bg-blue-500");
          button.classList.add("bg-green-500");
        });
      });
    });