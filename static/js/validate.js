const validator = new JustValidate("#registerForm")
const nameRegex = /^(?=.*[a-zA-Z])[a-zA-Z\s]{4,}$/
const numberRegex = /^(?:\+\d{1,3})?\d{10,13}$/
const emailRegex = /^[a-zA-Z0-9._%+-]+@gmail\.com$/
const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[\W_]).{5,}$/

validator.addField('#id_user_name',[
    {
    rule: 'required',
    errorMessage: 'Username is required.',
    },
    {
    rule: 'customRegexp',
    value: nameRegex,
    errorMessage: 'Name should not contain numbers.',
    },
])
.addField('#id_phone_number',[
    {
        rule:'required',
        errorMessage:'Phone Number is required.'
    },
    {
        rule:'customRegexp',
        value:numberRegex,
        errorMessage:"Invalid number."
    }
])
.addField('#id_email_address',[
    {
        rule:'required',
        errorMessage:'Email is required.'
    },
    {
        rule:'customRegexp',
        value:emailRegex,
        errorMessage:'Invalid Email.'
    }
])
.addField('#id_password',[
    {
        rule:'required',
        errorMessage:'Password is required.'
    },
    {
        rule:'customRegexp',
        value:passwordRegex,
        errorMessage: 'Choose a strong password.'
    }
])


validator.onSuccess((e)=>{
    e.target.submit()
})