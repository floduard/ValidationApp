// validationApp/static/js/scripts.js
document.addEventListener("DOMContentLoaded", function () {
    const addVehicleButton = document.getElementById("add-vehicle");
    const vehicleContainer = document.getElementById("vehicle-container");

    addVehicleButton.addEventListener("click", function () {
        const newVehicleInput = vehicleContainer.firstElementChild.cloneNode(true);
        resetVehicleInputs(newVehicleInput);
        vehicleContainer.appendChild(newVehicleInput);
    });

    vehicleContainer.addEventListener("click", function (event) {
        if (event.target.classList.contains("remove-vehicle")) {
            event.target.closest(".vehicle-input").remove();
        }
    });

    function resetVehicleInputs(vehicleInput) {
        // Reset values and clear validation messages
        vehicleInput.querySelectorAll("input").forEach(function (input) {
            input.value = "";
            input.setCustomValidity("");
        });
    }
});
