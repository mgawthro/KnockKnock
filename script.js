validateInput = () => {
    var inputElement = document.getElementById("bed");
    var inputValue = inputElement.value;

    // Check if the input is a positive integer and within the desired range
    if (/^[1-9]\d*$/.test(inputValue) && inputValue >= 0 && inputValue < 10) {
        // Valid input
        alert("Valid input: " + inputValue);
    } else {
        // Invalid input
        alert("Please enter a positive integer between 0 and 9");
        inputElement.value = ""; // Clear the input field
    }
}

// JavaScript function to dump form data
dumpFormData = () => {
    var form = document.getElementById("currentPosting");
    var formData = {};
    // Iterate through form elements
    var amenities = [];
    for (var i = 0; i < form.elements.length; i++) {
        var element = form.elements[i];
        // Check if the element is a form control with a name attribute
        if(element.name){
            if (element.type === "radio") {
                if (element.checked) {
                    formData[element.name] = element.value;
                }
            } else if(element.name === "amenities" && element.checked){
                amenities.push(element.id);
            } else if(element.type !== "button" && element.type !== "submit" && element.type !== "reset"){
                formData[element.name] = element.value;
            }
        }
    }
    formData["amenities"] = amenities;
    // Log the form data to the console
    console.log("Form data:", formData);
    // Alternatively, you can display the form data in an alert or update the HTML content
    // Example: alert("Form data:\n" + JSON.stringify(formData, null, 2));
}