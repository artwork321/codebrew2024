// database.js

// Wait for the DOM content to be loaded
document.addEventListener('DOMContentLoaded', function() {
    const charitiesTable = document.getElementById('charities');
    
    fetch('charities.json') // Fetch the JSON data from charities.json
        .then(response => response.json()) // Parse the JSON response
        .then(data => {
            // Map the data to extract only the relevant information for each charity
            const simplifiedData = data.map(charity => ({
                name: charity["Charity Name"],
                state: charity["State"]
            }));

            // Create a table element
            let table = document.createElement('table');

            // Calculate the number of rows needed
            const numRows = Math.ceil(simplifiedData.length / 4);

            // Iterate over the number of rows
            for (let i = 0; i < numRows; i++) {
                let row = table.insertRow();
                // Iterate over 4 charities for each row
                for (let j = 0; j < 4; j++) {
                    const index = i * 4 + j; // Calculate the index in the simplifiedData array
                    if (index < simplifiedData.length) {
                        let cell = row.insertCell();
                        cell.textContent = `${simplifiedData[index].name} - ${simplifiedData[index].state}`;
                    }
                }
            }

            // Append the table to the charities container
            charitiesTable.appendChild(table);
        })
        .catch(error => console.error('Error fetching JSON:', error)); // Log any errors that occur during fetching or parsing
});