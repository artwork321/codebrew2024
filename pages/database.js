fetch('./charities.json', {
    mode: 'no-cors'
})
    .then(response => response.json())
    .then(datapi => {
        // Process the JSON data
        console.log(datapi); // Example: Log the data to the console
    })
    .catch(error => {
        console.error('Error loading JSON:', error);
    });
