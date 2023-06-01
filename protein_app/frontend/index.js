
// Example POST method implementation:
async function fetchData(url = '', method='', data={}, customHeaders={}) {
    var headers = {
        'Content-Type': 'application/json',
        'origin': '*',
    }
    
    var requestData = {
        method: method, // *GET, POST, PUT, DELETE, etc.
        mode: 'cors',
        headers: headers,
        body: JSON.stringify(data) // body data type must match "Content-Type" header
    }

    if (customHeaders) {
        Object.assign(headers, customHeaders)
    }
    // console.log(headers)
    if (!data){
        delete requestData.body
    }

    const response = await fetch(url, requestData);

    if (!response.ok) {
        const error = response.statusText || response.status;
        return Promise.reject(error);
    }
    
    return response.json(); // parses JSON response into native JavaScript objects
    
}

let userCredentials = {}

function refresh () {
    
    let refreshEndpoint = 'http://127.0.0.1:8000/api/token/refresh/'
    refreshToken = localStorage.getItem('refresh')

    if (refreshToken) {
                
        fetchData(refreshEndpoint, 'POST', { 'refresh': refreshToken })
        .then((data) => {
            console.log(data); // JSON data parsed by `data.json()` call
            userCredentials.access = data['access']
            localStorage.setItem('access', data['access']);
        }).catch(error => {
            // handle error here
            displayErrorMessage(error + " Login again")
            loadTaxaBtn = document.querySelector('#load-form-submit')
            loadTaxaBtn.style.opacity = 0
        });
    }
}


function getCredentials(username, password) {

    var tokenEndpoint = 'http://127.0.0.1:8000/api/token/'

    let requestData = {
        'username': username,
        'password': password
    }

    fetchData(tokenEndpoint, 'POST', requestData).then((data) => {

        localStorage.clear();
        localStorage.setItem('access', data['access'])
        localStorage.setItem('refresh', data['refresh'])
    }).catch(error => {
        // handle error here
        displayErrorMessage(error)
    });
}

function resetErrorMessage() {
    errorMessageElement = document.querySelector('#login-error-msg')
    errorMessageElement.innerHTML = ''
    errorMessageElement.style.opacity = 0
}

function displayErrorMessage(message) {
    errorMessageElement = document.querySelector('#login-error-msg')
    errorMessageElement.innerHTML = message
    errorMessageElement.style.opacity = 1
}

resetErrorMessage()

let loginForm = document.querySelector('#login-form')
let loginButton = document.querySelector('#login-form-submit')

proteinContainer = document.querySelector('.protein-container')
loadTaxaBtn = document.querySelector('#load-form-submit')

loginButton.addEventListener('click', (e) => {

    e.preventDefault();
    resetErrorMessage();

    const username = loginForm.username.value;
    const password = loginForm.password.value;
    const taxaId = loginForm.taxa.value;

    let proteinEndpoint = `http://127.0.0.1:8000/api/protein/${taxaId}/`

    getCredentials(username, password)

    localStorage.setItem('taxaID', taxaId)
    console.log(localStorage.getItem('taxaID'))
    access = localStorage.getItem('access')

    fetchData(proteinEndpoint, 'GET', null, {'Authorization': 'Bearer ' + access}).then((data) => {
        console.log(data)
        loadTaxaBtn.style.opacity = 1

    }).catch(error => {
        displayErrorMessage(error + " login again")
    });

})

loadTaxaBtn.addEventListener('click', (e) => {
    e.preventDefault();
    resetErrorMessage();

    const access = localStorage.getItem('access')
    const taxaId = localStorage.getItem('taxaID')
    
    let proteinEndpoint = `http://127.0.0.1:8000/api/protein/${taxaId}/`

    fetchData(proteinEndpoint, 'GET', null, {'Authorization': 'Bearer ' + access}).then((data) => {
        console.log(data)
    }).catch(error => {
        displayErrorMessage(error + " load again")
        refresh();
    });

})

// 53326
// ASEW2345