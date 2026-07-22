// Login validation

function loginCheck(){

    let name = document.getElementById("name").value.trim();
    let email = document.getElementById("email").value.trim();
    let mobile = document.getElementById("mobile").value.trim();
    let password = document.getElementById("password").value.trim();

    if(name=="" || email=="" || mobile=="" || password==""){

        alert("Please fill all details");

        return false;
    }

    // Email validation
    let emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;

    if(!emailPattern.test(email)){

        alert("Please enter a valid email address.");

        return false;
    }

    // Mobile number validation
    let mobilePattern = /^[6-9][0-9]{9}$/;

    if(!mobilePattern.test(mobile)){

        alert("Please enter a valid 10-digit mobile number.");

        return false;
    }

    alert("Login Successful");

    return true;
}



// Resume analysis button

function analyzeResume(){

    alert("Resume analysis started...");

    window.location.href="recommendation.html";

}



// Email button

function sendEmail(){

    alert("Email notification sent successfully");

}



// WhatsApp button

function sendWhatsapp(){

    alert("WhatsApp notification sent successfully");

}



// Resume upload validation

function checkResume(){

    let file = document.getElementById("resume");

    if(file.files.length == 0){

        alert("Please upload your resume first.");

        return false;

    }

    return true;

}