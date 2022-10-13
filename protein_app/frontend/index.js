
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

    // Default options are marked with *
    const response = await fetch(url, requestData);

    if (response.status !== 200) {
        return response.status === 200;
    } 
    return response.json(); // parses JSON response into native JavaScript objects
    
}

let userCredentials = {}

function refresh () {
    
    let refreshEndpoint = 'http://127.0.0.1:8000/api/token/refresh/'
    refreshToken = localStorage.getItem('refresh')

    if (refreshToken) {
                
        fetchData(refreshEndpoint, 'POST',{ 'refresh': refreshToken })
        .then((data) => {
            if (!data) {
                // display error message
            } else {
                console.log(data); // JSON data parsed by `data.json()` call
                userCredentials.access = data['access']
                localStorage.setItem('access', data['access']);
            }
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
        // console.log(data);
        if (data) {
            localStorage.clear();
            localStorage.setItem('access', data['access'])
            localStorage.setItem('refresh', data['refresh'])
        } else {
            // display error message here
        }

        
    })
}

let loginForm = document.querySelector('#login-form')
let loginButton = document.querySelector('#login-form-submit')

proteinContainer = document.querySelector('.protein-container')

loginButton.addEventListener('click', (e) => {
    e.preventDefault();
    const username = loginForm.username.value;
    const password = loginForm.password.value;
    const taxaId = loginForm.taxa.value;

    let proteinEndpoint = `http://127.0.0.1:8000/api/protein/${taxaId}/`


    getCredentials(username, password)

    access = localStorage.getItem('access')

    fetchData(proteinEndpoint, 'GET', null, {'Authorization': 'Bearer ' + access}).then((data) => {
        console.log(data)
        if (!data) {
            refresh()
        }
    })

})