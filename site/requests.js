const getAttritionButton = document.getElementById('getAttrition')
const getAttritionOvertimeButton = document.getElementById('getAttritionOvertime')

const attritionTextbox = document.getElementById('attrition')
const attritionOvertimeTextbox = document.getElementById('attritionOvertime')

const addEmployeeButton = document.getElementById('addEmployee')
const addEmployeeForm = document.getElementById('addEmployeeForm')


const getAttrition = async () => {
    const response = await fetch('http://localhost:8080/attrition');
    const responseJson = await response.json()

    attritionTextbox.innerHTML = (responseJson.attrition * 100).toFixed(2) + '%'
}

const getAttritionOvertime = async () => {
    const response = await fetch('http://localhost:8080/attrition-overtime');
    const responseJson = await response.json()

    attritionOvertimeTextbox.innerHTML = (responseJson.attritionOvertime * 100).toFixed(2) + '%'
}

const addEmployee = async event => {
    // Prevents page reload
    event.preventDefault()

    const headers = {
        'Content-Type': 'application/json'
    }

    const formData = new FormData(addEmployeeForm)
    const jsonBody = {}
    for (const [key, value] of formData.entries()) {
        jsonBody[key] = value
    }

    jsonBody.employeeNumber = Number(jsonBody.employeeNumber)

    // Cast the checkbox state to a boolean - why aren't checkboxes boolean??
    // https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/checkbox#attr-value
    jsonBody.attrition = jsonBody.attrition === 'on'

    try {
        const response = await fetch('http://localhost:8080/add-row', {
            method: 'POST',
            headers,
            body: JSON.stringify(jsonBody)
        })

        if (response.status != 200)
            window.alert('Error adding customer ' + jsonBody.employeeNumber)
    } catch (error) {
        console.error(error)
    }
}


getAttritionButton.addEventListener('click', getAttrition);
getAttritionOvertimeButton.addEventListener('click', getAttritionOvertime);
// ??
addEmployeeButton.addEventListener('click', async event => addEmployee(event));

// addEmployeeForm.addEventListener('submit', async function(event) {
//     await addEmployee(event, this)
// })