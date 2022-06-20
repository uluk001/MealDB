let login = document.querySelector('.login')
let register = document.querySelector('.register')
let modal = document.querySelector('.modal')
let btn = document.querySelector('.modal_btn') 

modal.style.display = 'none'

login.addEventListener( 'click', () =>{
    modal.style.display = 'block'
    btn.innerHTML = 'Войти' 
})


register.addEventListener( 'click', () =>{
    modal.style.display = 'block'
    btn.innerHTML = 'Регистрация' 
})

modal.addEventListener('click', () =>{
    modal.style.display = 'none'
})