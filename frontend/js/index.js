async function carregarHelps(){
    const response = await axios.get('http://projhelptechman-dev.us-east-1.elasticbeanstalk.com/helps')
  
    const helps = response.data

    const lista = document.getElementById('lista-helps')

    lista.innerHTML = ''


    helps.forEach(help => {
        const item = document.createElement('li')
        item.innerText = help.pergunta

        lista.appendChild(item)
    }); 
}

function incluirPerguntas(){
    const help_search = document.getElementById('help-search')
    const input_pergunta = document.getElementById('pergunta')

    help_search.onsubmit = async (event) => {
        event.preventDefault() 
        const help_pergunta = input_pergunta.value

        await axios.post('http://projhelptechman-dev.us-east-1.elasticbeanstalk.com/helps', {
            pergunta: help_pergunta
        })

        carregarHelps()
        alert('Pergunta cadastrada com sucesso!')

    }
}

function app(){
    console.log('Iniciado OK')
    carregarHelps()
    incluirPerguntas()
}

app()
