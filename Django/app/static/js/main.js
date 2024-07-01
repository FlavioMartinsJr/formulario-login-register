const logar = document.getElementById("form-logar")
const registrar = document.getElementById("form-registrar")

function OpenOrCloseForms(){
    event.preventDefault();

    if(logar.classList.length == 1 && registrar.classList.length > 1)
    {
        console.log("primeira condição")
        console.log(logar)
        console.log(registrar)

        logar.className = 'container-form deactive';
        registrar.className = 'container-form';
        
    }else if(registrar.classList.length == 1 && logar.classList.length > 1){

        console.log("segunda condição")
        console.log(logar)
        console.log(registrar)

        logar.className = 'container-form ';
        registrar.className = 'container-form deactive';
    }
    
}