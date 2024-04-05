fetch('./charities.json')
    .then(response => response.json())
    .then(data => {
        // Process the JSON data
        console.log(data); // Example: Log the data to the console
    })
    .catch(error => {
        console.error('Error loading JSON:', error);
    });
