function setupPickers() {
    console.log("working!");
    let config = {
        enableTime: false,
        dateFormat: "d/m/Y"
    };
    flatpickr("#id_start_date", config);
    flatpickr("#id_expiry_date", config);
}

window.addEventListener('load', function () {
    setupPickers();
});